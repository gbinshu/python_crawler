# -*- coding: utf-8 -*-

import json

import pandas
import redis

from genurl.create_start_urls import lists_detail
from pyspark import SQLContext
from pyspark.sql import SparkSession, DataFrame

pool = redis.ConnectionPool(host="127.0.0.1", password="")
redis_obj = redis.Redis(connection_pool=pool)

spark = SparkSession.builder.appName("salary_peocessing").getOrCreate()
sc = spark.sparkContext
sparkSqlContest = SQLContext(sc)

conn_param = {}
conn_param['user'] = 'root'
conn_param['password'] = '123456'
conn_param['driver'] = "com.mysql.jdbc.Driver"


dicts_detail = [[] for i in range(5)]
[dicts_detail[i].append([]) for i in range(5) for j in range(5)]


#gain average salary per month
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += int(num[i])
    nsum_month = nsum / 12
    return round(nsum_month / len(num), 2)


#salary type from str to int
def modify_salary(raw_salary):
    lists = []
    lists = raw_salary.str.split("-")
    lists = [averagenum(i) for i in lists ]
    return lists


#obtain useful salary information
for i in range(0, 5):
    for j in range(0, 5):
        for k in redis_obj.lrange(lists_detail[i][j] + "salary:information", 0, -1):
            dict_tmp = {}
            dict_tmp = json.loads(k, encoding="utf-8")
            if dict_tmp["salary"] !="面议":
                dicts_detail[i][j].append(dict_tmp)


#pandas_df to spark_df
pd_df_detail = [[] for i in range(5)]
[pd_df_detail[i].append([]) for i in range(5) for j in range(5)]
spark_df_detail = pd_df_detail

for i in range(0, 5):
    for j in range(0, 5):
        # 创建DataFrame对象的数据可以为列表，数组和字典，列名和索引为列表对象
        pd_df_detail[i][j] = pandas.DataFrame(dicts_detail[i][j])
        # pd_df_detail[i][j]["salary"]类型为Series
        pd_df_detail[i][j]["salary"] = modify_salary(pd_df_detail[i][j]["salary"].str.replace("万", ""))
        # #pandas_df to spark_df
        spark_df_detail[i][j] = sparkSqlContest.createDataFrame(pd_df_detail[i][j])  #spark_df to pandas_df: spark_df_detail[i][j].toPandas()
        spark_df_detail[i][j].write.jdbc("jdbc:mysql://127.0.0.1:3306/salaryPro", lists_detail[i][j] + "_info", 'overwrite', conn_param)

        # pd_df to json
        # pd_df_detail[i][j].to_json(orient='records', force_ascii=False)
















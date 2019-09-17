import redis

from genurl.creare_urls_list2 import lists, lists_detail

pool = redis.ConnectionPool(host="127.0.0.1", password="")
redis_obj = redis.Redis(connection_pool=pool)

#爬虫链接存入redis中
if __name__ == '__main__':
    print("urls have been ran directly")
    print("Beginning generating urls")
    for i in range(0, 5):
        for j in range(0, 5):
            for k in range(0, 100):
                url = lists[i][j].format(k)
                redis_obj.rpush(lists_detail[i][j] + "salary:start_urls", url)

    print("Generating Done")



'''
大数据
北京
https://www.liepin.com/zhaopin/?init=-1&headckid=4b80f408c16786e9&fromSearchBtn=2&dqs=010&sfrom=click-pc_homepage-centre_searchbox-search_new&ckid=b9e6aba8a4fba5ac&degradeFlag=0&key=%E5%A4%A7%E6%95%B0%E6%8D%AE&siTag=LGV-fc5u_67LtFjetF6ACg%7EF5FSJAXvyHmQyODXqGxdVw&d_sfrom=search_fp&d_ckId=64636213defb1d00321c1a420738864a&d_curPage=0&d_pageSize=40&d_headId=64636213defb1d00321c1a420738864a&curPage={}
上海
https://www.liepin.com/zhaopin/?init=-1&headckid=4b80f408c16786e9&fromSearchBtn=2&dqs=020&ckid=800e3b29cdd650ef&degradeFlag=0&sfrom=click-pc_homepage-centre_searchbox-search_new&key=%E5%A4%A7%E6%95%B0%E6%8D%AE&siTag=LGV-fc5u_67LtFjetF6ACg~r3i1HcfrfE3VRWBaGW6LoA&d_sfrom=search_fp&d_ckId=51a4736751df4412a9fa7c31ee508d8f&d_curPage=1&d_pageSize=40&d_headId=51a4736751df4412a9fa7c31ee508d8f&curPage={}
广州
https://www.liepin.com/zhaopin/?init=-1&headckid=4b80f408c16786e9&fromSearchBtn=2&dqs=050020&ckid=3db0dfbf57675e98&degradeFlag=0&sfrom=click-pc_homepage-centre_searchbox-search_new&key=%E5%A4%A7%E6%95%B0%E6%8D%AE&siTag=LGV-fc5u_67LtFjetF6ACg%7E_FrslumzzaHrHe3aSW0VTQ&d_sfrom=search_fp&d_ckId=672a18fa2cbf5087717be6a452e36444&d_curPage=0&d_pageSize=40&d_headId=64636213defb1d00321c1a420738864a&curPage={}
成都
https://www.liepin.com/zhaopin/?init=-1&headckid=4b80f408c16786e9&fromSearchBtn=2&dqs=280020&ckid=ff8d5941cfe240b8&degradeFlag=0&sfrom=click-pc_homepage-centre_searchbox-search_new&key=%E5%A4%A7%E6%95%B0%E6%8D%AE&siTag=LGV-fc5u_67LtFjetF6ACg%7EDARaeHgTI7JY9N3sNhM1Ow&d_sfrom=search_fp&d_ckId=b54fee346e784ed50abefe301e1448f9&d_curPage=0&d_pageSize=40&d_headId=64636213defb1d00321c1a420738864a&curPage={}
深圳
https://www.liepin.com/zhaopin/?init=-1&headckid=4b80f408c16786e9&fromSearchBtn=2&dqs=050090&ckid=5c5f911e8f9a9125&degradeFlag=0&sfrom=click-pc_homepage-centre_searchbox-search_new&key=%E5%A4%A7%E6%95%B0%E6%8D%AE&siTag=LGV-fc5u_67LtFjetF6ACg%7E-nQsjvAMdjst7vnBI-6VZQ&d_sfrom=search_fp&d_ckId=25dba427bd29c7c44542ca7c5982d496&d_curPage=0&d_pageSize=40&d_headId=64636213defb1d00321c1a420738864a&curPage={}
'''
'''
安卓
北京
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=010&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=安卓&init=-1&searchType=1&headckid=57406d993ac3e834&compkind=&fromSearchBtn=2&sortFlag=15&ckid=cbe2fd39c33a1915&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=QZB2XplsFaQhH9ggxlcL2A~F5FSJAXvyHmQyODXqGxdVw&d_sfrom=search_prime&d_ckId=51f19c3fed46785861aff7c48ce654a1&d_curPage=0&d_pageSize=40&d_headId=7c216b670bacf9dc47b54dde8ac4432f&curPage={}
上海
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=安卓&init=-1&searchType=1&headckid=57406d993ac3e834&compkind=&fromSearchBtn=2&sortFlag=15&ckid=95364036dfea386b&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=QZB2XplsFaQhH9ggxlcL2A~r3i1HcfrfE3VRWBaGW6LoA&d_sfrom=search_prime&d_ckId=18ece6a9d5493aac0ff00894437acbfb&d_curPage=0&d_pageSize=40&d_headId=7c216b670bacf9dc47b54dde8ac4432f&curPage={}
广州
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=%E5%AE%89%E5%8D%93&init=-1&searchType=1&headckid=57406d993ac3e834&compkind=&fromSearchBtn=2&sortFlag=15&ckid=6f2bbe111e45c460&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=QZB2XplsFaQhH9ggxlcL2A%7E_FrslumzzaHrHe3aSW0VTQ&d_sfrom=search_prime&d_ckId=dadf5d5d2f3cccf1d79491457678bf41&d_curPage=0&d_pageSize=40&d_headId=7c216b670bacf9dc47b54dde8ac4432f&curPage={}
成都
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=280020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=安卓&init=-1&searchType=1&headckid=57406d993ac3e834&compkind=&fromSearchBtn=2&sortFlag=15&ckid=2aa3ecf5c1ee0fa3&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=QZB2XplsFaQhH9ggxlcL2A~DARaeHgTI7JY9N3sNhM1Ow&d_sfrom=search_prime&d_ckId=7a9a16a1e5599cf4ec5083e2eeef5e14&d_curPage=0&d_pageSize=40&d_headId=7c216b670bacf9dc47b54dde8ac4432f&curPage={}
深圳
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050090&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=安卓&init=-1&searchType=1&headckid=57406d993ac3e834&compkind=&fromSearchBtn=2&sortFlag=15&ckid=3330a9b3e207bbdc&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=QZB2XplsFaQhH9ggxlcL2A~-nQsjvAMdjst7vnBI-6VZQ&d_sfrom=search_prime&d_ckId=824b0d598ae91c262bed2e931d762b75&d_curPage=0&d_pageSize=40&d_headId=7c216b670bacf9dc47b54dde8ac4432f&curPage={}
'''
'''
JAVA WEB
北京
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=010&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=JAVA+WEB&init=-1&searchType=1&headckid=b64fe0fa3f68f09b&compkind=&fromSearchBtn=2&sortFlag=15&ckid=f02173337d4f32f9&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=NCJaCOmz2ySemnvFiPv1tQ~F5FSJAXvyHmQyODXqGxdVw&d_sfrom=search_prime&d_ckId=cdcc136a3f0c2196cf467d8af76344dd&d_curPage=0&d_pageSize=40&d_headId=785fbc85f0c9bd8584b9173c56ff688a&curPage={}
上海
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=JAVA+WEB&init=-1&searchType=1&headckid=b64fe0fa3f68f09b&compkind=&fromSearchBtn=2&sortFlag=15&ckid=bad6fba3c0e0b6b6&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=NCJaCOmz2ySemnvFiPv1tQ~r3i1HcfrfE3VRWBaGW6LoA&d_sfrom=search_prime&d_ckId=85dd3366a574f6d946a49f50583441bd&d_curPage=0&d_pageSize=40&d_headId=785fbc85f0c9bd8584b9173c56ff688a&curPage={}
广州
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=JAVA+WEB&init=-1&searchType=1&headckid=b64fe0fa3f68f09b&compkind=&fromSearchBtn=2&sortFlag=15&ckid=2f6d7b2dc90b02d5&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=NCJaCOmz2ySemnvFiPv1tQ~_FrslumzzaHrHe3aSW0VTQ&d_sfrom=search_prime&d_ckId=dd6509d0da8b42436e734eae8529fd52&d_curPage=0&d_pageSize=40&d_headId=785fbc85f0c9bd8584b9173c56ff688a&curPage={}
成都
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=280020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=JAVA+WEB&init=-1&searchType=1&headckid=b64fe0fa3f68f09b&compkind=&fromSearchBtn=2&sortFlag=15&ckid=85f910bb3cb63e8c&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=NCJaCOmz2ySemnvFiPv1tQ~DARaeHgTI7JY9N3sNhM1Ow&d_sfrom=search_prime&d_ckId=29943640070c4eb1fc4401ccfaaa17e1&d_curPage=0&d_pageSize=40&d_headId=785fbc85f0c9bd8584b9173c56ff688a&curPage={}
深圳
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050090&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=JAVA+WEB&init=-1&searchType=1&headckid=b64fe0fa3f68f09b&compkind=&fromSearchBtn=2&sortFlag=15&ckid=6ee7f929c02c095e&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=NCJaCOmz2ySemnvFiPv1tQ~-nQsjvAMdjst7vnBI-6VZQ&d_sfrom=search_prime&d_ckId=6c6f053a25515a5b9e609a87f5d80a12&d_curPage=0&d_pageSize=40&d_headId=785fbc85f0c9bd8584b9173c56ff688a&curPage={}
'''
'''
算法
北京
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=010&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=算法&init=-1&searchType=1&headckid=129606c2f3dbc166&compkind=&fromSearchBtn=2&sortFlag=15&ckid=74754321016e6484&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=BGqJnuem7IjTcCEaUYyegA~F5FSJAXvyHmQyODXqGxdVw&d_sfrom=search_prime&d_ckId=f638733957e085e35621a1a7bad791ac&d_curPage=0&d_pageSize=40&d_headId=8c51ed50c2c5e83138b1579c6e65db4c&curPage={}
上海
http://liepin.com/zhaopin/?isAnalysis=&dqs=020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=算法&init=-1&searchType=1&headckid=129606c2f3dbc166&compkind=&fromSearchBtn=2&sortFlag=15&ckid=f20aca5f692c0e53&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=BGqJnuem7IjTcCEaUYyegA~r3i1HcfrfE3VRWBaGW6LoA&d_sfrom=search_prime&d_ckId=725e5e6c6df7a2122415aae090a43e9e&d_curPage=0&d_pageSize=40&d_headId=8c51ed50c2c5e83138b1579c6e65db4c&curPage={}
广州
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=算法&init=-1&searchType=1&headckid=129606c2f3dbc166&compkind=&fromSearchBtn=2&sortFlag=15&ckid=77f9d052003efcb6&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=BGqJnuem7IjTcCEaUYyegA~_FrslumzzaHrHe3aSW0VTQ&d_sfrom=search_prime&d_ckId=d3952a157de8bc53379121366881560b&d_curPage=0&d_pageSize=40&d_headId=8c51ed50c2c5e83138b1579c6e65db4c&curPage={}
成都
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=280020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=算法&init=-1&searchType=1&headckid=129606c2f3dbc166&compkind=&fromSearchBtn=2&sortFlag=15&ckid=129606c2f3dbc166&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=BGqJnuem7IjTcCEaUYyegA~DARaeHgTI7JY9N3sNhM1Ow&d_sfrom=search_prime&d_ckId=8c51ed50c2c5e83138b1579c6e65db4c&d_curPage=0&d_pageSize=40&d_headId=8c51ed50c2c5e83138b1579c6e65db4c&curPage={}
深圳
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050090&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=算法&init=-1&searchType=1&headckid=129606c2f3dbc166&compkind=&fromSearchBtn=2&sortFlag=15&ckid=774a219b22337e85&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=BGqJnuem7IjTcCEaUYyegA~-nQsjvAMdjst7vnBI-6VZQ&d_sfrom=search_prime&d_ckId=b04d450af7c8d64aff0bf54e5030bd94&d_curPage=0&d_pageSize=40&d_headId=8c51ed50c2c5e83138b1579c6e65db4c&curPage={}
'''
'''
数据库
北京100
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=010&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=数据库&init=-1&searchType=1&headckid=9c2f4564190b3547&compkind=&fromSearchBtn=2&sortFlag=15&ckid=a6d2d3ce53c8060c&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=aAUb9KonQ7AwmEtpRijunA~F5FSJAXvyHmQyODXqGxdVw&d_sfrom=search_prime&d_ckId=0db239f6c1e9893f136e00cbbad1bf43&d_curPage=0&d_pageSize=40&d_headId=0db239f6c1e9893f136e00cbbad1bf43&curPage={}
上海
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=数据库&init=-1&searchType=1&headckid=9c2f4564190b3547&compkind=&fromSearchBtn=2&sortFlag=15&ckid=a1676cd8443d6ec1&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=aAUb9KonQ7AwmEtpRijunA~r3i1HcfrfE3VRWBaGW6LoA&d_sfrom=search_prime&d_ckId=0dbe72063e33bdcd887ba223c5a951ca&d_curPage=0&d_pageSize=40&d_headId=0db239f6c1e9893f136e00cbbad1bf43&curPage={}
广州
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=数据库&init=-1&searchType=1&headckid=9c2f4564190b3547&compkind=&fromSearchBtn=2&sortFlag=15&ckid=1f73b7f2999b8f14&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=aAUb9KonQ7AwmEtpRijunA~_FrslumzzaHrHe3aSW0VTQ&d_sfrom=search_prime&d_ckId=5198140029010b884820dd96d736c77a&d_curPage=0&d_pageSize=40&d_headId=0db239f6c1e9893f136e00cbbad1bf43&curPage={}
成都89
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=280020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=数据库&init=-1&searchType=1&headckid=9c2f4564190b3547&compkind=&fromSearchBtn=2&sortFlag=15&ckid=352e8ddf6af532a1&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=aAUb9KonQ7AwmEtpRijunA~DARaeHgTI7JY9N3sNhM1Ow&d_sfrom=search_prime&d_ckId=a25c2ccebec51fb41d8f9f11deeb7636&d_curPage=0&d_pageSize=40&d_headId=0db239f6c1e9893f136e00cbbad1bf43&curPage={}
深圳
https://www.liepin.com/zhaopin/?isAnalysis=&dqs=050090&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=数据库&init=-1&searchType=1&headckid=9c2f4564190b3547&compkind=&fromSearchBtn=2&sortFlag=15&ckid=515198d5f3e3bd0b&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=aAUb9KonQ7AwmEtpRijunA~-nQsjvAMdjst7vnBI-6VZQ&d_sfrom=search_prime&d_ckId=38736310b923b941b9b827807964c0fd&d_curPage=0&d_pageSize=40&d_headId=0db239f6c1e9893f136e00cbbad1bf43&curPage={}
'''

# redis_obj.rpush("salary:start_urls", "https://www.liepin.com/zhaopin/?isAnalysis=&dqs=280020&pubTime=&salary=&subIndustry=&industryType=&compscale=&key=数据库&init=-1&searchType=1&headckid=9c2f4564190b3547&compkind=&fromSearchBtn=2&sortFlag=15&ckid=352e8ddf6af532a1&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=aAUb9KonQ7AwmEtpRijunA~DARaeHgTI7JY9N3sNhM1Ow&d_sfrom=search_prime&d_ckId=a25c2ccebec51fb41d8f9f11deeb7636&d_curPage=0&d_pageSize=40&d_headId=0db239f6c1e9893f136e00cbbad1bf43&curPage=100")






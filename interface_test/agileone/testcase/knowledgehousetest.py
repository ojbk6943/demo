from interface_test.agileone.common.knowledgehouse import KnowledgeHouse
from interface_test.agileone.util.utility import Utility
from random import randint
import json
class KnowledgeHouseTest:
    def test_query_knowledge(self,session,query_knowledge_url):
        #从数据库随机获取一条知识仓库的记录
        sql='select * from knowledge'
        result=Utility.query_all(sql)

        randint_index=randint(0,len(result)-1)
        randint_knowledgeid=result[randint_index][0]
        randint_headline = result[randint_index][4]
        randint_creator = result[randint_index][2]
        randint_type = result[randint_index][3]
        randint_projectid = result[randint_index][1]
        query_knowledge_data={'knowledgeid':randint_knowledgeid,'headline':randint_headline,
                              'creator':randint_creator,'type':randint_type,'projectid':randint_projectid}
        query_knowledge_respanse=KnowledgeHouse().query_knowledge(session,query_knowledge_url,query_knowledge_data)
        content=query_knowledge_respanse.json()
        print(content[0]['knowledgeid'])
        print(randint_knowledgeid)
        print('oooooooooooooooooooooooooooooooooooooooooooooooooooo')
        if  content[0]['knowledgeid']==randint_knowledgeid and content[0]['headline']==randint_headline\
             and content[0]['creator']==randint_creator and content[0]['type']==randint_type\
            and content[0]['projectid']==randint_projectid :
            actual= 'query knowledge success'

        else:
            actual = 'query knowledge fail'
        #断言
        flag=Utility.assertequal('query knowledge success',actual)
        if flag :
            print('test query knowledge success')
        else:
            print('test query knowledge fail')

















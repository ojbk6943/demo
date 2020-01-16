class KnowledgeHouse:
    def add_knowledge(self, session, add_notice_url, add_notice_data):
        return session.post(add_notice_url, add_notice_data)

    def edit_knowledge(self, session, edit_notice_url, edit_notice_data):
        return session.post(edit_notice_url, edit_notice_data)
    def query_knowledge(self,session,query_knowledge_url,query_knowledge_data):
        return  session.post(query_knowledge_url,query_knowledge_data)

    def delete_knowledge(self, session, delete_notice_url, delete_notice_data):
        return session.post(delete_notice_url, delete_notice_data)
#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Notice:

    def add_notice(self,session,add_notice_url,add_notice_data):
        return session.post(add_notice_url,add_notice_data)

    def edit_notice(self,session,edit_notice_url,edit_notice_data):
        return session.post(edit_notice_url,edit_notice_data)

    def query_notice(self,session,query_notice_url,query_notice_data):
        return session.post(query_notice_url,query_notice_data)

    def delete_notice(self,session,delete_notice_url,delete_notice_data):
        return session.post(delete_notice_url,delete_notice_data)
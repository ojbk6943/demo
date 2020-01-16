#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Requirement:

    def add_requirement(self,session,add_requirement_url,add_requirement_data):
        return session.post(add_requirement_url,add_requirement_data)

    def edit_requirement(self,session,edit_requirement_url,edit_requirement_data):
        return session.post(edit_requirement_url,edit_requirement_data)

    def query_requirement(self,session,query_requirement_url,query_requirement_data):
        return session.post(query_requirement_url,query_requirement_data)

    def delete_requirement(self,session,delete_requirement_url,delete_requirement_data):
        return session.post(delete_requirement_url,delete_requirement_data)

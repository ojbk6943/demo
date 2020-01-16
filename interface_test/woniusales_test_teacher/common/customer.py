#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Customer:

    def add_customer(self, session, add_customer_url, add_customer_data):
        return session.post(add_customer_url, add_customer_data)

    def edit_customer(self, session, edit_customer_url, edit_customer_data):
        return session.post(edit_customer_url, edit_customer_data)

    def query_customer(self, session, query_customer_url, query_customer_data):
        return session.post(query_customer_url, query_customer_data)

   
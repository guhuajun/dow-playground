# -*- coding: utf-8 -*-
# pylint: disable=

from locust import HttpLocust, TaskSet


# def login(l):
#     l.client.post("/manager/status", {"username":"ellen_key", "password":"education"})

def index(l):
    l.client.get("/")

def test(l):
    l.client.get("/spring-mvc-showcase/views/test")

class UserBehavior(TaskSet):
    tasks = {index: 1, test: 4}

    # def on_start(self):
    #     login(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

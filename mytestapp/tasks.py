#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020-06-01 15:44
# @Author : tuxingguo
# @File : tasks.py
# @Software : PyCharm

from celery import task


@task
def mul(x, y):
    return x * y

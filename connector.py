#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connections.Connection(host='192.168.0.42',
                                      user='patrick',
                                      password='secret',
                                      database='rezeptdb',
                                      charset='utf8')

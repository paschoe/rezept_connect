#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql


def mysql_connect():
    conn = pymysql.connections.Connection(host='192.168.0.42',
                                          user='patrick',
                                          password='secret',
                                          database='rezeptdb',
                                          charset='utf8')
    return conn


def get_existing():
    with mysql_connect().cursor() as cursor:
        # Read a single record
        sql = "SELECT rezept_id, name FROM rezept_main ORDER BY name"
        cursor.execute(sql)
        rezepte = cursor.fetchall()

        print(u"==================================================================")
        print("Vorhandene Rezepte:")
        for k in range(0, len(rezepte)):
            d = unicode(rezepte[k][0]) + " " + rezepte[k][1]
            print(d)
        print(u"------------------------------------------------------------------")

        rezept_id = raw_input("Eingabe der Nummer des gewuenschten Rezepts: ")
        print(u"------------------------------------------------------------------")

        rezept_name = u""
        for i in range(0,len(rezepte)):
            if int(rezepte[i][0]) == int(rezept_id):
                rezept_name = unicode(rezepte[i][1])

        cursor.close()

    return rezept_id, rezept_name, rezepte


def get_rezept(rezept_id):
    with mysql_connect().cursor() as cursor:
        sql_zutaten = u"SELECT m.menge, m.einheit, m.zutat FROM zutaten_menge AS m JOIN rezept_main As r " \
                      u"USING(rezept_ID) WHERE rezept_id=" + unicode(rezept_id)
        sql_addinf = u"SELECT a.ofeneinstellung,a.temperatur,a.Backform,a.zub1,a.zub2,a.zub3,a.zub4,a.zub5,a.zub6 " \
                     u"FROM rezept_add AS a JOIN rezept_main AS r USING(rezept_ID) " \
                     u"WHERE r.rezept_id=" + unicode(rezept_id)
        cursor.execute(sql_zutaten)
        zutaten = cursor.fetchall()
        cursor.execute(sql_addinf)
        addinf = cursor.fetchone()
        cursor.close()
    return zutaten,addinf

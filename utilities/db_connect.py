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


def get_rezept_list():
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
    return zutaten, addinf


def get_zutaten_list():
    sql = u"SELECT zutat FROM zutaten"
    with mysql_connect().cursor() as cursor:
        cursor.execute(sql)
        raw_zutaten = cursor.fetchall()
        zutaten = []
        for i in range(0, len(raw_zutaten)):
            zutaten.append(raw_zutaten[i][0])
    return zutaten


def add_rezept_main(name, typ, subtyp, commit):
    sql = u'INSERT INTO rezept_main(name,typ,subtyp) VALUES (' + name + u',' + typ + u',' + subtyp + u')'
    with mysql_connect().cursor() as cursor:
        cursor.execute(sql)
    if commit is True:
        mysql_connect().commit()


def get_zutaten_typen_list():
    sql = u"SELECT typ FROM zutaten GROUP BY typ"
    with mysql_connect().cursor() as cursor:
        cursor.execute(sql)
        exist_typ = cursor.fetchall()
        output = []
        for i in range(0,len(exist_typ)):
            if type(exist_typ[i][0]) is unicode:
                output.append(exist_typ[i][0])
        print(u"Vorhandene Zutatstypen: " + u",".join(output))


def add_zutaten(zutaten, typen, commit):
    with mysql_connect().cursor() as cursor:
        sql_data = []
        for k in range(0, len(zutaten)):
            sql_data.append(u'(' + zutaten[k] + u',' + typen[k] + u')')
        sql = u'INSERT INTO zutaten(zutat,typ) VALUES ' + u','.join(sql_data)
        cursor.execute(sql)
    if commit is True:
        mysql_connect().commit()
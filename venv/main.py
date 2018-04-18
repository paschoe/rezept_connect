#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connections.Connection(host='192.168.0.42',
                                      user='patrick',
                                      password='secret',
                                      database='rezeptdb',
                                      charset='utf8')

sql_zutaten = u"SELECT m.menge, m.einheit, m.zutat FROM zutaten_menge AS m JOIN rezept_main AS r USING(rezept_ID) WHERE r.name="

try:
    with conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT rezept_id, name FROM rezept_main"
        cursor.execute(sql)
        rezepte = cursor.fetchall()

        print("===================")
        print("Vorhandene Rezepte:")
        for k in range(0,len(rezepte)):
            d = unicode(rezepte[k][0])+" "+rezepte[k][1]
            print(d)
        print("===================")

        for i in range(0,len(rezepte)):
            rezept_str = (rezepte[i][0])
            query = sql_zutaten + '"' +rezept_str +'"'
            query = query.encode('utf-8')
            cursor.execute(query)
            zutaten = (cursor.fetchall())
            print("Zutaten fuer " + rezept_str +":")
            disp_zutat=[]
            for j in range(0,len(zutaten)):
                if zutaten[j][0] != None:
                    menge = unicode(zutaten[j][0])
                else:
                    menge = unicode("")
                if zutaten[j][1] != None:
                    einheit = zutaten[j][1]
                else:
                    einheit = unicode("")
                name = zutaten[j][2]
                print(name)
                a = unicode(menge + einheit + " " + name)
                disp_zutat.append(a)
            print(disp_zutat[1])


finally:
    conn.close()

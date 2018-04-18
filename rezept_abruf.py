#!/usr/bin/env python
# -*- coding: utf-8 -*-

import connector as c

sql_zutaten = u"SELECT m.menge, m.einheit, m.zutat FROM zutaten_menge AS m JOIN rezept_main AS r USING(rezept_ID) WHERE r.rezept_id="

try:
    with c.conn.cursor() as cursor:
        # Read a single record
        sql = "SELECT rezept_id, name FROM rezept_main"
        cursor.execute(sql)
        rezepte = cursor.fetchall()

        print("===================")
        print("Vorhandene Rezepte:")
        for k in range(0,len(rezepte)):
            d = unicode(rezepte[k][0])+" "+rezepte[k][1]
            print(d)
        print("-------------------")

        rezept_id = raw_input("Eingabe der Nummer des gewuenschten Rezepts: ")
        print("-------------------")

        query = sql_zutaten + unicode(rezept_id)
        query = query.encode('utf-8')
        cursor.execute(query)
        zutaten = (cursor.fetchall())
        rezept_name = unicode(rezepte[int(rezept_id)-1][1])
        print("Zutaten fuer " + rezept_name +":")
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
            a = unicode(menge + einheit + " " + name)
            disp_zutat.append(a)
            print(disp_zutat[j])


finally:
    c.conn.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import connector as c

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

finally:
    cursor.close()
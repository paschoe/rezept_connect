#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utilities import connector as c


def get_existing():
    with c.mysql_connect().cursor() as cursor:
        # Read a single record
        sql = "SELECT rezept_id, name FROM rezept_main"
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

        cursor.close()

    return rezept_id

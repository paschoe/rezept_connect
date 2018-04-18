#!/usr/bin/env python
# -*- coding: utf-8 -*-

import connector as c

sql_get_zutaten = u"SELECT zutat FROM zutaten"
sql_get_typen = u"SELECT typ FROM zutaten GROUP BY typ"

try:
    with c.conn.cursor() as cursor:
        cursor.execute(sql_get_zutaten)
        exist_zutaten = cursor.fetchall()
        z = []
        for i in range(0,len(exist_zutaten)):
            z.append(exist_zutaten[i][0])

        print z

        data_new_zutat =[]
        zutat = []
        menge = []
        einheit = []
        new_zutat = ""
        while new_zutat != "ende":
            new_zutat = raw_input("Eingabe der Zutat: ")
            if new_zutat == 'ende':
                break
            new_zutat = new_zutat.decode("utf-8")
            zutat.append(new_zutat)
            new_menge = raw_input("Eingabe der Menge ohne Einheit: ")
            if new_menge != '':
                menge.append(int(new_menge))
            else:
                menge.append(None)
            new_einheit = raw_input("Eingabe der Einheit: ")
            if new_einheit != '':
                einheit.append(new_einheit.decode("utf-8"))
            else:
                einheit.append(None)

            if (new_zutat not in z and new_zutat != unicode("ende")):
                data_new_zutat.append(new_zutat)

        print zutat
        print menge
        print einheit

        print("======================")
        print("Vorhandene Zutatstypen")
        cursor.execute(sql_get_typen)
        exist_typ = cursor.fetchall()
        print(exist_typ)
        print("----------------------")
        data_new_typ =[]
        for j in range(0,len(data_new_zutat)):
            d = raw_input("Definiere den Typ der neuen Zutat " + data_new_zutat[j] +":")
            d = d.decode("utf-8")
            data_new_typ.append(d)
        print data_new_zutat
        print data_new_typ

finally:
    c.conn.close()
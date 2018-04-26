#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utilities import connector as c

sql_zutaten = u"SELECT m.menge, m.einheit, m.zutat FROM zutaten_menge AS m JOIN rezept_main AS r USING(rezept_ID) " \
              u"WHERE r.rezept_id="
sql_addinf = u'SELECT a.ofeneinstellung,a.temperatur,a.Backform,a.zub1,a.zub2,a.zub3,a.zub4,a.zub5,a.zub6 ' \
             u'FROM rezept_add AS a JOIN rezept_main AS r USING(rezept_ID) WHERE r.rezept_id='

try:
    with c.mysql_connect().cursor() as cursor:
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
        print("=========================")

        query = sql_zutaten + unicode(rezept_id)
        query = query.encode('utf-8')
        cursor.execute(query)
        zutaten = (cursor.fetchall())
        for p in range(0,len(rezepte)):
            if int(rezepte[p][0]) == int(rezept_id):
                rezept_name = unicode(rezepte[p][1])

        print("Zutaten fuer " + rezept_name +":")
        print("-------------------------")
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

        # Rufe zusätzliche Informationen aus rezept_add ab.
        print("-------------------------")
        print("Hinweise zur Zubereitung: ")
        print("-------------------------")
        query_addinf = sql_addinf + unicode(rezept_id)
        query_addinf = query_addinf.encode('utf-8')
        cursor.execute(query_addinf)
        add_inf = cursor.fetchone()
        if add_inf == None:
            print("Keine Informationen vorhanden!")
            exit()
        add_inf = list(add_inf)
        if add_inf[0] != None:
            print(u'Ofeneinstellung: ' + add_inf[0])
            print(u'Temperatur:      ' + unicode(add_inf[1]))
            print(u'Backform:        ' + add_inf[2])
        print(u'Zubereitungsschritte:')
        for i1 in range(3,9):
            if add_inf[i1] != None:
                print(unicode(i1-2) + u'. ' + add_inf[i1])




finally:
    c.mysql_connect().close()

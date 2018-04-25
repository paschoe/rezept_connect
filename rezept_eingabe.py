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
        new_rezept = raw_input("Name des Rezepts: ")
        new_rezept = new_rezept.decode("utf-8")
        new_rezept_typ = raw_input("Typ des Rezepts: ")
        new_rezept_typ = new_rezept_typ.decode("utf-8")
        new_rezept_subtyp = raw_input("Subtyp des Rezepts: ")
        if new_rezept_subtyp == '':
            new_rezept_subtyp = u'NULL'
        else:
            new_rezept_subtyp = new_rezept_subtyp.decode("utf-8")
            new_rezept_subtyp = u'"' + new_rezept_subtyp + u'"'

        sql_new_rezept = u'INSERT INTO rezept_main(name,typ,subtyp) VALUES ("' + new_rezept +u'","' + new_rezept_typ\
                         + u'",' + new_rezept_subtyp+ u')'


        cursor.execute(sql_new_rezept)

        data_new_zutat =[]
        zutat = []
        menge = []
        einheit = []
        new_zutat = "dummy"
        while new_zutat != "":
            new_zutat = raw_input("Eingabe der Zutat: ")
            if new_zutat == '':
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
                einheit.append(u'"' + new_einheit.decode("utf-8") + u'"')
            else:
                einheit.append(u'NULL')

            if (new_zutat not in z and new_zutat != unicode("ende")):
                data_new_zutat.append(new_zutat)
            print "........."

## Ergänze rezeptdb.zutaten
        print("======================")
        print("Vorhandene Zutatstypen")
        cursor.execute(sql_get_typen)
        exist_typ = cursor.fetchall()
        print(exist_typ)
        print("----------------------")
        data_new_typ =[]
        for j in range(0,len(data_new_zutat)):
            d = raw_input("Definiere den Typ der neuen Zutat " + data_new_zutat[j] +": ")
            if d == "":
                d = u'NULL'
            else:
                d = '"'+d+'"'
                d = d.decode("utf-8")
            data_new_typ.append(d)

        data_new_zutat_ready = []
        for k in range(0,len(data_new_zutat)):
            data_new_zutat_ready.append(u'("'+data_new_zutat[k]+u'",'+data_new_typ[k]+u')')
        if len(data_new_zutat_ready)>0:
            sql_new_zutaten = u'INSERT INTO zutaten(zutat,typ) VALUES ' + u','.join(data_new_zutat_ready)
            print sql_new_zutaten
            cursor.execute(sql_new_zutaten)
        c.conn.commit()

## Befülle rezeptdb.zutaten_menge
        sql_get_newrezeptid = u'SELECT rezept_id FROM rezept_main WHERE name = "' + new_rezept + u'"'
        cursor.execute(sql_get_newrezeptid)
        new_id = cursor.fetchone()[0]
        data_menge_ready = []
        for m in range(0,len(zutat)):
            if menge[m] is None:
                menge_temp = u'NULL'
            else:
                menge_temp = unicode(menge[m])
            data_menge_ready.append(u'('+unicode(new_id) + u',"'+zutat[m] + u'",' + menge_temp +u','+einheit[m] + u')')
        sql_new_zutaten_menge = u'INSERT INTO zutaten_menge(rezept_ID, zutat, menge, einheit) ' \
                                u'VALUES ' + u','.join(data_menge_ready)
        cursor.execute(sql_new_zutaten_menge)
        c.conn.commit()

finally:
    c.conn.close()
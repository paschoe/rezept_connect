#!/usr/bin/env python
# -*- coding: utf-8 -*-

print(u'Wähle das zu ergänzende Rezept aus:')

import get_existing as g
id = int(g.rezept_id)
import connector as con

try:
    with con.conn.cursor() as cursor:
        sql_check_existence = "SELECT rezept_id FROM rezept_add"
        cursor.execute(sql_check_existence)
        existent_id = []
        for row in cursor:
            existent_id.append(row[0])
        if id in existent_id:
            print(u'Informationen bereits vorhanden, keine Eingabe notwendig.')
            exit()
        else:
            print(u'Weitere Informationen können im folgenden eingegeben werden. Falls keine Eingabe erwünscht, ENTER'
                  u'betätigen.')

            n_beschreibung = raw_input("Beschreibung des Rezepts: ")
            if n_beschreibung != "":
                n_beschreibung = u'"' + n_beschreibung.decode("utf-8") + u'"'
            else:
                n_beschreibung = u'NULL'

            n_dauer = raw_input("Dauer in Minuten: ")
            if n_dauer == "":
                n_dauer = u'NULL'
            else:
                n_dauer=unicode(n_dauer)

            n_portionen = raw_input("Anzahl der Portionen: ")
            if n_dauer == "":
                n_dauer = u'NULL'
            else:
                n_dauer = unicode(n_dauer)


            print("-----------------------")
            print("Es stehen 6 Zubereitungsschritte zur Verfügung: ")
            n_zub=[]
            for i in range(0,6):
                t_zub = raw_input("Schritt" + str(i+1) + ": ")
                if t_zub != "":
                    n_zub.append(u'"' + t_zub.decode("utf-8") + u'"')
                else:
                    n_zub.append(u'NULL')

            q_back = raw_input("Wird der Backofen benötigt? Antwort mit j/n. ")
            if q_back == "j":

                n_ofeneinstellung = raw_input("Ofeneinstellung: ")
                if n_ofeneinstellung != "":
                    n_ofeneinstellung=u'"' + n_ofeneinstellung.decode("utf-8") + u'"'
                else:
                    n_ofeneinstellung=u'NULL'

                n_temperatur = raw_input("Temperatur in C: ")
                if n_temperatur == "":
                    n_temperatur=u'NULL'
                else:
                    n_temperatur = unicode(n_temperatur)

                n_backform = raw_input("Backform: ")
                if n_backform != "":
                    n_backform=u'"' + n_backform.decode("utf-8") + u'"'
                else:
                    n_backform=u'NULL'
            else:
                n_ofeneinstellung = u'NULL'
                n_temperatur = u'NULL'
                n_backform = u'NULL'
            sql_input_base = u'INSERT INTO rezept_add(rezept_id, beschreibung, temperatur, ofeneinstellung, portionen, ' \
                             u'zub1, zub2, zub3, zub4, zub5, zub6, Backform, dauer) VALUES ('
            sql_values = (unicode(id) + u',' + n_beschreibung + u',' + n_temperatur + u',' + n_ofeneinstellung + u','
                          + n_portionen + u',' + u','.join(n_zub) + u',' + n_backform + u',' + n_dauer +u')')
            sql_ready = sql_input_base + sql_values
            cursor.execute(sql_ready)
            con.conn.commit()

finally:
    con.conn.close()

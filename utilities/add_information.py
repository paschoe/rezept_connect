#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utilities import db_tools as db
from utilities import input_tools as it


def fun():
    print(u'Wähle das zu ergänzende Rezept aus:')
    rezept_id = int(db.get_existing()[0])

    try:
        with db.mysql_connect().cursor() as cursor:
            sql_check_existence = "SELECT rezept_id FROM rezept_add"
            cursor.execute(sql_check_existence)
            existent_id = []
            for row in cursor:
                existent_id.append(row[0])
            if rezept_id in existent_id:
                print(u'Informationen bereits vorhanden, keine Eingabe notwendig.')
            else:
                print(
                    u'Weitere Informationen können im folgenden eingegeben werden. Falls keine Eingabe erwünscht,'
                    u' ENTER betätigen.')

                n_beschreibung = it.str_input("Beschreibung des Rezepts: ")
                n_dauer = it.int_input("Dauer in Minuten: ")
                n_portionen = it.int_input("Anzahl der Portionen: ")

                print("-----------------------")
                print("Es stehen 6 Zubereitungsschritte zur Verfügung: ")
                n_zub = []
                for i in range(0, 6):
                    n_zub.append(it.str_input("Schritt" + str(i + 1) + ": "))

                q_back = raw_input("Wird der Backofen benötigt? Antwort mit j/n. ")
                if q_back == "j":
                    n_ofeneinstellung = it.str_input("Ofeneinstellung: ")
                    n_temperatur = it.int_input("Temperatur in C: ")
                    n_backform = it.str_input("Backform: ")
                else:
                    n_ofeneinstellung = u'NULL'
                    n_temperatur = u'NULL'
                    n_backform = u'NULL'

                sql = u'INSERT INTO rezept_add(rezept_id, beschreibung, temperatur, ofeneinstellung, ' \
                      u'portionen, zub1, zub2, zub3, zub4, zub5, zub6, Backform, dauer) VALUES (' + \
                      unicode(rezept_id) + u',' + n_beschreibung + u',' + n_temperatur + u',' + n_ofeneinstellung + \
                      u',' + n_portionen + u',' + u','.join(n_zub) + u',' + n_backform + u',' + n_dauer + u')'
                cursor.execute(sql)
                db.mysql_connect().commit()

    finally:
        db.mysql_connect().close()

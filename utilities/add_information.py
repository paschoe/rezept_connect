# -*- coding: UTF-8 -*-
from utilities import db_tools as db
from utilities import input_tools as it
import pymysql


def fun(use_input, rezept_id):
    try:
        if use_input is False:
            print(u'Wähle das zu ergänzende Rezept aus:')
            rezept_id = unicode(int(db.get_rezept_list()[0]))
        existence = db.check_existence_rezept_add(rezept_id)
        if existence is True:
            print(u'Informationen bereits vorhanden, keine Eingabe notwendig.')
        else:
            print(u'Weitere Informationen können im folgenden eingegeben werden. Falls keine Eingabe erwünscht, '
                  u'ENTER betätigen.')

            n_beschreibung = it.str_input("Beschreibung des Rezepts: ")
            n_dauer = it.int_input("Dauer in Minuten: ")
            n_portionen = it.int_input("Anzahl der Portionen: ")

            print("-----------------------")
            print("Es stehen 6 Zubereitungsschritte zur Verfügung: ")
            n_zub = []
            for i in range(0, 6):
                n_zub.append(it.str_input("Schritt " + str(i + 1) + ": "))

            q_back = raw_input("Wird der Backofen benötigt? Antwort mit j/n. ")
            if q_back == "j":
                n_ofeneinstellung = it.str_input("Ofeneinstellung: ")
                n_temperatur = it.int_input("Temperatur in C: ")
                n_backform = it.str_input("Backform: ")
            else:
                n_ofeneinstellung = u'NULL'
                n_temperatur = u'NULL'
                n_backform = u'NULL'

            db.add_rezept_add_information(rezept_id, n_beschreibung, n_temperatur, n_ofeneinstellung, n_portionen,
                                          n_zub, n_backform, n_dauer, commit=True)

    except pymysql.DataError:
        print("Eine fehlerhafte Eingabe liegt vor. Eingabe wird zurückgesetzt und neugestartet.")
        fun(True, rezept_id)

    finally:
        db.mysql_connect().close()

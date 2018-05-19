# -*- coding: UTF-8 -*-

from utilities import db_tools as db
from utilities import input_tools as it
import pymysql


def fun():
    try:
        # Befüllen der rezeptdb.rezept_main
        rezept_name = it.str_input("Name des Rezepts: ")
        rezept_typ = it.str_input("Typ des Rezepts: ")
        rezept_subtyp = it.str_input("Subtyp des Rezepts: ")
        db.add_rezept_main(rezept_name, rezept_typ, rezept_subtyp, commit=False)

        # Eingabe der Zutaten, Aufnahme der Daten für rezeptdb.zutaten_menge
        zutaten = []
        mengen = []
        einheiten = []
        new_zutat = "dummy"
        unknown_zutat = []
        exist_zutaten = db.get_zutaten_list()
        while new_zutat != "":
            new_zutat = it.str_input("Eingabe der Zutat: ")
            if new_zutat == u'NULL':
                break
            zutaten.append(new_zutat)
            mengen.append(it.int_input("Eingabe der Menge ohne Einheit: "))
            einheiten.append(it.str_input("Eingabe der Einheit: "))
            if new_zutat.replace(u'"', u'') not in exist_zutaten:
                unknown_zutat.append(new_zutat)
            print "......................................."

        # Ergänze rezeptdb.zutaten falls Zutat unbekannt
        if len(unknown_zutat) > 0:
            print("======================")
            db.get_zutaten_typen_list()
            print("----------------------")
            new_type = []
            for j in range(0, len(unknown_zutat)):
                new_type.append(it.str_input("Definiere den Typ der neuen Zutat " + unknown_zutat[j] + ": "))
            db.add_zutaten(unknown_zutat, new_type, commit=True)

        # Befülle rezeptdb.zutaten_menge
        rezept_id = db.add_rezept_zutaten(rezept_name, zutaten, mengen, einheiten, commit=True)
        return rezept_id

    except pymysql.DataError:
        print("Eine fehlerhafte Eingabe liegt vor. Eingabe wird zurückgesetzt und neugestartet.")
        fun()

    finally:
        db.mysql_connect().close()

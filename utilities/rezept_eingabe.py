#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utilities import db_connect as db
from utilities import input_tools as it


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
        i = 0
        exist_zutaten = db.get_zutaten_list()
        while new_zutat != "":
            new_zutat = it.str_input("Eingabe der Zutat: ")
            if new_zutat == u'""':
                break
            zutaten.append(new_zutat)
            mengen.append(it.int_input("Eingabe der Menge ohne Einheit: "))
            einheiten.append(it.str_input("Eingabe der Einheit: "))
            if new_zutat not in exist_zutaten:
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
            db.add_zutaten(unknown_zutat,new_type,commit=True)



        # Befülle rezeptdb.zutaten_menge
        sql_get_newrezeptid = u'SELECT rezept_id FROM rezept_main WHERE name = "' + new_rezept + u'"'
        cursor.execute(sql_get_newrezeptid)
        new_id = cursor.fetchone()[0]
        data_menge_ready = []
        for m in range(0, len(zutat)):
            if menge[m] is None:
                menge_temp = u'NULL'
            else:
                menge_temp = unicode(menge[m])
            data_menge_ready.append(
                u'(' + unicode(new_id) + u',"' + zutat[m] + u'",' + menge_temp + u',' + einheit[m] +
                u')')
        sql_new_zutaten_menge = u'INSERT INTO zutaten_menge(rezept_ID, zutat, menge, einheit) ' \
                                u'VALUES ' + u','.join(data_menge_ready)
        cursor.execute(sql_new_zutaten_menge)
        db.mysql_connect().commit()

    finally:
        db.mysql_connect().close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from utilities import db_connect as db
from utilities import output_tools as o


def fun():
    try:
        # Extrahiere Daten  über Zutaten und Zubereitung aus der Datenbank
        rezept_id, rezept_name, rezepte = db.get_rezept_list()
        zutaten, add_inf = db.get_rezept(rezept_id)
        print(u"Zutaten für " + rezept_name + ":")
        print(u"------------------------------------------------------------------")
        disp_zutat = []
        for j in range(0, len(zutaten)):
            if zutaten[j][0] is not None:
                menge = unicode(zutaten[j][0])
            else:
                menge = unicode("")
            if zutaten[j][1] is not None:
                einheit = zutaten[j][1]
            else:
                einheit = unicode("")
            name = zutaten[j][2]
            a = unicode(menge + einheit + " " + name)
            disp_zutat.append(a)
            print(disp_zutat[j])

        # Rufe zusätzliche Informationen aus rezept_add ab.
        print(u"------------------------------------------------------------------")
        print("Hinweise zur Zubereitung: ")
        print(u"------------------------------------------------------------------")
        if add_inf is None:
            print("Keine Informationen vorhanden!")
        else:
            add_inf = list(add_inf)
            if add_inf[0] is not None:
                o.print_if_not_none(u"Ofeneinstellung:", add_inf[0])
                o.print_if_not_none(u"Temperatur     :", add_inf[1])
                o.print_if_not_none(u"Backform       :", add_inf[2])
            print(u'Zubereitungsschritte:')
            for i1 in range(3, 9):
                o.print_if_not_none(unicode(i1 - 2) + u".", add_inf[i1])

    except:
        print(u"Ups! Da lief etwas schief! Neustart eingeleitet")
        time.sleep(2)
        fun()

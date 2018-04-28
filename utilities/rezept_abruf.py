#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from utilities import connector as c
from utilities import get_existing as g
from utilities import output_tools as o


def fun():
    sql_zutaten = u"SELECT m.menge, m.einheit, m.zutat FROM zutaten_menge AS m JOIN rezept_main AS r " \
                  u"USING(rezept_ID) WHERE r.rezept_id="
    sql_addinf = u'SELECT a.ofeneinstellung,a.temperatur,a.Backform,a.zub1,a.zub2,a.zub3,a.zub4,a.zub5,a.zub6 ' \
                 u'FROM rezept_add AS a JOIN rezept_main AS r USING(rezept_ID) WHERE r.rezept_id='

    rezept_id, rezepte = g.get_existing()

    try:
        with c.mysql_connect().cursor() as cursor:

            query = sql_zutaten + unicode(rezept_id)
            query = query.encode('utf-8')
            cursor.execute(query)
            zutaten = (cursor.fetchall())
            for p in range(0, len(rezepte)):
                if int(rezepte[p][0]) == int(rezept_id):
                    rezept_name = unicode(rezepte[p][1])

            print("Zutaten fuer " + rezept_name + ":")
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
            query_addinf = sql_addinf + unicode(rezept_id)
            query_addinf = query_addinf.encode('utf-8')
            cursor.execute(query_addinf)
            add_inf = cursor.fetchone()
            if add_inf is None:
                print("Keine Informationen vorhanden!")
            else:
                add_inf = list(add_inf)
                if add_inf[0] is not None:
                    o.print_if_not_none(u"Ofeneinstellung:",add_inf[0])
                    o.print_if_not_none(u"Temperatur     :",add_inf[1])
                    o.print_if_not_none(u"Backform       :",add_inf[2])
                print(u'Zubereitungsschritte:')
                for i1 in range(3, 9):
                    o.print_if_not_none(unicode(i1 - 2) + u".",add_inf[i1])

    except:
        print(u"Irgendetwas lief schief. Neustart eingeleitet")
        time.sleep(2)
        fun()

    finally:
        c.mysql_connect().close()

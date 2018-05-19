# coding=utf-8
from utilities import add_information
from utilities import rezept_abruf
from utilities import rezept_eingabe
from utilities import db_tools as db


def main():
    print(u"rezept_connect")
    print(u"==================================================================")
    print(u"Wählen sie die gewünschte Aufgabe:")
    print(u"1. Abruf eines existierenden Rezepts")
    print(u"2. Eingabe eines neuen Rezepts.")
    print(u"3. Ergänzung eines existierenden Rezepts mit Zubereitungsschritten.")
    user_choice = raw_input(u"Geben Sie die gewünschte Zahl ein und bestätigen Sie mit Enter: ")
    print(u"==================================================================")
    print(u"")
    if user_choice == "1":
        rezept_abruf.fun()
    elif user_choice == "2":
        rezept_id = rezept_eingabe.fun()
        user_addinf = raw_input(u"Möchten Sie Informationen zur Zubereitung hinzufügen (j/n)? ")
        if user_addinf == "j":
            add_information.fun(use_input=True, rezept_id=unicode(rezept_id))
    elif user_choice == "3":
            add_information.fun(use_input=False, rezept_id=u"")
    else:
        print(u"Keine gültige Eingabe! Versuchen Sie es erneut!")
        main()
    print(u"")
    user_restart = raw_input(u"Möchten Sie eine weitere Abfrage durchführen (j/n)? ")
    if user_restart == "j":
        print("")
        print("")
        main()
    db.mysql_connect().close()


if __name__ == "__main__":
    main()

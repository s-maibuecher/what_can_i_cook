als erstes venv installieren, oder sollte das besser alles über Docker ablaufen?

https://www.popsugar.co.uk/food/website-that-tells-you-what-to-cook-with-what-you-have-47116006?utm_medium=redirect&utm_campaign=US:DE&utm_source=www.google.de

rezepte habe ich unter c temp temp runtergeladen


lieber mongo db nehmen --> erstmal mongo installieren und versuchen die Rezepte einzuladen

Datenbank Modellierung: https://www.access-diva.com/dm15.html

############
hier weiter

siehe https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html

Container bauen:
docker-compose -f local.yml build --no-cache


Container zum Laufen bringen:
docker-compose -f local.yml up -d


pip dependencies checken mittels:
https://stackoverflow.com/a/49472328/2952486

johnnydep pymongo 


manage.py Befehle ausführe:
docker-compose -f local.yml run --rm django python manage.py migrate

Viele Infos, Logs, usw gibt dann auch im Docker Dashboard auszulesen


unter /backups ist ein Datenbank Backup mit dem Stand der frisch gezogenen Mongo Daten

## Bisheriges Vorgehen:

Rezepte über das alte Skript mittels http Befehlen gezogen
dann mit dem build_recipes-db.py Skript in eine Mongo Atlas DB geladen
für die Konfiguration von dem Python Interpreter bietet Pycharm die Möglichkeit an, die Python Venv aus dem Docker Container zu wählen


hier weiter:
[korrekt]wie adde ich pymongo? --> ich denke requirements ändern und dann nochmal ein docker-compose built machen
[moment mal] das sollte auch klappen: docker-compose run web pip install package_name (wobei ich gerade nicht weiß wofür web steht)
+ in requirements von hand eintragen. das logging von docker wäre auch ganz interessant, ob er dependencies installieren muss


debugging klappt noch nicht wie gewünscht. in den Docs nutzen die pdb. Ausserdem ist werkzeug?! installiert.

dann in eine extra python file die Funktion (in utils) schreiben, um rezepte aus mongo db zu holen, erst mal nur drei

diese dann in diese erstellte migration file reinladen und dann damit migrieren

dann ausbauen...

[hier weiter]: 
mongo zugangsdaten löschen -> geht das ohne weiteres? brauche glaube ich einen gastaccount bei mongo


manche zutaten haben einen stern am ende
unwichtige zutaten?
das zuerst rausfinden und falls ja noch ein Feld

dann alles neu und migration bauen

dann daten darstellen

hatte überlegt, das select Feld gemeinsam aus zutaten und Zutatengruppen zu füllen, aber ich glaube darauf kommt es eigentlich gar nicht an in einer Portfolio App


wie resette ich die Datenbank? Drop Table Befehl? Hier im Docker-compose oder Dockerfile nochmal die richtige Zeile laufen lassen?


wie lasse ich pylint oder flake8 laufen?

der pytest Befehl oben klappt, das kann ich mit dokumentieren 


todo nach dem compose build muss noch ein migrate what_can_i_cook erfolgen, aber das kann ja auch ins Dockerfile mit
aufgenommen werden


shipped=False
Wasser* Öl* Olivenöl* Butter* Salz* Pfeffer* Zucker* Essig* Milch* Ei* Mehl* Backpulver Rotweinessig Gemüsebrühe* Weißweinessig* heißes Wasser* Gemüsebrühpaste* Honig* Hühnerbrühe* (Oliven-)Öl* Balsamicoessig* Balsamico-Essig Meersalz Eier Garflüssigkeit Balsamico-Essig, hell Rinderbrühe* Senf Pfefferkörner Geflügelbrühe Brühe Weißwein Wasser (mit Kohlensäure) natives Olivenöl extra Apfelessig


Zutaten mit Stern markiert:
'Wasser* Öl* Olivenöl* Butter* Salz* Pfeffer* Zucker* Essig* Milch* Ei* Mehl* Gemüsebrühe* Weißweinessig* heißes Wasser* Gemüsebrühpaste* Honig* Hühnerbrühe* (Oliven-)Öl* Balsamicoessig* Rinderbrühe*'

als erstes venv installieren, oder sollte das besser alles über Docker ablaufen?

https://www.popsugar.co.uk/food/website-that-tells-you-what-to-cook-with-what-you-have-47116006?utm_medium=redirect&utm_campaign=US:DE&utm_source=www.google.de

rezepte habe ich unter c temp temp runtergeladen


lieber mongo db nehmen --> erstmal mongo installieren und versuchen die Rezepte einzuladen



############
hier weiter

siehe https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html

docker-compose -f local.yml build




und dann noch die richtigen pycharm einstellungen

https://joshuahunter.com/posts/using-cookiecutter-to-jumpstart-a-django-project-on-windows-with-pycharm/#final-pycharm-settings


## Bisheriges Vorgehen:

Rezepte über das alte Skript mittels http Befehlen gezogen
dann mit dem build_recipes-db.py Skript in eine Mongo Atlas DB geladen
für die Konfiguration von dem Python Interpreter bietet Pycharm die Möglichkeit an, die Python Venv aus dem Docker Container zu wählen

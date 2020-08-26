from django.db import migrations
from what_can_i_cook.utils.seed_database import main as seed_main


def seed_db_with_recipes(apps, schema_editor):
    seed_main()


class Migration(migrations.Migration):
    dependencies = [
        ('what_can_i_cook', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_db_with_recipes),
    ]

# Generated by Django 4.2.5 on 2023-09-13 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_rename_pretynum_prettynum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prettynum',
            old_name='num',
            new_name='mobile',
        ),
    ]

# Generated by Django 4.0.6 on 2023-07-29 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_detail_uno_detail_option_detail_optionid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='optionID',
            new_name='answer',
        ),
    ]

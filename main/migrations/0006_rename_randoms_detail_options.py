# Generated by Django 4.0.6 on 2023-07-29 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_detail_answer_alter_option_optionid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='randoms',
            new_name='options',
        ),
    ]

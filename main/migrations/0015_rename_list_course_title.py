# Generated by Django 4.2.3 on 2023-08-09 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_detail_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='list',
            new_name='title',
        ),
    ]

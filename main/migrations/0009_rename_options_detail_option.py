# Generated by Django 4.0.6 on 2023-07-29 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_course_alter_detail_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='options',
            new_name='option',
        ),
    ]

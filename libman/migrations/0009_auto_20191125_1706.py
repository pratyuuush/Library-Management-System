# Generated by Django 2.2.6 on 2019-11-25 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libman', '0008_auto_20191125_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='faculty_id',
            new_name='fac_id',
        ),
    ]
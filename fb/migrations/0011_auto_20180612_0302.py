# Generated by Django 2.0.6 on 2018-06-12 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0010_auto_20180612_0300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notifications',
            old_name='content',
            new_name='notif_content',
        ),
    ]

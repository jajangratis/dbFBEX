# Generated by Django 2.0.6 on 2018-06-11 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0004_auto_20180611_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

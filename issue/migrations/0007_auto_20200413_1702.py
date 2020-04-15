# Generated by Django 3.0.5 on 2020-04-13 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issue', '0006_auto_20200413_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='btissues',
            name='assigned_To',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='btissues',
            name='created_By',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
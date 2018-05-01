# Generated by Django 2.0.4 on 2018-04-29 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portalAutomotora', '0002_auto_20180429_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='marca',
        ),
        migrations.AddField(
            model_name='auto',
            name='modelo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='portalAutomotora.Modelo'),
            preserve_default=False,
        ),
    ]
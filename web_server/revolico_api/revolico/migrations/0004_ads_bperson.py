# Generated by Django 2.2.4 on 2019-08-09 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revolico', '0003_auto_20190809_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='bperson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='revolico.BPerson'),
        ),
    ]

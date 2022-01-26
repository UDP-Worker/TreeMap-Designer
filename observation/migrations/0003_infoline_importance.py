# Generated by Django 4.0.1 on 2022-01-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observation', '0002_infoline'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoline',
            name='importance',
            field=models.SmallIntegerField(choices=[(1, '紧急'), (2, '担忧'), (3, '重要'), (4, '普通')], default=1),
            preserve_default=False,
        ),
    ]
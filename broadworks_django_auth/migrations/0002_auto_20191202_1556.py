# Generated by Django 2.1 on 2019-12-02 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broadworks_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadworks',
            name='is_group',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='broadworks',
            name='is_serviceprovider',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='broadworks',
            name='is_system',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='broadworks',
            name='is_user',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0010_auto_20240321_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='network',
        ),
        migrations.AlterField(
            model_name='network',
            name='network',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='network',
            name='network_ABI',
            field=models.TextField(max_length=25500),
        ),
        migrations.AlterField(
            model_name='network',
            name='network_url',
            field=models.CharField(max_length=255),
        ),
    ]

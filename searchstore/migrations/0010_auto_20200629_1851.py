# Generated by Django 3.0.3 on 2020-06-29 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchstore', '0009_auto_20200627_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawleddata',
            name='Product_Tags',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='Container_Product_Tags_Path_Class',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='Container_Product_Tags_Path_Type',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

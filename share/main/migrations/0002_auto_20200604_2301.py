# Generated by Django 2.2.8 on 2020-06-04 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='commentinfo',
            table='comment_info',
        ),
        migrations.AlterModelTable(
            name='ruleuser',
            table='rule_user',
        ),
    ]
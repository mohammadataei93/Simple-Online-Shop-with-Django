# Generated by Django 3.2.12 on 2022-04-05 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20220405_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='activa',
            new_name='active',
        ),
    ]
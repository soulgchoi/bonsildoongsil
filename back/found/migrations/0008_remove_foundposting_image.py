# Generated by Django 3.0.5 on 2020-04-27 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('found', '0007_auto_20200426_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foundposting',
            name='image',
        ),
    ]
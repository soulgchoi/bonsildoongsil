# Generated by Django 3.0.5 on 2020-04-27 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0004_auto_20200427_0226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lostposting',
            options={'ordering': ('-lost_time',)},
        ),
    ]
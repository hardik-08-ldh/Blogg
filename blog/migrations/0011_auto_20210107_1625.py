# Generated by Django 3.1.2 on 2021-01-07 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-date_added',)},
        ),
    ]

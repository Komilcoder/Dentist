# Generated by Django 2.2 on 2020-07-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_delete_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(null=True),
        ),
    ]

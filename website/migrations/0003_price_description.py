# Generated by Django 3.0.5 on 2020-07-09 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

# Generated by Django 3.0.5 on 2020-07-09 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_price_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='description',
        ),
        migrations.AddField(
            model_name='price',
            name='text',
            field=models.TextField(max_length=350, null=True),
        ),
    ]

# Generated by Django 2.2 on 2020-07-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20200719_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='picture',
            field=models.ImageField(upload_to='doctors'),
        ),
    ]

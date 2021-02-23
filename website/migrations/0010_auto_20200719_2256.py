# Generated by Django 2.2 on 2020-07-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200718_0505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='cost',
        ),
        migrations.AlterField(
            model_name='price',
            name='cost',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='cover',
            field=models.ImageField(null=True, upload_to='service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='service'),
        ),
    ]

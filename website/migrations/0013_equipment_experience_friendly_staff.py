# Generated by Django 2.2 on 2020-07-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_dentist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image1', models.ImageField(blank=True, null=True, upload_to='service')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='service')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image1', models.ImageField(blank=True, null=True, upload_to='service')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='service')),
            ],
        ),
        migrations.CreateModel(
            name='Friendly_staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.CharField(max_length=200, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='service')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='service')),
            ],
        ),
    ]

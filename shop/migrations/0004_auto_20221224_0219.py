# Generated by Django 3.2 on 2022-12-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20221222_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
    ]

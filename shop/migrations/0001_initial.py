# Generated by Django 3.2 on 2022-12-20 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрики',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
                ('rubric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.rubric', verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Маркет',
                'verbose_name_plural': 'Магазин',
                'ordering': ('-published',),
            },
        ),
    ]

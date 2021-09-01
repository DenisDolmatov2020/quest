# Generated by Django 2.2.10 on 2021-03-28 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_start', models.DateField(auto_now_add=True, verbose_name='Дата старта')),
                ('date_end', models.DateField(verbose_name='Дата окончания')),
            ],
        ),
    ]

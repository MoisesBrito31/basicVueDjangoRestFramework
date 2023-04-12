# Generated by Django 4.2 on 2023-04-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('description', models.CharField(max_length=500, verbose_name='Descrição')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

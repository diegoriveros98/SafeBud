# Generated by Django 3.2.16 on 2022-11-17 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostuladorPaseo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('nacimiento', models.DateField()),
                ('mensaje', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
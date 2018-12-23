# Generated by Django 2.0 on 2018-12-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('F', '女'), ('M', '男'), ('U', '保密')], max_length=8)),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
    ]

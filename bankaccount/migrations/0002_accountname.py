# Generated by Django 4.0.3 on 2022-03-02 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
            ],
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-26 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200326_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=255, unique=True, verbose_name='username'),
        ),
    ]
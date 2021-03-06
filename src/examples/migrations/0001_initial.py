# Generated by Django 3.0.4 on 2020-03-26 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_one', models.CharField(max_length=100)),
                ('field_two', models.CharField(max_length=100)),
                ('last_edit_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edited_example_ones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

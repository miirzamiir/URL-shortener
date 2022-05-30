# Generated by Django 4.0.4 on 2022-05-30 20:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('592eca37-2825-4d8e-8852-55839580ae2c'), primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

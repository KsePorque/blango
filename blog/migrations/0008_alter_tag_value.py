# Generated by Django 3.2.6 on 2022-09-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='value',
            field=models.TextField(max_length=100, unique=True),
        ),
    ]

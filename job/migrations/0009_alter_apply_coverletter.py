# Generated by Django 4.2.7 on 2023-11-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_apply_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='coverletter',
            field=models.TextField(max_length=500),
        ),
    ]

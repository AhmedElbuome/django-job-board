# Generated by Django 4.2.7 on 2023-11-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_category_job_description_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(null=True, upload_to='jobs/'),
        ),
    ]
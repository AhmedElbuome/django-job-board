# Generated by Django 4.2.7 on 2023-11-21 17:23

from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_alter_apply_coverletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='job.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to=job.models.image_upload),
        ),
    ]
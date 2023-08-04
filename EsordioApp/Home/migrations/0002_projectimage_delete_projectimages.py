# Generated by Django 4.2.3 on 2023-07-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projectimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prj_images', models.ImageField(upload_to='project_image')),
                ('prj_name', models.TextField(max_length=100)),
                ('prj_para', models.TextField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Projectimages',
        ),
    ]

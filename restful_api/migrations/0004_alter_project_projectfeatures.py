# Generated by Django 4.0.6 on 2022-08-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful_api', '0003_alter_project_projectfeatures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectfeatures',
            field=models.TextField(),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-16 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful_api', '0004_alter_project_projectfeatures'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tokenization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.BigIntegerField()),
                ('token', models.CharField(default='', max_length=255)),
                ('lastRoute', models.CharField(default='', max_length=100)),
                ('isDestroyed', models.CharField(default='', max_length=1)),
                ('isvalid', models.CharField(default='', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 4.1.6 on 2023-05-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_examples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeDataModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('stored_field', models.JSONField(blank=True)),
            ],
        ),
    ]

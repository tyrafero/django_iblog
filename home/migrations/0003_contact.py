# Generated by Django 4.1.7 on 2023-03-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_service_alter_feedback_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.TextField(blank=True)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]

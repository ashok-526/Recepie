# Generated by Django 4.2.3 on 2023-07-26 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0024_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['student_name'], 'verbose_name': 'student'},
        ),
    ]

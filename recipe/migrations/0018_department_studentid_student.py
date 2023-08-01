# Generated by Django 4.2.3 on 2023-07-26 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0017_recipe_recipe_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sutdent_name', models.CharField(max_length=20)),
                ('Student_email', models.EmailField(max_length=254, unique=True)),
                ('sutdent_age', models.IntegerField(default=18)),
                ('student_address', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart', to='recipe.department')),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentid', to='recipe.studentid')),
            ],
        ),
    ]

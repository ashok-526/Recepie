# Generated by Django 4.2.3 on 2023-07-22 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_alter_recipe_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]

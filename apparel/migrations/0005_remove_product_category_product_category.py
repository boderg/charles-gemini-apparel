# Generated by Django 5.0.4 on 2024-05-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0004_alter_category_friendly_name_alter_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='apparel.category'),
        ),
    ]
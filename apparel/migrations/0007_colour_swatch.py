# Generated by Django 5.0.4 on 2024-06-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apparel', '0006_colour_size_alter_product_category_product_colours_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='colour',
            name='swatch',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]

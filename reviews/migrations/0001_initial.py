# Generated by Django 3.2.12 on 2023-11-19 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=50)),
                ('average_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='product_photos/')),
            ],
        ),
    ]

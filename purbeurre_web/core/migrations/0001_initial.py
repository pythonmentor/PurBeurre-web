# Generated by Django 2.1.3 on 2018-12-19 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=50)),
                ('nutrition_grade', models.CharField(max_length=5)),
                ('image_nutrition_url', models.CharField(max_length=500)),
                ('image_small_product_url', models.CharField(max_length=500)),
                ('image_full_product_url', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=300)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Category')),
            ],
        ),
    ]

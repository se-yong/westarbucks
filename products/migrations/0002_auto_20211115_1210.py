# Generated by Django 3.2.9 on 2021-11-15 12:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy_drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.allergy')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kca', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sodium_mg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saturated_fat_g', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sugars_g', models.DecimalField(decimal_places=2, max_digits=10)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=10)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('size_ml', models.CharField(max_length=45)),
                ('size_fluid_ounce', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='description',
            field=models.TextField(default='hgjkl;'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drink',
            name='english_name',
            field=models.CharField(default=datetime.date(2021, 11, 15), max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drink',
            name='korean_name',
            field=models.CharField(default='dasf', max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.AddField(
            model_name='nutrition',
            name='drink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink'),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.size'),
        ),
        migrations.AddField(
            model_name='allergy_drink',
            name='drink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.drink'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimador', '0017_remove_pricevalue_cotizacion_pricevalue_cotizacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReusoSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(blank=True, max_length=255, null=True)),
                ('flow', models.FloatField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('cotizacion', models.ManyToManyField(blank=True, db_index=True, to='estimador.cotizacion')),
            ],
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='reuso_cotizacion',
            field=models.ManyToManyField(blank=True, related_name='reuso_cotizacion', to='estimador.reusosystem'),
        ),
        migrations.CreateModel(
            name='WasteWaterSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(blank=True, max_length=255, null=True)),
                ('flow', models.FloatField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('cotizacion', models.ManyToManyField(blank=True, db_index=True, to='estimador.cotizacion')),
            ],
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='waste_water_cotizacion',
            field=models.ManyToManyField(blank=True, related_name='waste_water_cotizacion', to='estimador.wastewatersystem'),
        ),
        migrations.CreateModel(
            name='WaterSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(blank=True, max_length=255, null=True)),
                ('flow', models.FloatField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('cotizacion', models.ManyToManyField(blank=True, db_index=True, to='estimador.cotizacion')),
            ],
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='water_cotizacion',
            field=models.ManyToManyField(blank=True, related_name='water_cotizacion', to='estimador.watersystem'),
        ),
        migrations.DeleteModel(
            name='PriceValue',
        ),
    ]
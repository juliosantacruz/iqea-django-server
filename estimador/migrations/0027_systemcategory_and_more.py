# Generated by Django 5.0.1 on 2024-03-01 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimador', '0026_preciorefpoint_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('water_cotizacion', 'Clean Water'), ('waste_water_cotizacion', 'Waste Water'), ('reuso_cotizacion', 'Reuso Water')])),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='preciosreferencia',
            name='system_categories',
        ),
        migrations.AlterField(
            model_name='preciorefpoint',
            name='currency',
            field=models.CharField(blank=True, choices=[('USD', 'usd'), ('MXN', 'mxn')], null=True),
        ),
        migrations.CreateModel(
            name='SystemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('osmosis', 'Osmosis Inversa'), ('suavisador', 'Suavisador'), ('filtracion', 'Filtracion'), ('pretratamiento', 'Pretratamiento'), ('lodosActivados', 'Lodos Activados'), ('bioFiltracion', 'BioFiltracion'), ('mbbr', 'MBBR'), ('osmosisReuso', 'Osmosis Reuso'), ('ultrafiltracion', 'Ultrafiltracion')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('system_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='system_category', to='estimador.systemcategory')),
            ],
        ),
        migrations.AlterField(
            model_name='preciosreferencia',
            name='system_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='system_type', to='estimador.systemtype'),
        ),
    ]

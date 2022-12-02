# Generated by Django 4.1.2 on 2022-12-02 17:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal_Line_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('serving_quantity', models.DecimalField(decimal_places=2, max_digits=4)),
                ('user', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=50)),
                ('sodium', models.FloatField(null=True)),
                ('potassium', models.FloatField(null=True)),
                ('phosophorus', models.FloatField(null=True)),
                ('protein', models.FloatField(null=True)),
                ('water', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'journal_line_item',
            },
        ),
    ]
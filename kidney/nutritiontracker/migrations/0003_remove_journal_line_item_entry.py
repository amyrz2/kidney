# Generated by Django 4.1.2 on 2022-12-02 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutritiontracker', '0002_alter_journal_line_item_phosophorus_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal_line_item',
            name='entry',
        ),
    ]

from django.db import models
from django.utils import timezone
# Create your models here.
#Probably removing this table, just log each entry individually with patient_id and date
class Journal_Line_Item(models.Model):
   entry_datetime = models.DateTimeField(default=timezone.now)
   serving_quantity = models.DecimalField(max_digits=4, decimal_places=2)
   user = models.CharField(max_length=50)
   item = models.CharField(max_length=50)
   sodium = models.FloatField(null=True)
   potassium = models.FloatField(null=True)
   phosophorus = models.FloatField(null=True)
   protein = models.FloatField(null=True)
   water = models.FloatField(null=True)
   class Meta:
       db_table = 'journal_line_item'
   def __str__(self):
       return f'{self.serving_quantity}'
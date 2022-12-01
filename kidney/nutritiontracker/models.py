from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
# Create your models here.
#Change your models (in models.py).
#Run python manage.py makemigrations to create migrations for those changes
#Run python manage.py migrate to apply those changes to the database.


class User(models.Model):
    user_first_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=100)
    user_password = models.CharField(max_length=20)
    user_phone = models.CharField(max_length=13, blank=True)
    user_gender = models.CharField(max_length=1) 

    @property
    def user_full_name(self):
        return '%s %s' % (self.user_first_name, self.user_last_name)
    
    class Meta:
        db_table = 'user'
    
    def __str__(self):
        return f'{self.user_full_name}-{self.user_email}-{self.user_password}-{self.user_phone}-{self.user_gender}'    

class Doctor(User):
    doctor_specialization = models.CharField(max_length=20, blank=True)
    doctor_license = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'doctor'

    def __str__(self):
        return f'{self.doctor_specialization}-{self.doctor_license}'


class Accountability_Partner(User):
    relationship = models.CharField(max_length=20)

    class Meta:
        db_table = 'accountability_partner'

    def __str__(self):
        return f'{self.relationship}'

class Patient(User):
    patient_DOB = models.DateField(help_text= "Date of birthday")
    patient_race = models.CharField(max_length=20)
    doctor_id = models.ManyToManyField(Doctor, blank=True)
    partner_id = models.ManyToManyField(Accountability_Partner, blank=True)

    class Meta:
        db_table = 'patient'

    def __str__(self):
        return f'{self.patient_DOB}-{self.patient_race}'

class Journal_Entry(models.Model):
    entry_datetime = models.DateTimeField(default=timezone.now)
    patient_id = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'journal_entry'
    
    def __str__(self):
        return f'{self.entry_datetime}'
    
class Journal_Entry_Type(models.Model):
    type_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'journal_entry_type'
    
    def __str__(self):
        return f'{self.type_name}'

class Measurement_Type(models.Model):
    unit_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'measurement_type'

    def __str__(self):
        return f'{self.unit_name}'

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    serving_size = models.DecimalField(max_digits=8,decimal_places=2)
    measurement_type_id = models.ForeignKey(Measurement_Type, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'item'
    
    def __str__(self):
        return f'{self.item_name}-{self.serving_size}'

class Journal_Line_Item(models.Model):
    serving_quantity = models.DecimalField(max_digits=4, decimal_places=2)
    entry_id = models.ForeignKey(Journal_Entry, on_delete=models.DO_NOTHING)
    type_id = models.ForeignKey(Journal_Entry_Type, on_delete=models.DO_NOTHING)
    item_id = models.ForeignKey(Item, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'journal_line_item'

    def __str__(self):
        return f'{self.serving_quantity}'

class Modify_Info_Entry(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    patient_id = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'modify_info_entry'

    def __str__(self):
        return f'{self.timestamp}'

class Weight(models.Model):
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    modify_id = models.ForeignKey(Modify_Info_Entry, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'weight'

    def __str__(self):
        return f'{self.weight}'

class Height(models.Model):
    feet = models.IntegerField()
    inches = models.IntegerField()
    modify_id = models.ForeignKey(Modify_Info_Entry, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'height'

    def __str__(self):
        return f'{self.height}'

class Morbidity(models.Model):
    morbidity_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'morbidity'

    def __str__(self):
        return f'{self.morbidity_name}'

class Stage(models.Model):
    stage_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'stage'

    def __str__(self):
        return f'{self.stage_name}'

class Morbidity_Stage(models.Model):
    morbidity_id = models.ForeignKey(Morbidity, on_delete=models.DO_NOTHING, blank=True)
    stage_id = models.ForeignKey(Stage, on_delete=models.DO_NOTHING, blank=True)

    class Meta:
        db_table = 'morbidity_stage'

class Diagnosis(models.Model):
    modify_id = models.ForeignKey(Modify_Info_Entry, on_delete=models.DO_NOTHING, primary_key=True)
    morbidity_stage_id = models.ForeignKey(Morbidity_Stage, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'diagnosis'



    










   

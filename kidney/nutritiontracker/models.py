from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
# Create your models here.
#Change your models (in models.py).
#Run python manage.py makemigrations to create migrations for those changes
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )
        return self._create_user(email, password, **extra_fields)
class User(AbstractUser):
    email = models.EmailField("email address", unique=True)
    phone = models.IntegerField(blank=True)
    gender = models.CharField(max_length=10)
    birthday = models.DateField()
    USERNAME_FIELD = "email" # make the user log in with the email
    REQUIRED_FIELDS = ["username"]
    objects = CustomUserManager()
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
   user_gender = models.CharField(max_length=1)
   doctor = models.ManyToManyField(Doctor, blank=True)
   partner = models.ManyToManyField(Accountability_Partner, blank=True)
   class Meta:
       db_table = 'patient'
   def __str__(self):
       return f'{self.patient_DOB}-{self.patient_race}'
class Journal_Entry(models.Model):
   entry_datetime = models.DateTimeField(default=timezone.now)
   patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
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
   sodium = models.FloatField()
   potassium = models.FloatField()
   phosophorus = models.FloatField()
   protein = models.FloatField()
   water = models.FloatField()
   measurement_type = models.ForeignKey(Measurement_Type, on_delete=models.DO_NOTHING)
   class Meta:
       db_table = 'item'
   def __str__(self):
       return f'{self.item_name}-{self.serving_size}'
class Journal_Line_Item(models.Model):
   serving_quantity = models.DecimalField(max_digits=4, decimal_places=2)
   entry = models.ForeignKey(Journal_Entry, on_delete=models.DO_NOTHING)
   type = models.ForeignKey(Journal_Entry_Type, on_delete=models.DO_NOTHING)
   item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
   class Meta:
       db_table = 'journal_line_item'
   def __str__(self):
       return f'{self.serving_quantity}'
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
   morbidity = models.ForeignKey(Morbidity, on_delete=models.DO_NOTHING, blank=True)
   stage = models.ForeignKey(Stage, on_delete=models.DO_NOTHING, blank=True)
   class Meta:
       db_table = 'morbidity_stage'
class Modify_Info_Entry(models.Model):
   timestamp = models.DateTimeField(default=timezone.now)
   patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
   morbidity_stage = models.ManyToManyField(Morbidity_Stage, blank=True)
   class Meta:
       db_table = 'modify_info_entry'
   def __str__(self):
       return f'{self.timestamp}'
class Weight(models.Model):
   weight = models.DecimalField(max_digits=4, decimal_places=2)
   modify = models.ForeignKey(Modify_Info_Entry, on_delete=models.DO_NOTHING)
   class Meta:
       db_table = 'weight'
   def __str__(self):
       return f'{self.weight}'
class Height(models.Model):
   feet = models.IntegerField()
   inches = models.IntegerField()
   modify = models.ForeignKey(Modify_Info_Entry, on_delete=models.DO_NOTHING)
   class Meta:
       db_table = 'height'
   def __str__(self):
        return f'{self.feet}-{self.inches}'
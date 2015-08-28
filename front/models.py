from django.db import models
import datetime 
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from audit_log.models import AuthStampedModel
from audit_log.models.fields import LastUserField, LastSessionKeyField
from audit_log.models.fields import CreatingUserField, CreatingSessionKeyField

# Create your models here.
class Barcode(models.Model):
    name = models.CharField(max_length=255, unique=True)
    updated = models.DateTimeField('Updated date', editable=False, default=datetime.datetime.now)
    created = models.DateTimeField('Created date', editable=False, default=datetime.datetime.now)
    modified_by = LastUserField() 
    modified_session = LastSessionKeyField()

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    updated = models.DateTimeField('Updated date', editable=False, default=datetime.datetime.now)
    created = models.DateTimeField('Created date', editable=False, default=datetime.datetime.now)
    modified_by = LastUserField() 
    modified_session = LastSessionKeyField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.EmailField(max_length=70, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    updated = models.DateTimeField('Updated date', editable=False, default=datetime.datetime.now)
    created = models.DateTimeField('Created date', editable=False, default=datetime.datetime.now)
    modified_by = LastUserField() 
    modified_session = LastSessionKeyField()

    def __str__(self):
        return self.name
   
'''   
class Plates(models.Model):
    position = models.CharField(max_length=255, unique=True)
    number = models.CharField(max_length=255)
    delivery_number = models.CharField(max_length=255)
    updated = models.DateTimeField('Updated date', editable=False, default=datetime.datetime.now)
    created = models.DateTimeField('Created date', editable=False, default=datetime.datetime.now)
    modified_by = LastUserField() 
    modified_session = LastSessionKeyField()

    class Meta:
        verbose_name_plural="Plates"

    def __str__(self):
        return self.position
'''

class Species(models.Model):
    name = models.CharField(max_length=255, unique=True)
    updated = models.DateTimeField('Updated date', editable=False, default=datetime.datetime.now)
    created = models.DateTimeField('Created date', editable=False, default=datetime.datetime.now)
    modified_by = LastUserField() 
    modified_session = LastSessionKeyField()

    class Meta:
        verbose_name_plural="Species"

    def __str__(self):
        return self.name

class Storage(models.Model):
    TYPE = (
     ('1', 'Shelf'),
     ('2', 'Rack'),
    )
    RACKNO = [(i,i+1) for i in range(40)]
    name = models.CharField(max_length=255, unique=False)
    type = models.CharField(max_length=255, choices=TYPE)
    rackno = models.PositiveIntegerField(choices=RACKNO)
    updated = models.DateTimeField('Updated date', editable=False, default=datetime.datetime.now)
    created = models.DateTimeField('Created date', editable=False, default=datetime.datetime.now)
    modified_by = LastUserField() 
    modified_session = LastSessionKeyField()

    class Meta:
        verbose_name_plural="Storage"

    def __str__(self):
        return self.name

class Status(models.Model):
    current = models.CharField(max_length=255, unique=True)
    updated = models.DateTimeField('Updated date', editable=False, default=datetime.datetime.now)
    created = models.DateTimeField('Created date', editable=False, default=datetime.datetime.now)
    modified_by = LastUserField() 
    modified_session = LastSessionKeyField()

    class Meta:
        verbose_name_plural="Status"

    def __str__(self):
        return self.current

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    list_per_page = models.IntegerField()

class Sampletype(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False, unique=True, default="Other")
    updated = models.DateTimeField('Updated date', editable=False, default=datetime.datetime.now)
    created = models.DateTimeField('Created date', editable=False, default=datetime.datetime.now)
    modified_by = LastUserField() 
    modified_session = LastSessionKeyField()
    class Meta:
        verbose_name_plural="Sampletype"

    def __str__(self):
        return self.name

class Sample(models.Model):
    barcode = models.ForeignKey(Barcode)
    project = models.ForeignKey(Project)
    customer = models.ForeignKey(Customer)
    species = models.ForeignKey(Species)
    status = models.ForeignKey(Status)
    storage = models.ForeignKey(Storage)
    sampletype = models.ForeignKey(Sampletype, default=1)
    plate_position = models.CharField(max_length=3, blank=False, null=False)
    customer_plate = models.CharField(max_length=50, blank=True)
    customer_sample = models.CharField(max_length=255, blank=True)
    concentration = models.CharField(max_length=10, blank=True, null=True)
    volume = models.CharField(max_length=10, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, default='')
    updated = models.DateTimeField('Updated date', editable=False, default=datetime.datetime.now)
    created = models.DateTimeField('Created date', editable=False, default=datetime.datetime.now)
    created_by = CreatingUserField(related_name = "created_categories")
    created_with_session_key = CreatingSessionKeyField()
    modified_by = LastUserField() 
    modified_session = LastSessionKeyField()

    class Meta:
        unique_together = ('barcode', 'plate_position',)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.updated = datetime.datetime.today()
        return super(Sample, self).save(*args, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def __str__(self):
        return self.plate_position


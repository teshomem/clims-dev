from django.contrib import admin
from django.contrib.auth.models import User
from front.models import Sample, Project, Customer, Barcode, Species, Status, Storage, Sampletype
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from import_export import resources, fields, widgets

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'name', 'updated', 'modified_by')
    list_editable = ('description', 'name')
    search_fields = ['name']
admin.site.register(Project, ProjectAdmin)

def copy_record(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
copy_record.short_description = "Duplicate selected record"

class CustomerAdmin(admin.ModelAdmin):
    actions = [copy_record] 
    list_display = ('id', 'name', 'project', 'contact', 'phone', 'email', 'updated', 'modified_by')
    list_editable = ( 'project', 'contact', 'phone', 'email')
    search_fields = ['name']
#    save_as = True
#    save_on_top = True
admin.site.register(Customer, CustomerAdmin)

'''
class PlatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'position', 'number', 'delivery_number', 'updated', 'modified_by')
    list_filter = ['number']
    search_fields = ['number']
admin.site.register(Plates, PlatesAdmin)
'''

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','current', 'updated', 'modified_by')
    list_editable = ('current',)
    search_fields = ['current']
admin.site.register(Status, StatusAdmin)


class StorageAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'type', 'rackno', 'updated', 'modified_by')
    list_editable = ('name', 'type', 'rackno')
    search_fields = ['id', 'name', 'type']
admin.site.register(Storage, StorageAdmin)

class SampletypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updated', 'modified_by')
    list_editable = ('name',)
    search_fields = ['id', 'name']
admin.site.register(Sampletype, SampletypeAdmin)

class BarcodeResource(resources.ModelResource):
    class Meta:
        model = Barcode 
        fields = ('id', 'name')
#        value_overrides = ('name')

class BarcodeAdmin(ImportExportActionModelAdmin):
    resource_class = BarcodeResource
    search_fields = ('id', 'name')
    list_display = ('id', 'name')
    list_editable = ('name',)
    pass
admin.site.register(Barcode, BarcodeAdmin)


class SampleResource(resources.ModelResource):

    class Meta:
        model = Sample
        fields = ('id', 'barcode', 'barcode', 'barcode_id', 'project', 'customer', 'species', 'storage', 'sampletype', 'customer_plate', 'customer_sample', 'plate_position',  'concentration', 'volume', 'status', 'comment','modified_by')
        #value_overrides = ("barcode_id", "project_id", "customer", "species", "storage", "status", "sampletype")
        value_overrides = ("barcode_id", "project", "species", "storage", "status", "sampletype")

class SampleAdmin(ImportExportActionModelAdmin):
    resource_class = SampleResource
    search_fields = ('id', 'barcode__name', 'project__name', 'customer__name', 'species__name', 'storage__name', 'sampletype__name', 'customer_plate', 'customer_sample', 'plate_position',  'concentration', 'volume', 'status__current','comment')
    list_display = ('id', 'barcode', 'project', 'customer', 'species', 'storage', 'sampletype', 'customer_plate', 'customer_sample', 'plate_position',  'concentration', 'volume', 'status', 'comment','modified_by')
    list_editable = ('concentration', 'volume', 'status', 'comment')
    pass
admin.site.register(Sample, SampleAdmin)

class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updated', 'modified_by')
    search_fields = ['name']
    list_editable = ['name',]
admin.site.register(Species, SpeciesAdmin)

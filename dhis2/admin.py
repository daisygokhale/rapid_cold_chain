#Create your admin definitions here
from django.contrib import admin
from util.admin import RelatedFieldAdmin
from models import *


class FacilityAdmin(admin.ModelAdmin):
	pass
	
class EquitmentAdmin(admin.ModelAdmin):
	pass
	
class ContactAdmin(admin.ModelAdmin):
	pass
	
class ContactConnectionAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Facility,FacilityAdmin)
admin.site.register(OrganisationUnit,FacilityAdmin)
admin.site.register(Equitment,EquitmentAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(ContactConnection,ContactConnectionAdmin)


#Create your admin definitions here
from django.contrib import admin
from util.admin import RelatedFieldAdmin
from models import *



class ReportInline(admin.TabularInline):
	model = Report
	
	extra = 1

class MessageAdmin(RelatedFieldAdmin):
	
	list_display = ('created','message__text','message__connection','num_reports')
	
	readonly_fields = ('created','modified')
	
	inlines = (ReportInline,)

class ReportAdmin(RelatedFieldAdmin):
	
	list_display = ('created','commands','errors','has_error')


admin.site.register(SubmissionMessage,MessageAdmin)
admin.site.register(RegularMessage,MessageAdmin)
admin.site.register(Report,ReportAdmin)

	

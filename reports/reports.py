from django.db import models
import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from datetime import datetime
from xhtml2pdf import pisa as pisa

# Create your models here.
class Report(models.Model):
	"""docstring for Report"""
	# def __init__(self):

	def openPDF(self):
		data = 2
		district_name="Pune"
		curdate = datetime.now()
		template = get_template('pdf_report_base.html')
		context = Context({ 'data' : data,
							'district_name' : district_name,
							'date' : curdate })
		html  = template.render( context )
		
		# add in boolean for timestamp!
		filename = os.path.dirname(os.path.realpath(__file__)) + "/pdf-reports/testPDF.pdf"
		pdf = pisa.CreatePDF(
			src=html,
			dest=file(filename, "wb"))
		if not pdf.err:
			pisa.startViewer(filename)

	def generate_district_reportPDFtest(self, dest_file):
		district_name="Pune"
		curdate = datetime.now()
		template = get_template('pdf_report_base.html')
		context = Context({ 'data' : data,
							'district_name' : district_name,
							'date' : curdate })
		generate_reportPDF(self, "derp", dest_file, context, true)

	def generate_reportPDF(self, template_name, dest_file, context, timestamp=false):
		# add in case for district vs immunization unit
		html = template.render( context )
		
		# add in boolean for timestamp!
		if(timestamp) {
			filename = os.path.dirname(os.path.realpath(__file__)) + "/pdf-reports/testPDF" + datetime.now() + ".pdf"
		} else {
			filename = os.path.dirname(os.path.realpath(__file__)) + "/pdf-reports/testPDF.pdf"
		}
		filename.replace(" ", "_")
		pdf = pisa.CreatePDF(
			src=html,
			dest=file(filename, "wb"))
		if not pdf.err:
			pisa.startViewer(filename)

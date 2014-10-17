from django.core.management.base import BaseCommand, CommandError
import reports as report

class Command(BaseCommand):

	def handle(self, *args, **options):
		r = report.Report()
		r.openPDF()
		self.stdout.write("Wrote PDF.")
from django.core.management.base import BaseCommand

class Command(BaseCommand):    
  help = 'Загрузка продуктов'    
  def handle(self, *args, **options):        
    import os        
    os.system('python3.11 manage.py loaddata data.json')

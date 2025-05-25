from django.core.management.base import BaseCommand

class Command(BaseCommand):    
  help = 'Выгрузка продуктов'    
  def handle(self, *args, **options):        
    import os        
    os.system('python3 manage.py dumpdata users.StockBalance > data.json')

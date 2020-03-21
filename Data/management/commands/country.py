from django.core.management.base import BaseCommand
import requests
from coronaapi.models import CoronaAge, CoronaSex, CoronaComorbidity, Hackathon, Area, Total


# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         url = 'http://www.mocky.io/v2/5e767b012f0000710098609f'
#         r = requests.get(url)
#         titles = r.json()
#         print(titles)

#         for micro in titles['countries'] or []:
#             Area.objects.update_or_create(
#                 country=micro['country'],
#                 state=micro['states'],
#             )

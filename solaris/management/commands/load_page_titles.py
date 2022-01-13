from django.core.management.base import BaseCommand
from solaris.models import Page


class Command(BaseCommand):
    page_titles = {
        'partner_card': 'Карта партнера',
        'vacuum_oils': 'Вакуумные масла',
        'turbine_oils': 'Турбинные масла',
        'transmission_oils': 'Трансмиссионные масла',
        'special_liquids': 'Специальные жидкости',
        'ships_oils': 'Судовые масла',
        'price_list': 'Прайс-лист',
        'instrument_oils': 'Инструментальные масла',
        'engine_oils': 'Моторные масла',
        'industrial_oils': 'Индустриальные масла',
        'hydraulic_oils': 'Гидравлические масла',
        'compressor_oils': 'Компрессорные масла',
        'cable_and_transformer_oils': 'Кабельные и трансформаторные масла',
        'aviation_oils': 'Авиационные масла',
        'greases': 'Смазки',
    }

    def handle(self, *args, **options):
        pages = Page.objects.filter()
        for page in pages:
            if page.name in self.page_titles.keys():
                page.title = self.page_titles[page.name]
                page.save(0)

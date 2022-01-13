from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.db.models import Prefetch
from django.conf import settings
from .models import Page, Header, Text, List, Table, TableCell
import os


class IndexPageView(TemplateView):
    template_name = "solaris/index_page.html"


class SitePageView(TemplateView):
    template_name = "solaris/site_page.html"

    def prepare_tables_data(self, tables):
        data = []
        for idx, table in enumerate(tables):
            data.append([])

            for cell in table.cells.all():
                row = cell.row

                if len(data[idx]) <= table.rows:
                    data[idx].append([])

                data[idx][row].append(cell)

        return data

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if context['page_name'] == 'favicon.ico':
            print(settings.BASE_DIR)
            image_data = open(os.path.join(settings.BASE_DIR, 'static/imgs/favicon.ico'), 'rb').read()
            return HttpResponse(image_data)  # , mimetype="image/png"

        page = Page.objects.filter(name=context['page_name'])\
            .prefetch_related('headers')\
            .prefetch_related('text')\
            .prefetch_related('lists')\
            .prefetch_related(Prefetch(
                'tables', queryset=Table.objects.all()\
                .prefetch_related(Prefetch('cells', queryset=TableCell.objects.filter(spanned=False)))
            ))\
            .first()

        headers = list(page.headers.all())
        text = list(page.text.all())
        lists = list(page.lists.all())
        tables = self.prepare_tables_data(list(page.tables.all()))

        elements = headers + text + lists + tables

        def sort_func(x):
            if hasattr(x, 'page_index'):
                return x.page_index
            else:
                return x[0][0].table.page_index

        # elements.sort(key=lambda x: x.page_index)
        elements.sort(key=sort_func)

        data = []
        for elem in elements:
            if isinstance(elem, Header):
                data.append(('header', elem))
            elif isinstance(elem, Text):
                data.append(('text', elem))
            elif isinstance(elem, List):
                data.append(('list', elem))
            else:
                data.append(('table', elem))

        context['data'] = data
        context['page_title'] = page.title
        return self.render_to_response(context)

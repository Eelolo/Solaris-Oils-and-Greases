from django.core.management.base import BaseCommand
import json
from solaris.models import Page, Header, Text, List, Table, TableCell


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('solaris/management/commands/all_data/pages.json', 'r') as f:
            data = json.loads(f.read())

            for page in data:
                Page.objects.create(id=page['id'], name=page['name'])

        with open('solaris/management/commands/all_data/headers.json', 'r', encoding='utf_8_sig') as f:
            data = json.loads(f.read())

            for header in data:
                page = Page.objects.filter(id=header['page_id']).first()
                Header.objects.create(
                    id=header['id'], content=header['content'], page=page,
                    page_index=header['page_index'], tag=header['tag'],
                )

        with open('solaris/management/commands/all_data/text.json', 'r', encoding='utf_8_sig') as f:
            data = json.loads(f.read())

            for text in data:
                page = Page.objects.filter(id=text['page_id']).first()
                Text.objects.create(
                    id=text['id'], content=text['content'], page=page,
                    page_index=text['page_index'],
                )

        with open('solaris/management/commands/all_data/lists.json', 'r', encoding='utf_8_sig') as f:
            data = json.loads(f.read())

            for list in data:
                page = Page.objects.filter(id=list['page_id']).first()
                List.objects.create(
                    id=list['id'], content=json.loads(list['content']), page=page,
                    page_index=list['page_index'], label=list['label'], rows=list['rows']
                )

        with open('solaris/management/commands/all_data/tables.json', 'r', encoding='utf_8_sig') as f:
            data = json.loads(f.read())

            for table in data:
                page = Page.objects.filter(id=table['page_id']).first()
                new_table = Table.objects.create(
                    id=table['id'], page=page, page_index=table['page_index'],
                    columns=table['columns'], rows=table['rows']
                )
                content = json.loads(table['content'])

                spanned = []
                for row in range(table['rows']):
                    for col in range(table['columns']):
                        if f'{row}-{col}' in spanned:
                            TableCell.objects.create(
                                content='', row_span=1, col_span=1, spanned=True,
                                thead=False, table=new_table, row=row, column=col
                            )
                            continue

                        value = content[row][0]['value']
                        colspan = content[row][0].get('colspan', 1)
                        rowspan = content[row][0].get('rowspan', 1)

                        TableCell.objects.create(
                            content=value, row_span=rowspan, col_span=colspan, spanned=False,
                            thead=False, table=new_table, row=row, column=col
                        )

                        if colspan and colspan != 1:
                            for span in range(1, int(colspan)):
                                spanned.append(f'{row}-{col + span}')

                        if rowspan and rowspan != 1:
                            for span in range(1, int(rowspan)):
                                spanned.append(f'{row + span}-{col}')

                        content[row].pop(0)

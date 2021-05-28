from app import db
from app.models import Tables
import json


def create_table(content, rows, columns, page_id, page_index):
    content = json.dumps(content)
    table = Tables(content, rows, columns, page_id, page_index)

    db.session.add(table)
    db.session.commit()


def get_table(table_id):
    table = Tables.query.filter_by(id=table_id).first()

    return table


def get_all_tables():
    tables = Tables.query.all()

    return tables


def load_table_content(table):
    # ЗДЕСЬ ОШИБКА РАЗБЕЗРИСЬ
    # content = str(table.content).strip("'<>() ").replace('\'', '\"')
    # content = json.loads(content.encode('utf8'))

    content = json.loads(table.content.encode('utf8'))

    return content


def get_tables_data():
    tables = get_all_tables()

    data = []
    for table in tables:
        content = load_table_content(table)

        data.append(
            (
                table.id, content, table.rows, table.columns,
                table.page_id, table.page_index
            )
        )

    return data


def get_table_from_form(form):
    rows = int(form.get('rows'))
    cols = int(form.get('columns'))

    data = []
    for row in range(rows):
        data.append([])
        for col in range(cols):
            if not form.get(f'cell-{row}-{col}') and form.get(f'cell-{row}-{col}') != '':
                data[row].append('')
            else:
                data[row].append(form.get(f'cell-{row}-{col}'))

    return data


def change_table_format(table_id, rows=0, cols=0):
    table = get_table(table_id)

    if rows:
        table.rows = rows

    if cols:
        table.cols = cols

    db.session.commit()


def update_table(table_id, **kwargs):
    table = get_table(table_id)
    kwargs['content'] = json.dumps(kwargs['content'])

    for key, value in kwargs.items():
        setattr(table, key, value)

    db.session.commit()


def delete_table(table_id):
    table = get_table(table_id)

    db.session.delete(table)
    db.session.commit()

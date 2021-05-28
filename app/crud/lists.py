from app import db
from app.models import Lists
import json


def create_list(label, content, rows, page_id, page_index):
    content = json.dumps(content)
    list = Lists(label, content, rows, page_id, page_index)

    db.session.add(list)
    db.session.commit()


def get_list(list_id):
    list = Lists.query.filter_by(id=list_id).first()

    return list


def get_all_lists():
    lists = Lists.query.all()

    return lists


def load_list_content(list):
    content = json.loads(list.content.encode('utf8'))

    return content


def get_lists_data():
    lists = get_all_lists()

    data = []
    for list in lists:
        content = load_list_content(list)

        data.append(
            (
                list.id, list.label, content, list.rows,
                list.page_id, list.page_index
            )
        )

    return data


def get_list_from_form(form):
    rows = int(form.get('rows'))

    data = []
    for row in range(rows):
        if not form.get(f'row-{row}') and form.get(f'row-{row}') != '':
            data.append('')
        else:
            data.append(form.get(f'row-{row}'))

    return data


def update_list(list_id, **kwargs):
    list = get_list(list_id)
    kwargs['content'] = json.dumps(kwargs['content'])

    for key, value in kwargs.items():
        setattr(list, key, value)

    db.session.commit()


def delete_list(list_id):
    list = get_list(list_id)

    db.session.delete(list)
    db.session.commit()

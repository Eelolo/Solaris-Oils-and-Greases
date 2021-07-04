from app import db
from app.models import Lists
import json


def create_list(label, content, rows, page_id, page_index):
    content = json.dumps(content)
    list_ = Lists(label, content, rows, page_id, page_index)

    db.session.add(list_)
    db.session.commit()

    return list_


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
            [
                list.id, list.label, content, list.rows,
                list.page_id, list.page_index
            ]
        )

    return data


def update_list(list_id, **kwargs):
    list_ = get_list(list_id)
    kwargs['content'] = json.dumps(kwargs['content'])

    for key, value in kwargs.items():
        setattr(list_, key, value)

    db.session.commit()

    return list_


def delete_list(list_id):
    list = get_list(list_id)

    db.session.delete(list)
    db.session.commit()

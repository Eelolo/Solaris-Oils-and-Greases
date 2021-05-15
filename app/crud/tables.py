from app import db
from app.models import Tables


def create_table(content, page_id):
    table = Tables(content, page_id)

    db.session.add(table)
    db.session.commit()


def get_table(table_id):
    table = Tables.query.filter_by(id=table_id).first()

    return table


def get_all_tables():
    tables = Tables.query.all()

    return tables


def update_table(table_id, **kwargs):
    table = get_table(table_id)

    for key, value in kwargs.items():
        setattr(table, key, value)

    db.session.commit()


def delete_table(table_id):
    table = get_table(table_id)

    db.session.delete(table)
    db.session.commit()

from app import db
from app.models import Headers


def create_header(tag, content):
    header = Headers(tag, content)

    db.session.add(header)
    db.session.commit()


def get_header(header_id):
    header = Headers.query.filter_by(id=header_id).first()

    return header


def get_all_headers():
    headers = Headers.query.all()

    return headers


def update_header(header_id, **kwargs):
    header = get_header(header_id)

    for key, value in kwargs.items():
        setattr(header, key, value)

    db.session.commit()


def delete_header(header_id):
    header = get_header(header_id)

    db.session.delete(header)
    db.session.commit()

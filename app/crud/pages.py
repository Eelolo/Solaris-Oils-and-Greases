from app import db
from app.models import Pages


def create_page(name):
    page = Pages(name)

    db.session.add(page)
    db.session.commit()


def get_page(page_id):
    page = Pages.query.filter_by(id=page_id).first()

    return page


def get_all_pages():
    pages = Pages.query.all()

    return pages

def get_pages_data():
    pages = get_all_pages()

    data = []
    for page in pages:
        data.append((page.id, page.name))

    return data

def update_page(page_id, **kwargs):
    page = get_page(page_id)

    for key, value in kwargs.items():
        setattr(page, key, value)

    db.session.commit()


def delete_page(page_id):
    page = get_page(page_id)

    db.session.delete(page)
    db.session.commit()

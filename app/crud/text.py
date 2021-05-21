from app import db
from app.models import Text


def create_text(content, page_id):
    text = Text(content, page_id)

    db.session.add(text)
    db.session.commit()


def get_text(text_id):
    text = Text.query.filter_by(id=text_id).first()

    return text


def get_all_text():
    text = Text.query.all()

    return text


def get_text_data():
    texts = get_all_text()

    data = []
    for text in texts:
        data.append((text.id, text.content, text.page_id))

    return data


def update_text(text_id, **kwargs):
    text = get_text(text_id)

    for key, value in kwargs.items():
        setattr(text, key, value)

    db.session.commit()


def delete_text(text_id):
    text = get_text(text_id)

    db.session.delete(text)
    db.session.commit()

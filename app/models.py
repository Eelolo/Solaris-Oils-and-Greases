from app import db


class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    headers = db.relationship('Headers', backref='page')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Page {self.name}>"


class Headers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(2))
    content = db.Column(db.String(100))

    page_id = db.Column(db.Integer, db.ForeignKey('Pages.id'))


    def __init__(self, tag, content):
        self.tag = tag
        self.content = content

    def __repr__(self):
        return f"<Header {self.tag}>"

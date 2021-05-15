from app import db


class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    headers = db.relationship('Headers', backref='page')
    text = db.relationship('Text', backref='page')
    tables = db.relationship('Tables', backref='page')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Page {self.name}>"


class Headers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(2))
    content = db.Column(db.String(100))

    page_id = db.Column(db.Integer, db.ForeignKey(Pages.id))


    def __init__(self, tag, content):
        self.tag = tag
        self.content = content

    def __repr__(self):
        return f"<Header {self.tag}>"


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))

    page_id = db.Column(db.Integer, db.ForeignKey(Pages.id))

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f"<Text {self.id}>"


class Tables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(10000))

    page_id = db.Column(db.Integer, db.ForeignKey(Pages.id))

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f"<Table {self.id}>"

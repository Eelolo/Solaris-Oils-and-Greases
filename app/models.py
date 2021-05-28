from app import db


class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    headers = db.relationship('Headers', backref='page')
    text = db.relationship('Text', backref='page')
    lists = db.relationship('Lists', backref='page')
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
    page_index = db.Column(db.Integer)

    def __init__(self, tag, content, page_id, page_index):
        self.tag = tag
        self.content = content
        self.page_id = page_id
        self.page_index = page_index

    def __repr__(self):
        return f"<Header {self.tag}>"


class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))

    page_id = db.Column(db.Integer, db.ForeignKey(Pages.id))
    page_index = db.Column(db.Integer)

    def __init__(self, content, page_id, page_index):
        self.content = content
        self.page_id = page_id
        self.page_index = page_index

    def __repr__(self):
        return f"<Text {self.id}>"


class Lists(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(1000))
    content = db.Column(db.String(10000))
    rows = db.Column(db.Integer)
    page_id = db.Column(db.Integer, db.ForeignKey(Pages.id))
    page_index = db.Column(db.Integer)

    def __init__(self, label, content, rows, page_id, page_index):
        self.label = label
        self.content = content
        self.rows = rows
        self.page_id = page_id
        self.page_index = page_index

    def __repr__(self):
        return f"<List {self.id}>"


class Tables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(10000))
    rows = db.Column(db.Integer)
    columns = db.Column(db.Integer)
    page_id = db.Column(db.Integer, db.ForeignKey(Pages.id))
    page_index = db.Column(db.Integer)

    def __init__(self, content, rows, columns, page_id, page_index):
        self.content = content
        self.rows = rows
        self.columns = columns
        self.page_id = page_id
        self.page_index = page_index

    def __repr__(self):
        return f"<Table {self.id}>"

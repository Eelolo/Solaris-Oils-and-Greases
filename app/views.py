from flask import Blueprint, render_template, redirect
from .models import Headers, Text, Tables, Pages
from .crud.tables import load_table_content


main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index_page.html')


@main_bp.route('/<page_name>/')
def site_page(page_name):
    if page_name == 'favicon.ico':
        return redirect('/favicon.ico')

    page_id = Pages.query.filter_by(name=page_name).one().id
    headers = Headers.query.filter_by(page_id=page_id).all()
    text = Text.query.filter_by(page_id=page_id).all()
    tables = Tables.query.filter_by(page_id=page_id).all()

    for table in tables:
        content = load_table_content(table)
        table.content = content

    elements = headers + text + tables
    elements.sort(key=lambda x: x.page_index)

    data = []
    for elem in elements:
        if isinstance(elem, Headers):
            data.append(('header', elem))
        if isinstance(elem, Text):
            data.append(('text', elem))
        if isinstance(elem, Tables):
            data.append(('table', elem))

    return render_template('site_page.html', data=data)

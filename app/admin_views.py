from flask import render_template, Blueprint, request, flash, redirect, jsonify
from .crud.headers import get_headers_data, create_header, get_header, update_header, delete_header
from .crud.pages import get_page, create_page, update_page, delete_page, get_pages_data, get_pages_ids
from .crud.tables import (
    get_tables_data, create_table, get_table, update_table, delete_table,
    change_table_format, load_table_content
)
from .crud.text import get_text_data, create_text, update_text, delete_text
from .crud.lists import get_lists_data, load_list_content, create_list, get_list, update_list, delete_list
import json


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/')
def admin():
    return render_template('admin_page.html')


@admin_bp.route('/get_pages/')
def get_pages():
    pages = get_pages_data()

    data = {
        'table_name': 'pages',
        'table_data': [('Id', 'Name', 'Actions')] + pages
    }
    data = json.dumps(data)

    return jsonify(result=data)


@admin_bp.route('/get_headers/')
def get_headers():
    headers = get_headers_data()

    data = {
        'table_name': 'headers',
        'table_data': [('Id', 'Tag', 'Content', 'Page id', 'Page index', 'Actions')] + headers
    }

    data = json.dumps(data)

    return jsonify(result=data)


@admin_bp.route('/get_text/')
def get_text():
    text = get_text_data()

    for idx in range(len(text)):
        text[idx].pop(1)

    data = {
        'table_name': 'text',
        'table_data': [('Id', 'Page id', 'Page index', 'Actions')] + text
    }

    data = json.dumps(data)

    return jsonify(result=data)


@admin_bp.route('/get_lists/')
def get_lists():
    lists = get_lists_data()

    for idx in range(len(lists)):
        lists[idx].pop(2)

    data = {
        'table_name': 'lists',
        'table_data': [('Id', 'Label', 'Rows', 'Page id', 'Page index', 'Actions')] + lists
    }

    data = json.dumps(data)

    return jsonify(result=data)


@admin_bp.route('/get_tables/')
def get_tables():
    tables = get_tables_data()

    for idx in range(len(tables)):
        tables[idx].pop(1)

    data = {
        'table_name': 'tables',
        'table_data': [('Id', 'Rows', 'Columns', 'Page id', 'Page index', 'Actions')] + tables
    }

    data = json.dumps(data)

    return jsonify(result=data)


@admin_bp.route('/create_page/', methods=['GET', 'POST'])
def admin_create_page():
    page_name = request.args.get('page_name', None, type=str)
    page = create_page(page_name)

    page = [page.id, page.name]
    return jsonify(result=page)


@admin_bp.route('/update_page/<page_id>/')
def admin_update_page(page_id):
    page_name = request.args.get('page_name', None, type=str)
    update_page(page_id, name=page_name)
    return f'Page {page_id} updated'


@admin_bp.route('/delete_page/<page_id>/')
def admin_delete_page(page_id):
    page = get_page(page_id)
    delete_page(page_id)

    page = [page.id, page.name]
    return jsonify(result=page)

@admin_bp.route('/get_pages_ids/')
def admin_get_pages_ids():
    ids = get_pages_ids()

    return jsonify(result=ids)


@admin_bp.route('/create_header/', methods=['GET', 'POST'])
def admin_create_header():
    tag = request.args.get('tag', None, type=str)
    content = request.args.get('content', None, type=str)
    page_id = request.args.get('page_id', None, type=int)
    page_index = request.args.get('page_index', None, type=int)

    header = create_header(tag, content, page_id, page_index)
    header = [header.id, header.tag, header.content, header.page_id, header.page_index]

    return jsonify(result=header)


@admin_bp.route('/update_header/<header_id>/')
def admin_update_header(header_id):
    tag = request.args.get('tag', None, type=str)
    content = request.args.get('content', None, type=str)
    page_id = request.args.get('page_id', None, type=int)
    page_index = request.args.get('page_index', None, type=int)

    header = update_header(header_id, tag=tag, content=content, page_id=page_id, page_index=page_index)
    header = [header.id, header.tag, header.content, header.page_id, header.page_index]

    return jsonify(result=header)

@admin_bp.route('/delete_header/<header_id>/')
def admin_delete_header(header_id):
    header = get_header(header_id)

    delete_header(header_id)
    header = [header.id, header.tag, header.content, header.page_id, header.page_index]

    return jsonify(result=header)


@admin_bp.route('/get_one_text/<text_id>/')
def get_one_text(text_id):
    from .crud.text import get_text

    text = get_text(text_id)
    text = [
        text.id, text.content,
        text.page_id, text.page_index
    ]

    return jsonify(result=text)

@admin_bp.route('/create_text/')
def admin_create_text():
    content = request.args.get('content', None, type=str)
    page_id = request.args.get('page_id', None, type=int)
    page_index = request.args.get('page_index', None, type=int)

    text = create_text(content, page_id, page_index)
    text = [text.id, text.content, text.page_id, text.page_index]

    return jsonify(result=text)


@admin_bp.route('/update_text/<text_id>/')
def admin_update_text(text_id):
    content = request.args.get('content', None, type=str)
    page_id = request.args.get('page_id', None, type=int)
    page_index = request.args.get('page_index', None, type=int)

    text = update_text(text_id, content=content, page_id=page_id, page_index=page_index)
    text = [text.id, text.content, text.page_id, text.page_index]

    return jsonify(result=text)


@admin_bp.route('/delete_text/<text_id>/')
def admin_delete_text(text_id):
    from .crud.text import get_text

    text = get_text(text_id)
    delete_text(text_id)

    text = [text.id, text.content, text.page_id, text.page_index]

    return jsonify(result=text)


@admin_bp.route('/get_list/<list_id>/')
def get_list(list_id):
    from .crud.lists import get_list

    list_ = get_list(list_id)
    list_ = [
        list_.id, list_.label, json.loads(list_.content),
        list_.page_id, list_.page_index
    ]

    return jsonify(result=list_)


@admin_bp.route('/create_list/')
def admin_create_list():
    content = json.loads(request.args.get('content', None, type=str))
    label = content.pop(0)
    rows = len(content)
    page_id = request.args.get('page_id', None, type=int)
    page_index = request.args.get('page_index', None, type=int)

    list_ = create_list(label, content, rows, page_id, page_index)
    list_ = [list_.id, list_.label, list_.content, list_.rows, list_.page_id, list_.page_index]

    return jsonify(result=list_)


@admin_bp.route('/update_list/<list_id>/')
def admin_update_list(list_id):
    content = json.loads(request.args.get('content', None, type=str))
    label = content.pop(0)
    rows = len(content)
    page_id = request.args.get('page_id', None, type=int)
    page_index = request.args.get('page_index', None, type=int)

    list_ = update_list(
        list_id, label=label, content=content,
        rows=rows, page_id=page_id, page_index=page_index
    )
    list_ = [list_.id, list_.label, list_.content, list_.page_id, list_.page_index]

    return jsonify(result=list_)


@admin_bp.route('/delete_list/<list_id>/')
def admin_delete_list(list_id):
    from .crud.lists import get_list

    list_ = get_list(list_id)
    delete_list(list_id)

    list_ = [list_.id, list_.label, list_.content, list_.rows, list_.page_id, list_.page_index]

    return jsonify(result=list_)


@admin_bp.route('/get_table/<table_id>/')
def get_table(table_id):
    from .crud.tables import get_table

    table = get_table(table_id)
    table = [
        table.id, json.loads(table.content),
        table.rows, table.columns, table.page_id, table.page_index
    ]

    return jsonify(result=table)


@admin_bp.route('/create_table/')
def admin_create_table():
    content = json.loads(request.args.get('content', None, type=str))

    from pprint import pprint
    pprint(content)

    rows = len(content)
    cols = len(content[0])

    page_id = request.args.get('page_id', None, type=int)
    page_index = request.args.get('page_index', None, type=int)

    table = create_table(content, rows, cols, page_id, page_index)
    table = [
        table.id, table.content, table.rows,
        table.columns, table.page_id, table.page_index
    ]

    return jsonify(result=table)


@admin_bp.route('/update_table/<table_id>/')
def admin_update_table(table_id):
    content = json.loads(request.args.get('content', None, type=str))
    rows = len(content)
    cols = len(content[0])
    page_id = request.args.get('page_id', None, type=int)
    page_index = request.args.get('page_index', None, type=int)

    table = update_table(
        table_id, content=content, rows=rows,
        columns=cols, page_id=page_id, page_index=page_index
    )
    table = [
        table.id, table.content, table.rows,
        table.columns, table.page_id, table.page_index
    ]

    return jsonify(result=table)

@admin_bp.route('/delete_table/<table_id>/')
def admin_delete_table(table_id):
    from .crud.tables import get_table

    table = get_table(table_id)
    delete_table(table_id)

    table = [
        table.id, table.content, table.rows, table.columns,
        table.page_id, table.page_index
    ]

    return jsonify(result=table)


@admin_bp.route('/list_look/<list_id>/')
def admin_list_look(list_id):
    list = get_list(list_id)
    content = load_list_content(list)
    data = list.label, content, list.rows

    return render_template('list_look.html', data=data)


@admin_bp.route('/table_look/<table_id>/')
def admin_table_look(table_id):
    table = get_table(table_id)
    content = load_table_content(table)
    data = table.id, content, table.rows, table.columns, table.page_id, table.page_index

    return render_template('table_look.html', data=data)


def change_format(form, table_id=None):
    if table_id:
        table = get_table(table_id)

    rows = int(form.get('rows'))
    columns = int(form.get('columns'))

    if request.form.get('format-btn') == 'Add Row':
        rows += 1

        if table_id:
            change_table_format(table_id, rows=table.rows + 1)

    if request.form.get('format-btn') == 'Delete Row':
        rows -= 1

        if table_id:
            change_table_format(table_id, rows=table.rows - 1)

    if request.form.get('format-btn') == 'Add Column':
        columns += 1

        if table_id:
            change_table_format(table_id, rows=table.columns + 1)

    if request.form.get('format-btn') == 'Delete Column':
        columns -= 1

        if table_id:
            change_table_format(table_id, rows=table.columns - 1)

    return rows, columns


def change_list_rows(form, list_id=None):
    if list_id:
        list = get_list(list_id)

    rows = int(form.get('rows'))

    if request.form.get('format-btn') == 'Add Row':
        rows += 1

        if list_id:
            change_table_format(list_id, rows=list.rows + 1)

    if request.form.get('format-btn') == 'Delete Row':
        rows -= 1

        if list_id:
            change_table_format(list_id, rows=list.rows - 1)

    return rows

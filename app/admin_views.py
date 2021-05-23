from flask import render_template, Blueprint, request, flash, redirect
from .crud.headers import get_headers_data, create_header, get_header, update_header, delete_header
from .crud.pages import get_page, create_page, update_page, delete_page, get_pages_data, get_pages_ids
from .crud.tables import (
    get_tables_data, create_table, get_table, update_table, delete_table,
    change_table_format, get_table_from_form, loads_table_content
)
from .crud.text import get_text_data, create_text, get_text, update_text, delete_text


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/')
def admin():
    headers = get_headers_data()
    pages = get_pages_data()
    text = get_text_data()
    tables = get_tables_data()

    return render_template(
        'admin_page.html',
        headers=headers, pages=pages, text=text, tables=tables,
    )


@admin_bp.route('/create_page/', methods=['GET', 'POST'])
def admin_create_page():
    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Create':
            name = request.form.get('name')

            if name:
                create_page(name)

            flash(f'Page {name} created')

        return redirect('/admin')

    return render_template('page_form.html')


@admin_bp.route('/update_page/<page_id>/', methods=['GET', 'POST'])
def admin_update_page(page_id):
    page = get_page(page_id)
    data = page.id, page.name

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            name = request.form.get('name')

            if name:
                update_page(page_id, name=name)

            flash(f'Page {data[1]} updated')

        return redirect('/admin')

    return render_template('page_form.html', data=data)


@admin_bp.route('/delete_page/<page_id>/')
def admin_delete_page(page_id):
    page = get_page(page_id)
    delete_page(page_id)

    flash(f'Page {page.name} deleted')
    return redirect('/admin')


@admin_bp.route('/create_header/', methods=['GET', 'POST'])
def admin_create_header():
    pages_ids = get_pages_ids()

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Create':
            tag = request.form.get('tag')
            content = request.form.get('content')
            page_id = request.form.get('page_select')

            if tag and content:
                create_header(tag, content, page_id)

            flash(f'Header {tag} created')

        return redirect('/admin')

    return render_template('header_form.html', pages_ids=pages_ids)


@admin_bp.route('/update_header/<header_id>/', methods=['GET', 'POST'])
def admin_update_header(header_id):
    pages_ids = get_pages_ids()
    header = get_header(header_id)
    data = header.id, header.tag, header.content, header.page_id

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            tag = request.form.get('tag')
            content = request.form.get('content')
            page_id = request.form.get('page_select')

            if tag and content:
                update_header(header_id, tag=tag, content=content, page_id=page_id)

            flash(f'Header {data[1]} updated')

        return redirect('/admin')

    return render_template('header_form.html', data=data, pages_ids=pages_ids)


@admin_bp.route('/delete_header/<header_id>/')
def admin_delete_header(header_id):
    header = get_header(header_id)
    delete_header(header_id)

    flash(f'Header {header.tag} deleted')
    return redirect('/admin')


@admin_bp.route('/create_text/', methods=['GET', 'POST'])
def admin_create_text():
    pages_ids = get_pages_ids()

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Create':
            content = request.form.get('content')
            page_id = request.form.get('page_select')

            if content:
                create_text(content, page_id)

            flash('Text created')

        return redirect('/admin')

    return render_template('text_form.html', pages_ids=pages_ids)


@admin_bp.route('/update_text/<text_id>/', methods=['GET', 'POST'])
def admin_update_text(text_id):
    pages_ids = get_pages_ids()
    text = get_text(text_id)
    data = text.id, text.content, text.page_id

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            content = request.form.get('content')
            page_id = request.form.get('page_select')

            if content:
                update_text(text_id, content=content, page_id=page_id)

            flash(f'Text {data[0]} updated')

        return redirect('/admin')

    return render_template('text_form.html', data=data, pages_ids=pages_ids)


@admin_bp.route('/delete_text/<text_id>/')
def admin_delete_text(text_id):
    text = get_text(text_id)
    delete_text(text_id)

    flash(f'Text {text.id} deleted')
    return redirect('/admin')


@admin_bp.route('/create_table/', methods=['GET', 'POST'])
def admin_create_table():
    pages_ids = get_pages_ids()
    rows = 4
    columns = 4

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Create':
            page_id = request.form.get('page_select')
            rows = int(request.form.get('rows'))
            columns = int(request.form.get('columns'))

            content = get_table_from_form(request.form)

            if rows and columns:
                create_table(content, rows, columns, page_id)

            flash('table created')

        if request.form.get('format-btn'):
            rows, columns = change_format(request.form)
            form = dict(request.form)
            form['rows'] = rows
            form['columns'] = columns
            table_content = get_table_from_form(form)

            return render_template(
                'table_form.html', pages_ids=pages_ids, rows=rows,
                columns=columns, table_content=table_content
            )

        return redirect('/admin')

    return render_template('table_form.html', pages_ids=pages_ids, rows=rows, columns=columns)


@admin_bp.route('/table_look/<table_id>/')
def admin_table_look(table_id):
    table = get_table(table_id)
    content = loads_table_content(table)
    data = table.id, content, table.rows, table.columns, table.page_id

    return render_template('table_look.html', data=data)


@admin_bp.route('/update_table/<table_id>/', methods=['GET', 'POST'])
def admin_update_table(table_id):
    pages_ids = get_pages_ids()
    table = get_table(table_id)
    content = loads_table_content(table)
    data = table.id, content, table.rows, table.columns, table.page_id

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            page_id = request.form.get('page_select')
            rows = int(request.form.get('rows'))
            columns = int(request.form.get('columns'))

            content = get_table_from_form(request.form)

            if rows and columns:
                update_table(table_id, content=content, rows=rows, columns=columns, page_id=page_id)

            flash(f'table {data[0]} updated')

        if request.form.get('format-btn'):
            rows, columns = change_format(request.form)
            form = dict(request.form)
            form['rows'] = rows
            form['columns'] = columns
            table_content = get_table_from_form(form)
            data = table.id, table_content, rows, columns, table.page_id

            return render_template(
                'table_form.html', data=data, pages_ids=pages_ids
            )

        return redirect('/admin')

    return render_template('table_form.html', data=data, pages_ids=pages_ids)


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


@admin_bp.route('/delete_table/<table_id>/')
def admin_delete_table(table_id):
    table = get_table(table_id)
    delete_table(table_id)

    flash(f'table {table.id} deleted')
    return redirect('/admin')

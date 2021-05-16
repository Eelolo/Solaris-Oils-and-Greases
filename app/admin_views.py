from flask import render_template, Blueprint, request, flash, redirect
from .crud.headers import get_all_headers
from .crud.pages import get_page, create_page, update_page, delete_page, get_pages_data
from .crud.tables import get_all_tables
from .crud.text import get_all_text


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/')
def admin():
    headers = get_all_headers()
    pages = get_pages_data()
    text = get_all_tables()
    tables = get_all_text()

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

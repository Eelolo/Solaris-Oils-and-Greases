from flask import render_template, Blueprint
from .crud.headers import get_all_headers
from .crud.pages import get_all_pages
from .crud.tables import get_all_tables
from .crud.text import get_all_text


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/')
def admin():
    headers = get_all_headers()
    pages = get_all_pages()
    text = get_all_tables()
    tables = get_all_text()

    return render_template(
        'admin_page.html',
        headers=headers, pages=pages, text=text, tables=tables,
    )


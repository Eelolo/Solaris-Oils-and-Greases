from flask import render_template, Blueprint, request, flash, redirect
from .crud.headers import get_headers_data, create_header, get_header, update_header, delete_header
from .crud.pages import get_page, create_page, update_page, delete_page, get_pages_data, get_pages_ids
from .crud.tables import (
    get_tables_data, create_table, get_table, update_table, delete_table,
    change_table_format, get_table_from_form, loads_table_content
)
from .crud.text import get_text_data, create_text, get_text, update_text, delete_text
from .models import Pages

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/')
def admin():
    headers = get_headers_data()
    pages = get_pages_data()
    text = get_text_data()
    tables = get_tables_data()

    data = {
        "antifrict_oils": {
            "h1": [
                "СМАЗКИ"
            ],
            "h3": [
                "Назначение смазок",
                "",
                "Свойства смазок при  различных загустителях",
                "Классификация пластичных  смазок по ГОСТ 23258-78",
                "Антифрикционные смазки",
                "Смазки  общего назначения для обычных температур",
                "Смазки общего назначения  для повышенных температур",
                "Многоцелевые смазки",
                "Термостойкие смазки",
                "Низкотемпературные смазки",
                "Химически стойкие смазки",
                "Приборные смазки",
                "Редукторные смазки  (полужидкие)",
                "Приработочные пасты",
                "Узкоспециализированные  (Отраслевые) смазки",
                "Смазки для электрических  машин",
                "Автомобильные смазки",
                "Железнодорожные смазки",
                "Морские смазки",
                "Авиационные смазки",
                "Индустриальные смазки",
                "Буровые смазки",
                "Электроконтактные смазки",
                "Консервационные  (Защитные) смазки",
                "Канатные смазки и  пропиточные составы",
                "Антифрикционные  смазки",
                "Узкоспециализированные (Отраслевые)  смазки",
                "Консервационные (Защитные)  смазки *",
                "Уплотнительные (Резьбовые)  смазки"
            ]
        },
        "avia_oils": {
            "h1": [
                "АВИАЦИОННЫЕ МАСЛА"
            ],
            "h3": [
                "Масла для поршневых  двигателей",
                "",
                "Масла для турбореактивных  двигателей",
                "Минеральные масла",
                "Характеристики  минеральных масел для турбореактивных двигателей",
                "Синтетические масла",
                "Характеристики  синтетических масел для газотурбинных двигателей",
                "Характеристики  синтетических масел для газотурбинных двигателей",
                "Масла для турбовинтовых  двигателей",
                "Характеристики масла  МН-7,5у и маслосмеси СМ-4,5",
                "Масла для вертолетов",
                "Характеристики  маслосмесей, используемых в редукторах вертолетов",
                "Смазочные масла для  шарниров винтов вертолетов",
                "Характеристика масел для  осевых шарниров втулок винтов вертолетов",
                "Смазывающие свойства авиационных масел (ГОСТ 9490-75)",
                "Совместимость масел для  авиационных газотурбинных двигателей"
            ]
        },
        "cabel_transform_oils": {
            "h1": [
                "КАБЕЛЬНЫЕ И ТРАНСФОРМАТОРНЫЕ МАСЛА"
            ],
            "h3": [
                "Электроизоляционные масла",
                "Трансформаторные масла",
                "Общие  требования и свойства",
                "Требования  Международной электротехнической комиссии  к трансформаторным маслам классов II, НА, III, IIIA  (Публикация 296)",
                "Требования к качеству эксплуатационных трансформаторных масел",
                "Ассортимент  трансформаторных масел",
                "Характеристики  трансформаторных масел",
                "Конденсаторные масла",
                "Характеристики  конденсаторных масел",
                "Кабельные масла",
                "Характеристики кабельных  масел"
            ]
        },
        "compress_oils": {
            "h1": [
                "КОМПРЕССОРНЫЕ МАСЛА"
            ],
            "h3": [
                "Компрессорные масла",
                "Масла для поршневых и  ротационных компрессоров",
                "Характеристики  компрессорных масел",
                "Компрессорные масла без  присадок",
                "Компрессорные  масла с присадками",
                "Масла для турбокомпрессоров",
                "Масла для компрессоров  холодильных машин",
                "Характеристики масел для компрессоров холодильных машин"
            ]
        },
        "delivering_oils": {
            "h1": [
                "Главная"
            ],
            "h3": [
                ""
            ]
        },
        "gidravl_oils": {
            "h1": [
                "ГИДРАВЛИЧЕСКИЕ МАСЛА"
            ],
            "h3": [
                "Характеристики масел для гидромеханических передач",
                "Обозначение товарных  гидравлических масел",
                "Характеристики  низкозастывающих  гидравлических масел МГЕ-10А, ВМГЗ, АМГ-10",
                "Характеристики  гидравлических жидкостей"
            ]
        },
        "industrial_oils": {
            "h1": [
                "ИНДУСТРИАЛЬНЫЕ МАСЛА"
            ],
            "h3": [
                "Группы индустриальных  масел по назначению",
                "Подгруппы индустриальных  масел для машин и механизмов  промышленного оборудования по эксплуатационным свойствам",
                "Классы вязкости  индустриальных масел по ISO 3448-75",
                "Масла общего назначения",
                "Масла без присадок",
                "Характеристики индустриальных  масел  общего назначения без присадок  (ГОСТ 20799-88)",
                "Характеристики базовых  масел серии ВИ (ТУ 38. 101308-97)",
                "Масла с присадками  (легированные)",
                "Характеристики индустриальных  масел И-Л-С и ИГП",
                "Характеристики индустриальных  масел  И-Л-С и ИГП (продолжение)",
                ""
            ]
        },
        "motor_oils": {
            "h1": [
                "МОТОРНЫЕ МАСЛА"
            ],
            "h3": [
                "Соответствие обозначений  марок моторных масел по ГОСТ 17479.1-85 и ранее принятых обозначений",
                "Для двухтактных  двигателей",
                "Масла групп Г1 В и B1",
                "Характеристики  масел групп Г1, В и В1",
                "Масла групп А и Б2",
                "Характеристики масел  групп А и Б2",
                "Масла группы В2",
                "Масла группы Г2",
                "Масла группы Д2"
            ]
        },
        "pribornie_oils": {
            "h1": [
                "ПРИБОРНЫЕ МАСЛА"
            ],
            "h3": [
                "Приборные масла",
                "Масла общего назначения",
                "Характеристики приборных  масел общего назначения",
                "Масла специального  назначения  на синтетической или минеральной основе",
                "Характеристики приборных  масел специального назначения",
                "Характеристики приборных  масел специального назначения (продолжение)",
                "Характеристики приборных  масел специального назначения (окончание)",
                "Масла на смешанной  (синтетической и минеральной) основе",
                "Характеристики масел на  смешанной основе",
                "Часовые масла"
            ]
        },
        "price_list": {
            "h1": [
                "Прайс-лист"
            ],
            "h3": []
        },
        "ships_oils": {
            "h1": [
                "СУДОВЫЕ МАСЛА"
            ],
            "h3": []
        },
        "special_fluids": {
            "h1": [
                "СПЕЦИАЛЬНЫЕ ЖИДКОСТИ"
            ],
            "h3": [
                "Масла цилиндровые",
                "Характеристики  цилиндровых масел",
                "Масла специального  назначения",
                "Характеристики масел  И-68СХ и И-Т-С-320(мт)",
                "Характеристики масел  И-Л-С-220(Мо), И-Л-Д-1000 и серии ИМСп",
                "Масла для текстильного  оборудования",
                "Характеристики масел для текстильного оборудования",
                "Полусинтетические бытовые  масла",
                "Характеристики масел для  бытовой техники",
                "Масла  рабочеконсервационные",
                "Характеристики рабоче-консервационных масел ТМ-3-18(чрк)",
                "Жидкости формовочные ТСП и  СЖФ-9",
                "Характеристики  формовочных жидкостей",
                "Защитные жидкости  Предокол и АГ-5И",
                "Характеристики защитных  жидкостей",
                "Характеристики рабочих  жидкостей для электроэрозионных станков",
                "Физико-химические  характеристики водосмешиваемых СОТС",
                "Физико-химические  характеристики масляных СОТС",
                "Бактерицидные присадки"
            ]
        },
        "transmission_oils": {
            "h1": [
                "ТРАНСМИССИОННЫЕ МАСЛА"
            ],
            "h3": [
                "Важнейшие  свойства трансмиссионных масел",
                "Соответствие обозначений трансмиссионных масел по ГОСТ 17479.2-85 принятым в  нормативно-технической документации",
                "Ассортимент  трансмиссионных масел"
            ]
        },
        "turbo_oils": {
            "h1": [
                "ТУРБИННЫЕ МАСЛА"
            ],
            "h3": [
                "Турбинные масла",
                "Общие требования и  свойства",
                "Ассортимент  турбинных масел",
                "Характеристики турбинных  масел"
            ]
        }
    }

    names = (
        'antifrict_oils', 'avia_oils', 'cabel_transform_oils', 'compress_oils', 'gidravl_oils',
        'industrial_oils', 'motor_oils', 'pribornie_oils', 'price_list', 'ships_oils',
        'special_fluids', 'transmission_oils', 'turbo_oils'
    )



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
            page_index = request.form.get('page_index')

            if tag and content and page_index:
                create_header(tag, content, page_id, page_index)

            flash(f'Header {tag} created')

        return redirect('/admin')

    return render_template('header_form.html', pages_ids=pages_ids)


@admin_bp.route('/update_header/<header_id>/', methods=['GET', 'POST'])
def admin_update_header(header_id):
    pages_ids = get_pages_ids()
    header = get_header(header_id)
    data = header.id, header.tag, header.content, header.page_id, header.page_index

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            tag = request.form.get('tag')
            content = request.form.get('content')
            page_id = request.form.get('page_select')
            page_index = request.form.get('page_index')

            if tag and content:
                update_header(header_id, tag=tag, content=content, page_id=page_id, page_index=page_index)

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
            page_index = request.form.get('page_index')

            if content:
                create_text(content, page_id, page_index)

            flash('Text created')

        return redirect('/admin')

    return render_template('text_form.html', pages_ids=pages_ids)


@admin_bp.route('/update_text/<text_id>/', methods=['GET', 'POST'])
def admin_update_text(text_id):
    pages_ids = get_pages_ids()
    text = get_text(text_id)
    data = text.id, text.content, text.page_id, text.page_index

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            content = request.form.get('content')
            page_id = request.form.get('page_select')
            page_index = request.form.get('page_index')

            if content and page_index:
                update_text(text_id, content=content, page_id=page_id, page_index=page_index)

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
            page_index = request.form.get('page_index')

            content = get_table_from_form(request.form)

            if rows and columns:
                create_table(content, rows, columns, page_id, page_index)

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
    data = table.id, content, table.rows, table.columns, table.page_id, table.page_index

    return render_template('table_look.html', data=data)


@admin_bp.route('/update_table/<table_id>/', methods=['GET', 'POST'])
def admin_update_table(table_id):
    pages_ids = get_pages_ids()
    table = get_table(table_id)
    content = loads_table_content(table)
    data = table.id, content, table.rows, table.columns, table.page_id, table.page_index

    if request.method == 'POST':
        if request.form.get('submit-btn') == 'Update':
            page_id = request.form.get('page_select')
            rows = int(request.form.get('rows'))
            columns = int(request.form.get('columns'))
            page_index = request.form.get('page_index')

            content = get_table_from_form(request.form)

            if rows and columns and page_index:
                update_table(
                    table_id, content=content, rows=rows,
                    columns=columns, page_id=page_id, page_index=page_index
                )

            flash(f'table {data[0]} updated')

        if request.form.get('format-btn'):
            rows, columns = change_format(request.form)
            form = dict(request.form)
            form['rows'] = rows
            form['columns'] = columns
            table_content = get_table_from_form(form)
            data = table.id, table_content, rows, columns, table.page_id, table.page_index

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

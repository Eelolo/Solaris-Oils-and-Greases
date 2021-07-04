import {createConfirmButtons, createPageIdSelect, createPageIndexInput} from '../common_functions.js';
import {createList, updateList} from './crud.js';


export function renderListForm (event) {
  if ($('.list_tr').length) {
    $('.list_tr').remove()
  }
  $('#form_tr').remove();

  if (event.data) {
    let list_id = event.data.id
    let form_tr = createForm(list_id)
    form_tr = fillForm(form_tr, list_id)

    let tr = $('tr#' + list_id);
    $(tr).after(form_tr);
  } else {
    let form_tr = createForm()

    $('#create_btn_cell').remove();
    let tr = $('#create_btn_row');
    $(tr).replaceWith($(form_tr))
  };
};


function createForm (list_id) {
  let form_tr = $('<tr>').addClass('list-tr');
  let td = $('<td>').addClass("btn_cell");
  let label = $('<label>').text('List label');
  let content_label = $('<label>').text("Content");

  let ul = $('<ul>').addClass('admin-list')
  if (!list_id) {
    for (var row = 0; row < 4; row++) {
      let li = $('<li>');
      li.attr({
        'id': 'list_row-' + row
      });
      li = bindLi(li)
      ul.append(li)
    }
  }

  let add_row = $('<button>').text("Add row");
  let delete_row = $('<button>').text("Delete row");

  form_tr.attr('id', 'form_tr');
  td.attr('colspan', '6');
  label.attr({
    "id": "list_label",
    "name": "list_label",
  });
  label = bindLabel(label)

  add_row.attr({
    'id': 'add_row',
    'class': 'btn btn-outline btn-sm create_btn',
    'type': 'submit',
  })
  add_row.click(addRow)

  delete_row.attr({
    'id': 'delete_row',
    'class': 'btn btn-outline btn-sm create_btn',
    'type': 'submit',
  })

  delete_row.click(deleteRow)

  ul.append(add_row, delete_row)

  let index_label = $('<label>').text("Page index");
  let index_input = createPageIndexInput()

  let buttons = createConfirmButtons(createList, updateList, list_id, 'lists');
  let accept = buttons.accept;
  let cancel = buttons.cancel;

  let id_label = $('<label>').text("Page id");
  let id_select = createPageIdSelect()

  let single_col_row = $('<div>').addClass('row')
  let di_col_row = $('<div>').addClass('row').addClass('reduced_width')
  let confirm_row = $('<div>').addClass('row')
  let col = $('<div>').addClass('col')
  let left_col = $('<div>').addClass('col')
  let right_col = $('<div>').addClass('col')
  let confirm_col = $('<div>').addClass('col')

  col.append(content_label, label, ul)
  single_col_row.append(col)

  left_col.append(id_label, id_select)
  right_col.append(index_label, index_input)
  di_col_row.append(left_col, right_col)

  confirm_col.append(accept, cancel)
  confirm_row.append(confirm_col)

  td.append(single_col_row, di_col_row, confirm_row)

  form_tr.append(td);

  return form_tr
}


function fillForm (form_tr, list_id) {
  let list = form_tr.find('.admin-list')
  let tr = $('tr#' + list_id);
  let rows = tr.find('td:eq(2)').text();
  let id_value = tr.find('td:eq(3)').text();
  let index_value = tr.find('td:eq(4)').text();

  fillList(form_tr, list_id)
  form_tr.find('select#id_select').val(id_value).change();
  form_tr.find('#page_index').val(index_value);

  return form_tr
}


function fillList (form_tr, list_id) {
  $.getJSON($SCRIPT_ROOT + '/admin/get_list/' + list_id, {
    }, function(data) {
      let add_row = form_tr.find('#add_row')

      form_tr.find('#list_label').text(data.result[1]);
      let list_content = data.result[2];
      for (var row = 0; row < list_content.length; row++) {
        let li = $('<li>');
        li.attr({
          'id': 'list_row-' + row
        });
        li = bindLi(li)
        li.text(list_content[row])
        add_row.before(li)
      };
  });

  return form_tr
}


function bindLi (li) {
  li.click(function () {
    let li = $('#' + this.id)
    if (!(li.find('textarea').length)) {
      let textarea = createTextarea(li.text())
      li.text('');
      li.append(textarea);
      $('textarea').focus()
    }
  });

  return li
}

function bindLabel (label) {
  label.click(function () {
    let textarea = $('<textarea>').addClass('admin-textarea list-textarea');
    textarea.val(label.text())
    textarea.attr('style', 'height:' + (this.scrollHeight + 5) + 'px;overflow-y:hidden;width:1000px;');
    textarea.on('input', function () {
      this.style.height = 'auto';
      this.style.height = (this.scrollHeight) + 'px';
    });
    label.hide();
    label.after(textarea);
    $('textarea').focus()
    $('textarea').focusout(function () {
      label.text($('textarea').val())
      label.show()
      $('textarea').remove()
    })
  })

  return label
}


function createTextarea (value) {
  let textarea = $('<textarea>').addClass('admin-textarea list-textarea');
  textarea.val(value)
//  textarea.attr('style', 'height:' + (this.scrollHeight + 5) + 'px;overflow-y:hidden;width:1000px;');
  textarea.attr('style', 'overflow-y:hidden;width:1000px;');

  textarea.on('input', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
  });
  textarea.focusout(function () {
    textarea.parent().text(textarea.val())
    textarea.remove()
  })

  return textarea
}


function addRow () {
  let row = Number($('.admin-list').find('li').last().attr('id').split('-')[1]) + 1
  let li = $('<li>')
  li.attr({
    "id": "list_row-" + row,
    "name": "list_row-" + row,
  });
  li = bindLi(li)

  $('.admin-list').find('li').last().after(li)
}


function deleteRow () {
  if ($('.admin-list').find('li').length > 1) {
    $('.admin-list').find('li').last().remove()
  }
}
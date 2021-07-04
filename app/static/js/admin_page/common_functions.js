import {renderPageForm} from './pages/form.js';
import {deletePage} from './pages/c_ud.js';

import {renderHeaderForm} from './headers/form.js';
import {deleteHeader} from './headers/c_ud.js';

import {renderTextForm} from './text/form.js';
import {renderText, deleteText} from './text/crud.js';

import {renderListForm} from './lists/form.js';
import {renderList, deleteList} from './lists/crud.js';

import {renderTableForm} from './tables/form.js';
import {renderTable, deleteTable} from './tables/crud.js';


function bindButton (table_name, button) {
  if (button.id.includes('update')) {
    var id = button.id.split('-')[1]
    var btn_type = 'update'
  } else if (button.id.includes('look')) {
    var id = button.id.split('-')[1]
    var btn_type = 'look'
  } else if (button.id.includes('delete')) {
    var id = button.id.split('-')[1]
    var btn_type = 'delete'
  } else {
    var btn_type = 'create'
  };

  if (table_name === 'pages') {
    var formFunc = renderPageForm;
    var deleteFunc = deletePage;
  } else if (table_name === 'headers') {
    var formFunc = renderHeaderForm;
    var deleteFunc = deleteHeader;
  } else if (table_name === 'text') {
    var formFunc = renderTextForm;
    var deleteFunc = deleteText;
    var lookFunc = renderText;
  } else if (table_name === 'lists') {
    var formFunc = renderListForm;
    var deleteFunc = deleteList;
    var lookFunc = renderList;
  } else {
    var formFunc = renderTableForm;
    var deleteFunc = deleteTable;
    var lookFunc = renderTable;
  };

  if (btn_type === 'create') {
    $(button).click(formFunc)
  } else if (btn_type === 'look') {
    $(button).click({'id': id}, lookFunc)
  } else if (btn_type === 'update') {
    $(button).click({'id': id}, formFunc)
  } else {
    $(button).click({'id': id}, deleteFunc)
  };

  return button
}

export function createActionsButtons (table_name, id) {
  let update = $('<button>').text('Update');
  let delete_ = $('<button>').text('Delete');

  update.attr({
    'id': 'update-' + id,
    'class': 'btn btn-outline btn-sm',
    'type': 'submit',
  });

  delete_.attr({
    'id': 'delete-' + id,
    'class': 'btn btn-outline btn-sm',
    'type': 'submit',
  });

  update.id = 'update-' + id
  delete_.id = 'delete-' + id
  bindButton(table_name, update)
  bindButton(table_name, delete_)
  if (['text', 'lists', 'tables'].includes(table_name)) {
    let look = $('<button>').text('Look');

    look.attr({
      'id': 'look-' + id,
      'class': 'btn btn-outline btn-sm',
      'type': 'submit',
    });

    look.id = 'look-' + id
    bindButton(table_name, look)

    return {'update': update, 'delete_': delete_, 'look': look}
  } else {
    return {'update': update, 'delete_': delete_}
  };
}

export function createCreationButton (table_name) {
  let tr = $('<tr>').attr('id', 'create_btn_row')
  let td = $('<td>').addClass('btn_cell');
  td.attr({
    'id': 'create_btn_cell',
    'colspan': $('th').length,
  })

  let btn = $('<button>').text('Create');
  btn.attr({
    'id': table_name + '_creation',
    'class': 'btn btn-outline btn-sm create_btn',
    'type': 'submit',
  })

  $(td).append(btn);
  $(tr).append(td);
  $('tfoot').append(tr);

  let create_btn = $('#' + table_name + '_creation');
  create_btn.id = table_name + '_creation';
  bindButton(table_name, create_btn);
}

export function createConfirmButtons (createFunc, updateFunc, id, table_name) {
  let accept = $('<button>').addClass('btn btn-outline btn-sm');
  let cancel = $('<button>').addClass('btn btn-outline btn-sm');

  accept.text('Accept');
  cancel.text('Cancel');

  if (id) {
    accept.click({'id': id}, updateFunc);
    cancel.click(function () {
      $('#form_tr').remove();
    });
  } else {
    accept.click(createFunc);
    cancel.click(function () {
      $('#form_tr').remove();
      createCreationButton(table_name)
    });
  }
  return {'accept': accept, 'cancel': cancel}
}

export function createPageIdSelect () {
  var id_select = $('<select>');
  $.getJSON($SCRIPT_ROOT + '/admin/get_pages_ids/', {
    }, function(data) {
    id_select.attr({
      'class': 'form-control admin-select',
      'id': 'id_select',
      'name': 'id_select',
    });
    var option;
    for (var idx = 0; idx < data.result.length; idx++) {
      option = $('<option>').text(data.result[idx]);
      if (idx === 0) {
        option.attr('selected', 'selected');
      };
      id_select.append(option);
    };
  })
  return id_select
}

export function createPageIndexInput () {
  let index_input = $('<input>');
  index_input.attr({
    'class': 'form-control admin-input',
    'id': 'page_index',
    'name': 'page_index',
    'placeholder': 'Enter page index',
    'autocomplete': 'off',
  });
  return index_input
}

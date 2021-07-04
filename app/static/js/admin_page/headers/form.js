import {createConfirmButtons, createPageIdSelect, createPageIndexInput} from '../common_functions.js';
import {createHeader, updateHeader} from './c_ud.js';


export function renderHeaderForm (event) {
  $('#form_tr').remove();

  if (event.data) {
    let header_id = event.data.id
    let form_tr = createForm(header_id);
    form_tr = fillForm(form_tr, header_id);
//    let form_tr = $.when(createForm(header_id)).done(fillForm($('#form_tr'), header_id));

    let tr = $('tr#' + header_id);
    $(tr).after(form_tr);
  } else {
    let form_tr = createForm();

    $('#create_btn_cell').remove();
    let tr = $('#create_btn_row');
    $(tr).replaceWith($(form_tr))
  };
}

function createForm (header_id) {
  let form_tr = $('<tr>');
  let td = $('<td>');
  let tag_label = $('<label>').text("Header tag");
  let tag_select = $('<select>');
  let content_label = $('<label>').text('Content');
  let content_input = $('<input>');
  let index_label = $('<label>').text('Page index');
  let index_input = createPageIndexInput()
  let id_label = $('<label>').text("Page id");
  let id_select = createPageIdSelect()
  let buttons = createConfirmButtons(
    createHeader, updateHeader, header_id, 'headers'
  );
  let accept = buttons.accept;
  let cancel = buttons.cancel;

  form_tr.attr({
    'id': 'form_tr',
  });
  td.attr({
    'class': 'btn_cell',
    'colspan': '6',
  });
  tag_select.attr({
    'id': 'tag_select',
    'name': 'tag_select',
    'class': 'form-control admin-select',
  })
  var option
  let tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6'];
  for (var idx = 0; idx < tags.length; idx++) {
    option = $('<option>').text(tags[idx])
    if (idx === 0) {
        option.attr('selected', 'selected');
    };
    $(tag_select).append(option)
  };
  content_input.attr({
    'id': 'content',
    'name': 'content',
    'class': 'form-control admin-input',
    'placeholder': 'Enter header content',
    'autocomplete': 'off',
  });
  td.append(
    tag_label, tag_select, content_label, content_input,
    id_label, id_select, index_label, index_input, accept, cancel
  );
  form_tr.append(td);

  return form_tr
}

function fillForm (form_tr, header_id) {
  let tr = $('tr#' + header_id);

  let tag_value = tr.find('td:eq(1)').text();
  let content_value = tr.find('td:eq(2)').text();
  let id_value = tr.find('td:eq(3)').text();
  let index_value = tr.find('td:eq(4)').text();

  form_tr.find('select#tag_select').val(tag_value).change();
  form_tr.find('select#id_select').val(id_value).change();
//  ПОЧЕМУ-ТО ПРИНЦИПИАЛЬНО НЕ НАХОДИТ id_select
  form_tr.find('#content').val(content_value);
  form_tr.find('#page_index').val(index_value);

  return form_tr
}


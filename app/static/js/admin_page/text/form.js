import {createConfirmButtons, createPageIndexInput, createPageIdSelect} from '../common_functions.js';
import {createText, updateText} from './crud.js';


export function renderTextForm (event) {
  if ($('.text_tr').length) {
    $('.text_tr').remove()
  }
  $('#form_tr').remove();

  if (event.data) {
    let text_id = event.data.id
    let form_tr = createForm(text_id);
    form_tr = fillForm(form_tr, text_id);

    let tr = $('tr#' + text_id);
    $(tr).after(form_tr);
  } else {
    let form_tr = createForm();

    $('#create_btn_cell').remove();
    let tr = $('#create_btn_row');
    $(tr).replaceWith($(form_tr))
  };
};

function createForm (text_id) {
  let form_tr = $('<tr>');
  let td = $('<td>');
  let content_label = $('<label>').text("Content");
  let textarea = $('<textarea>');
  let index_label = $('<label>').text("Page index");
  let index_input = createPageIndexInput()
  let buttons = createConfirmButtons(createText, updateText, text_id, 'text');
  let accept = buttons.accept;
  let cancel = buttons.cancel;
  let id_label = $('<label>').text("Page id");
  let id_select = createPageIdSelect()
  form_tr.attr({
    'id': 'form_tr',
    'class': 'text-form',
  });
  td.attr({
    'class': 'btn_cell',
    'colspan': '4',
  });
  textarea.attr({
    'id': 'content',
    'name': 'content',
    'class': 'form-control admin-textarea',
    'style': 'overflow-y:hidden;',
    'placeholder': 'Enter text content',
    'autocomplete': 'off',
    'rows': 4,
  });
  textarea.on('input', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
  });

  let div0 = $('<div>').addClass('row')
  let div1 = $('<div>').addClass('row form-cols')
  let div2 = $('<div>').addClass('row')

  let div3 = $('<div>').addClass('col')
  let div4 = $('<div>').addClass('col')
  let div5 = $('<div>').addClass('col')
  let div6 = $('<div>').addClass('col')

  div3.append(content_label, textarea)
  div0.append(div3)

  div4.append(id_label, id_select)
  div5.append(index_label, index_input)
  div1.append(div4, div5)

  div6.append(accept, cancel)
  div2.append(div6)

  td.append(div0, div1, div2)
  form_tr.append(td);

  return form_tr
}

function fillForm (form_tr, text_id) {
  let tr = $('tr#' + text_id);
  let id_value = tr.find('td:eq(1)').text();
  let index_value = tr.find('td:eq(2)').text();
  let textarea = form_tr.find('.admin-textarea')

  fillContentTextarea(textarea, text_id)
  form_tr.find('select#id_select').val(id_value).change();
  form_tr.find('#page_index').val(index_value);

  return form_tr
//  return $.parseHTML(html)
}

function fillContentTextarea (textarea, text_id) {
  $.getJSON($SCRIPT_ROOT + '/admin/get_one_text/' + text_id, {
  }, function(data) {
    textarea.val(data.result[1]);
  });

  return textarea
}
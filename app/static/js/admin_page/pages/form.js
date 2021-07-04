import {createConfirmButtons} from '../common_functions.js';
import {createPage, updatePage} from './c_ud.js';


export function renderPageForm (event) {
  $('#form_tr').remove();

  if (event.data) {
    let page_id = event.data.id
    let form_tr = createForm(page_id);
    form_tr = fillForm(form_tr, page_id);

    let tr = $('tr#' + page_id);
    $(tr).after(form_tr);
  } else {
    let form_tr = createForm();

    $('#create_btn_cell').remove();
    let tr = $('#create_btn_row');
    $(tr).replaceWith($(form_tr));
  };
}

function createForm (page_id) {
  let form_tr = $('<tr>');
  let td = $('<td>');
  let label = $('<label>').text('Page name');
  let input = $('<input>');

  let buttons = createConfirmButtons(
    createPage, updatePage, page_id, 'pages'
  );
  let accept = buttons.accept;
  let cancel = buttons.cancel;

  form_tr.attr({
    'id': 'form_tr',
  });
  td.attr({
    'class': 'btn_cell',
    'colspan': '3',
  });
  input.attr({
    'id': 'page_name',
    'name': 'page_name',
    'class': 'form-control admin-input',
    'placeholder': 'Enter page name',
    'autocomplete': 'off',
  });

  td.append(label, input, accept, cancel);
  form_tr.append(td);

  return form_tr
}

function fillForm (form_tr, page_id) {
  let tr = $('tr#' + page_id);
  let input_value = tr.find('td:eq(1)').text();
  form_tr.find('#page_name').val(input_value)

  return form_tr
}

import {createConfirmButtons, createPageIdSelect, createPageIndexInput} from '../common_functions.js';
import {createTable, updateTable} from './crud.js';


export function renderTableForm (event) {
  if ($('.table_tr').length) {
    $('.table_tr').remove()
  }
  $('#form_tr').remove();

  if (event.data) {
    let table_id = event.data.id;
    let form_tr = createForm(table_id);
    form_tr = fillForm(form_tr, table_id);

    let tr = $('tr#' + table_id);
    $(tr).after(form_tr);
  } else {
    let form_tr = createForm();

    $('#create_btn_cell').remove();
    let tr = $('#create_btn_row');
    $(tr).replaceWith($(form_tr))
  };
}


function createForm (table_id) {
  let form_tr = $('<tr>');
  let td = $('<td>');
  let content_label = $('<label>').text('Content');
  let table = $('<table>')
  let index_label = $('<label>').text('Page index');
  let index_input = createPageIndexInput()

  let buttons = createConfirmButtons(createTable, updateTable, table_id, 'tables');
  let accept = buttons.accept;
  let cancel = buttons.cancel;

  let id_label = $('<label>').text('Page id');
  let id_select = createPageIdSelect()

  let colspan_label = $('<label>').text('Td colspan:')
  let colspan_input = $('<input>');
  let rowspan_label = $('<label>').text('Td rowspan:')
  let rowspan_input = $('<input>');

  let form_check_div = $('<div>');
  let checkbox = $('<input>');
  let checkbox_label = $('<label>').text('Add "thead" class');

  let add_row = $('<button>').text('Add row');

  let delete_row = $('<button>').text('Delete row');
  let add_column = $('<button>').text('Add column');
  let delete_column = $('<button>').text('Delete column');

  form_tr.attr({
    'id': 'form_tr',
    'class': 'table-tr',
  });
  td.attr({
    'class': 'btn_cell',
    'colspan': '6',
  });
  table.attr({
    'id': 'table-' + table_id,
    'class': 'table_main table_look pos_relative',
  })

  if (table_id) {
    var tr = $('tr#' + table_id);
    var rows = tr.find('td:eq(1)').text();
    var cols = tr.find('td:eq(2)').text();
  } else {
    var rows = 4;
    var cols = 4;
  }

  for (var row = 0; row < rows; row++) {
    let table_tr = $('<tr>')
    for (var col = 0; col < cols; col++) {
      let td = $('<td>')
      td.attr('id', 'td_' + row + '-' + col)

//      if (row === 0) {
//        td.addClass('thead')
//      }

      td.click(selectTd);
      td.dblclick(changeTd);

      table_tr.append(td)
    }
    table.append(table_tr)
  }

  colspan_input.attr({
    'id': 'colspan',
    'name': 'colspan',
    'class': 'form-control admin-input',
    'value': '-',
    'placeholder': 'Enter td colspan',
    'autocomplete': 'off',
  });
  rowspan_input.attr({
    'id': 'rowspan',
    'name': 'rowspan',
    'class': 'form-control admin-input',
    'value': '-',
    'placeholder': 'Enter td rowspan',
    'autocomplete': 'off',
  });
  form_check_div.attr({
    'class': 'form-check',
  })
  checkbox.attr({
    'id': 'thead',
    'type': 'checkbox',
    'class': 'form-check-input',
  });
  checkbox_label.attr({
    'class': 'form-check-label',
    'for': 'thead',
  });

  form_check_div.append(checkbox, checkbox_label)

  add_row.attr({
    'id': 'table_add_row',
    'class': 'btn btn-outline btn-sm create_btn',
    'type': 'submit',
  })
  delete_row.attr({
    'id': 'table_delete_row',
    'class': 'btn btn-outline btn-sm create_btn',
    'type': 'submit',
  })
  add_column.attr({
    'id': 'table_add_column',
    'class': 'btn btn-outline btn-sm create_btn',
    'type': 'submit',
  })
  delete_column.attr({
    'id': 'table_delete_column',
    'class': 'btn btn-outline btn-sm create_btn',
    'type': 'submit',
  })

  add_row.click(addRow);
  delete_row.click(deleteRow)
  add_column.click(addColumn)
  delete_column.click(deleteColumn)

  let single_col_row = $('<div>').addClass('row')
  let spans_row = $('<div>').addClass('row spans_row')
  let row_col_row = $('<div>').addClass('row')
  let di_col_row = $('<div>').addClass('row').addClass('reduced_width')
  let confirm_row = $('<div>').addClass('row')
  col = $('<div>').addClass('col')
  let left_col = $('<div>').addClass('col')
  let right_col = $('<div>').addClass('col')
  let confirm_col = $('<div>').addClass('col')
  let row_col_col = $('<div>').addClass('col')

  col.append(content_label, table)
  single_col_row.append(col)

  spans_row.append(colspan_label, colspan_input, rowspan_label, rowspan_input, form_check_div)
  row_col_col.append(add_row, delete_row, add_column, delete_column)
  row_col_row.append(row_col_col)

  left_col.append(id_label, id_select)
  right_col.append(index_label, index_input)
  di_col_row.append(left_col, right_col)

  confirm_col.append(accept, cancel)
  confirm_row.append(confirm_col)

  td.append(single_col_row, spans_row, row_col_row, di_col_row, confirm_row)

  for (var row = 0; row < rows; row++) {
    for (var col = 0; col < cols; col++) {
      let form_td = $(table).find('#td_' + row + '-' + col)
      form_td.text('Pass td value')
    }
  }

  form_tr.append(td);

  return form_tr
}

function fillForm (form_tr, table_id) {
  let tr = $('tr#' + table_id);
  let rows = tr.find('td:eq(1)').text();
  let cols = tr.find('td:eq(2)').text();
  let id_value = tr.find('td:eq(3)').text();
  let index_value = tr.find('td:eq(4)').text();

  fillTable(form_tr, table_id)
  form_tr.find('select#id_select').val(id_value).change();
  form_tr.find('#page_index').val(index_value);

  return form_tr
}

function fillTable (form_tr, table_id) {
  $.getJSON($SCRIPT_ROOT + '/admin/get_table/' + table_id, {
    }, function(data) {
      let table_content = data.result[1];
      let rows = data.result[2];
      let cols = data.result[3];
      let table = form_tr.find('#table-' + table_id)
      let last_span = ''
      let span_offset = 0
      for (var row = 0; row < rows; row++) {
        for (var col = 0; col < cols; col++) {
          let td = $(table).find('#td_' + row + '-' + col)
          if (!(table_content[row][col])) {
            td.hide()
          } else {
            td.text(table_content[row][col].value)

            if (table_content[row][col].colspan) {
              td.attr('colspan', table_content[row][col].colspan)
            }
            if (table_content[row][col].rowspan) {
              td.attr('rowspan', table_content[row][col].rowspan)
            }
            if (table_content[row][col].thead) {
              td.addClass('thead')
            }
          }
        }
      }
  });
}

function addRow () {
  let rows = $('.table_main').find('tr').length;
  let cols = 0;
  let tr
  for (let row = 1; row < rows + 1; row++) {
    tr = $('.table_main tr:nth-child(' + row + ')');
    if ($(tr).find('td').length > cols) {
      cols = tr.find('td').length;
    };
  };

  tr = $('<tr>')
  let td
  for (let col = 0; col < cols; col++) {
    td = $('<td>')
    td.attr('id', 'td_' + (rows + 1) + '-' + col)
    td.text('Pass td value')
    td.click(selectTd);
    td.dblclick(changeTd);
    tr.append(td)
  }
  $('.table_main').append(tr)
}

function deleteRow () {
  if ($('.table_main').find('tr').length > 1) {
    $('.table_main').find('tr').last().remove()
  }
}

function addColumn () {
  let rows = $('.table_main').find('tr').length;
  let tr
  for (let row = 1; row < rows + 1; row++) {
    tr = $('.table_main tr:nth-child(' + row + ')');
    let col = tr.find('td').length
    let td = $('<td>')
    td.attr('id', 'td_' + (row - 1) + '-' + col)
    td.text('Pass td value')
    td.click(selectTd);
    td.dblclick(changeTd);

    tr.append(td)
  };
}

function deleteColumn () {
  let rows = $('.table_main').find('tr').length;
  let tr
  for (let row = 1; row < rows + 1; row++) {
    tr = $('.table_main tr:nth-child(' + row + ')');
    if (tr.find('td').length > 1) {
      tr.find('td').last().remove()
    }
  };
}

function selectTd () {
  let td = $('.table_main').find('#' + this.id);
  let colspan = (td.attr('colspan')) ? td.attr('colspan') : 1
  let rowspan = (td.attr('rowspan')) ? td.attr('rowspan') : 1
  let thead = (td.attr('class')) ? td.attr('class').split(' ').includes('thead') : false

  $('#colspan').val(colspan)
  $('#rowspan').val(rowspan)

  if ((td.attr('class')) && td.attr('class').split(' ').includes('thead')) {
    $('#thead').attr('checked', 'checked')
    $('#thead').prop('checked', true)
  } else {
    $('#thead').removeAttr('checked')
    $('#thead').prop('checked', false)
  }

  $('#colspan').unbind()
  $('#colspan').on('input', function (event) { changeTdColspan(event, td) })
  $('#rowspan').unbind()
  $('#rowspan').on('input', function (event) { changeTdRowspan(event, td) })

  $('#thead').unbind()
  $('#thead').change(function (event) { TheadCheckboxChanging(event, td) })
}

function changeTdColspan (event, td) {
  span = Number($('#colspan').val())
  let row = Number(td.attr('id').split('_')[1].split('-')[0])
  let col = Number(td.attr('id').split('-')[1])
  if (span > 0) {
    for (var i = Number(col) + 1; i < col + span; i++) {
      $('#td_' + row + '-' + i).addClass('spanned_by_' + row + '-' + col)
      $('#td_' + row + '-' + i).hide()
    }
  } else {
    $('.spanned_by_' + row + '-' + col).show()
    $('.spanned_by_' + row + '-' + col).removeClass('spanned_by_' + row + '-' + col)
  }
  td.attr('colspan', span)
}

function changeTdRowspan (event, td) {
  span = Number($('#rowspan').val())
  let row = Number(td.attr('id').split('_')[1].split('-')[0])
  let col = Number(td.attr('id').split('-')[1])

  if (span > 0) {
    for (var i = Number(row) + 1; i < row + span; i++) {
      $('#td_' + i + '-' + col).addClass('spanned_by_' + row + '-' + col)
      $('#td_' + i + '-' + col).hide()
    }
  } else {
    $('.spanned_by_' + row + '-' + col).show()
    $('.spanned_by_' + row + '-' + col).removeClass('spanned_by_' + row + '-' + col)
  }
  td.attr('rowspan', span)
}

function TheadCheckboxChanging (event, td) {
  if ($('#thead').attr('checked')) {
    ($('#thead').attr('checked', false))
  } else {
    ($('#thead').attr('checked', true))
  }

  if ($('#thead').attr('checked')) {
    td.addClass('thead')
  } else {
    td.removeClass('thead')
  }
}

function changeTd () {
  let td = $('.table_main').find('#' + this.id)
  if (!(td.find('textarea').length)) {
    let textarea = $('<textarea>').addClass('admin-textarea table-textarea');
    textarea.val(td.text())
    textarea.attr(
      'style',
      'height:' + (td.css('height')) + '; overflow-y: hidden; width:' + (td.css('width')) + ';'
    );

    let start_height = Number(JSON.parse(JSON.stringify(td.css('height').replace('px', ''))));
    textarea.on('input', function () {
      if (this.scrollHeight > start_height) {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
      }
      if (textarea.val().includes('  ')) {
        textarea.val(textarea.val().replace('  ', ' '``))
      }
    });
    td.text('');
    td.append(textarea);
    $('textarea').focus()
    $('textarea').focusout(function () {
      $('textarea').parent().text($('textarea').val())
      $('textarea').remove()
    })
  }
}

import {createActionsButtons, createCreationButton} from './common_functions.js';


function buildTable(rows, cols) {
  let table = $('<table>').addClass('table table_admin');
  let thead = $('<thead>');
  let tbody = $('<tbody>');
  let tfoot = $('<tfoot>');

  let tr = $('<tr>');
  for (var col = 0; col < cols; col++) {
    let id = '0-' + col;
    let th = $('<th>').attr('id', id);
    $(tr).append(th);
  }
  $(thead).append(tr);

  for (var row = 1; row < rows; row++) {
    let tr = $('<tr>');
    for (var col = 0; col < cols; col++) {
      let id = row + '-' + col;
      let td = $('<td>').attr('id', id);
      $(tr).append(td);
    }
    $(tbody).append(tr);
  }

  $(table).append(thead);
  $(table).append(tbody);
  $(table).append(tfoot);

  $(table).find('#0-0').addClass('id_col');
//  $(table).find('[id$="-2"]').addClass('btn_cell');
//  $(table).find('#0-2').attr('class', 'btn_col');
  $(table).find('[id$="-' + (cols - 1) + '"]').addClass('btn_cell');
  $(table).find('#0-' + (cols - 1)).attr('class', 'btn_col');

  return table;
}

function fillTable (table, data, table_name) {
  let rows = data.length
  let cols = data[0].length

  for (var col = 0; col < cols; col++) {
    $(table).find('#0-' + col).text(data[0][col])
  }

  for (var row = 1; row < rows; row++) {
    for (var col = 0; col < cols; col++) {
      let td = $(table).find('#' + row + '-' + col)
      td.text(data[row][col])
      td.parent().attr('id', data[row][0])

      if (col === cols - 1) {
        let buttons = createActionsButtons(table_name, data[row][0])
        let update = buttons.update;
        let delete_ = buttons.delete_;
        if (buttons.look) {
          let look = buttons.look
          td.append(look, update, delete_)
        } else {
          td.append(update, delete_)
        }
      }
    }
  }
  return table
}

function renderSection (table_name, table_data) {
  let empty_table = buildTable(table_data.length, table_data[0].length);
  let table = fillTable(empty_table, table_data, table_name)

  $('.table_admin').remove();
  $('#here_table').append(table);
  createCreationButton(table_name);
}

function getData (event) {
  $.getJSON($SCRIPT_ROOT + '/admin' + event.data.url, {
  }, function(data) {
    data = JSON.parse(data.result);
    renderSection(data.table_name, data.table_data)
  });
};

$(function () {
  $('a#get_pages').click({'url': "/get_pages"}, getData);
  $('a#get_headers').click({'url': "/get_headers"}, getData);
  $('a#get_text').click({'url': "/get_text"}, getData);
  $('a#get_lists').click({'url': "/get_lists"}, getData);
  $('a#get_tables').click({'url': "/get_tables"}, getData);
});

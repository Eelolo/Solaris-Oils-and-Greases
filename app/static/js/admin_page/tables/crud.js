import {createCreationButton, createActionsButtons} from '../common_functions.js'


export function renderTable (event) {
  if ($('#form_tr').length) {
    $('#form_tr').remove()
    createCreationButton('tables')
  };

  let table_id = event.data.id;

  if ($('.table_tr').length) {
    if ($('#table-' + table_id).length) {
      $('.table_tr').remove();
      return
    } else {
      $('.table_tr').remove();
    }
  };

  let curr_tr = $('tr#' + table_id);
  let table_tr = $('<tr>').addClass('table_tr');
  let table_td = $('<td>').attr('colspan', '6');

  $.getJSON($SCRIPT_ROOT + '/admin/get_table/' + table_id, {
  }, function(data) {
    let table_content = data.result[1]
    let rows = data.result[2]
    let cols = data.result[3]
    let table = $('<table>').addClass('table_main table_look')
    table.attr('id', 'table-' + table_id)
    for (var row = 0; row < rows; row++) {
      let tr = $('<tr>')
      if (row === 0) {
        tr.addClass('thead')
      }
      for (var col = 0; col < cols; col++) {
        if (!(table_content[row][col])) {
          break;
        }
        let td = $('<td>').text(table_content[row][col].value)
        if (table_content[row][col].colspan) {
          td.attr('colspan', table_content[row][col].colspan)
        }
        if (table_content[row][col].rowspan) {
          td.attr('rowspan', table_content[row][col].rowspan)
        }
        tr.append(td)
      }
      table.append(tr)
    }
    table_td.append(table)
    table_tr.append(table_td)
    });
    $(curr_tr).after(table_tr);
  };

export function parseTableFromForm () {
  let table = $('.table_main');
  let prev_tr = table.parent().parent().parent().parent().prev()

  if (!(prev_tr.length)) {
    var rows = 4
    var cols = 4
  } else {
    var rows = prev_tr.contents()[1].innerHTML;
    var cols = prev_tr.contents()[2].innerHTML;
  }

  var table_content = []
  for (var row = 0; row < rows; row++) {
    table_content.push([]);
    for (var col = 0; col < cols; col++) {
      let td = $('#td_' + row + '-' + col);
      if (td.text()) {
        table_content[row].push({value: td.text()})

        if (td.hasClass('thead')) {
          table_content[row][col].thead = true
        }
      };
    };
  };
  return table_content
};

export function createTable () {
  let content = JSON.stringify(parseTableFromForm());
  let page_id = $('select[name="id_select"]').val();
  let page_index = $('input[name="page_index"]').val();

  $.getJSON($SCRIPT_ROOT + '/admin/create_table/', {
    'content': content,
    'page_id': page_id,
    'page_index': page_index,
  }, function(data) {
    $('#form_tr').remove();
    createCreationButton('tables');

    let table_id = data.result[0];
    let tr = $('<tr>');
    tr.attr('id', table_id);

    let td0 = $('<td>').text(data.result[0]);
    let td1 = $('<td>').text(data.result[2]);
    let td2 = $('<td>').text(data.result[3]);
    let td3 = $('<td>').text(data.result[4]);
    let td4 = $('<td>').text(data.result[5]);

    let td5 = $('<td>').addClass('btn_cell');
    let buttons = createActionsButtons('tables', data.result[0]);
    let look = buttons.look;
    let update = buttons.update;
    let delete_ = buttons.delete_;
    $(td5).append(look, update, delete_);

    $(tr).append(td0, td1, td2, td3, td4, td5);
    $('.table_admin').append(tr.hide());
    $(tr).fadeIn('slow');
  });
}

export function updateTable (event) {
  let table_id = event.data.id;
  let content = parseTableFromForm();
  let rows = content.length
  let cols = content[0].length - 1
  let page_id = $('select[name="id_select"]').val();
  let page_index = $('input[name="page_index"]').val();
  $.getJSON($SCRIPT_ROOT + '/admin/update_table/' + table_id + '/', {
    'content': JSON.stringify(content),
    'page_id': page_id,
    'page_index': page_index,
  });

  let tr = $('tr#' + table_id);
  $(tr).fadeOut('fast', function () {
    tr.contents()[1].innerHTML = content.length;
    tr.contents()[2].innerHTML = content[3].length;
    tr.contents()[3].innerHTML = page_id;
    tr.contents()[4].innerHTML = page_index;
  });
  $(tr).fadeIn('slow');
  $('#form_tr').remove();
}

export function deleteTable (event) {
  let table_id = event.data.id;
  $.getJSON($SCRIPT_ROOT + '/admin/delete_table/' + table_id + '/', {});

  let tr = $('tr#' + table_id);
  $(tr).fadeOut('slow', function () {
    tr.remove()
  });
}

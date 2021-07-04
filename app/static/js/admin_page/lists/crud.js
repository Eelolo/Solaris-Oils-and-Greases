import {createCreationButton, createActionsButtons} from '../common_functions.js'


export function renderList (event) {
  if ($('#form_tr').length) {
    $('#form_tr').remove()
    createCreationButton('lists')
  };

  let list_id = event.data.id;

  if ($('.list_tr').length) {
    if ($('#list-' + list_id).length) {
      $('.list_tr').remove();
      return
    } else {
      $('.list_tr').remove();
    }
  };

  let tr = $('tr#' + list_id);
  let list_tr = $('<tr>').addClass('list_tr');
  let td = $('<td>');

  $.getJSON($SCRIPT_ROOT + '/admin/get_list/' + list_id, {
  }, function(data) {
    let label = $('<label>').text(data.result[1]);
    let list = data.result[2];
    let ul = $('<ul>').addClass('list-admin');
    let li;
    for (var row = 0; row < data.result[2].length; row++) {
      li = $('<li>').text(list[row]);
      ul.append(li);
    };
    td.append(label, ul);
    td.attr({
      'id': 'list-' + list_id,
      'colspan': data.result.length + 1,
    });
    list_tr.append(td);
  });
  $(tr).after(list_tr);
};

function parseListFromForm () {
  let list_label = $('#list_label').text()

  var listItems = $(".admin-list li");
  var listContent = [list_label]
  listItems.each(function(idx, li) {
    listContent.push($(li).text())
  });

  return listContent
}

export function createList () {
  let content = JSON.stringify(parseListFromForm());
  let page_id = $('select[name="id_select"]').val();
  let page_index = $('input[name="page_index"]').val();
  $.getJSON($SCRIPT_ROOT + '/admin/create_list/', {
    'content': content,
    'page_id': page_id,
    'page_index': page_index,
  }, function(data) {
    $('#form_tr').remove();
    createCreationButton('lists');

    let list_id = data.result[0];
    let tr = $('<tr>');
    tr.attr('id', list_id);

    let td0 = $('<td>').text(data.result[0]);
    let td1 = $('<td>').text(data.result[1]);
    let td2 = $('<td>').text(data.result[3]);
    let td3 = $('<td>').text(data.result[4]);
    let td4 = $('<td>').text(data.result[5]);

    let td5 = $('<td>').addClass('btn_cell');
    let buttons = createActionsButtons('lists', data.result[0]);
    let look = buttons.look;
    let update = buttons.update;
    let delete_ = buttons.delete_;
    $(td5).append(look, update, delete_);

    $(tr).append(td0, td1, td2, td3, td4, td5);
    $('.table_admin').append(tr.hide());
    $(tr).fadeIn('slow');
  });
}

export function updateList (event) {
  let list_id = event.data.id;

  let content = parseListFromForm();
  let page_id = $('select[name="id_select"]').val();
  let page_index = $('input[name="page_index"]').val();
  $.getJSON($SCRIPT_ROOT + '/admin/update_list/' + list_id + '/', {
    'content': JSON.stringify(content),
    'page_id': page_id,
    'page_index': page_index,
  });

  let tr = $('tr#' + list_id);
  $(tr).fadeOut('fast', function () {
    tr.contents()[1].innerHTML = content[0];
    tr.contents()[2].innerHTML = content.length - 1;
    tr.contents()[3].innerHTML = page_id;
    tr.contents()[4].innerHTML = page_index;
  });
  $(tr).fadeIn('slow');
  $('#form_tr').remove();
}

export function deleteList (event) {
  let list_id = event.data.id;
  $.getJSON($SCRIPT_ROOT + '/admin/delete_list/' + list_id + '/', {});

  let tr = $('tr#' + list_id);
  $(tr).fadeOut('slow', function () {
    tr.remove()
  });
}
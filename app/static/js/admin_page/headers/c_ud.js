import {createCreationButton, createActionsButtons} from '../common_functions.js'


export function createHeader () {
  let tag = $('select[name="tag_select"]').val();
  let content = $('input[name="content"]').val();
  let page_id = $('select[name="id_select"]').val();
  let page_index = $('input[name="page_index"]').val();
  $.getJSON($SCRIPT_ROOT + '/admin/create_header/', {
    'tag': tag,
    'content': content,
    'page_id': page_id,
    'page_index': page_index,
  }, function(data) {
    $('#form_tr').remove();
    createCreationButton('headers');

    let header_id = data.result[0];
    let tr = $('<tr>');
    tr.attr('id', header_id);

    let td0 = $('<td>').text(data.result[0]);
    let td1 = $('<td>').text(data.result[1]);
    let td2 = $('<td>').text(data.result[2]);
    let td3 = $('<td>').text(data.result[3]);
    let td4 = $('<td>').text(data.result[4]);

    let td5 = $('<td>').addClass('btn_cell');
    let buttons = createActionsButtons('headers', data.result[0]);
    let update = buttons.update;
    let delete_ = buttons.delete_;
    $(td5).append(update, delete_);

    $(tr).append(td0, td1, td2, td3, td4, td5);
    $('.table_admin').append(tr.hide());
    $(tr).fadeIn('slow');
  });
};

export function updateHeader (event) {
  let header_id = event.data.id;
  let tag = $('select[name="tag_select"]').val();
  let content = $('input[name="content"]').val();
  let page_id = $('select[name="id_select"]').val();
  let page_index = $('input[name="page_index"]').val();
  $.getJSON($SCRIPT_ROOT + '/admin/update_header/' + header_id + '/', {
    'tag': tag,
    'content': content,
    'page_id': page_id,
    'page_index': page_index,
  });

  let tr = $('tr#' + header_id);
  $(tr).fadeOut('fast', function () {
    tr.contents()[1].innerHTML = tag;
    tr.contents()[2].innerHTML = content;
    tr.contents()[3].innerHTML = page_id;
    tr.contents()[4].innerHTML = page_index;
  });
  $(tr).fadeIn('slow');
  $('#form_tr').remove();
};

export function deleteHeader (event) {
  let header_id = event.data.id;
  $.getJSON($SCRIPT_ROOT + '/admin/delete_header/' + header_id + '/', {
  });

  let tr = $('tr#' + header_id);
  $(tr).fadeOut('slow', function () {
    tr.remove()
  });
};

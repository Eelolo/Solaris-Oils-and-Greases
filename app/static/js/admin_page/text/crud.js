import {createCreationButton, createActionsButtons} from '../common_functions.js'


export function renderText (event) {
  if ($('#form_tr').length) {
    $('#form_tr').remove()
    createCreationButton('text')
  };

  let text_id = event.data.id;

  if ($('.text_tr').length) {
    if ($('#text-' + text_id).length) {
      $('.text_tr').remove();
      return
    } else {
      $('.text_tr').remove();
    }
  };

  let tr = $('tr#' + text_id);
  let text_tr = $('<tr>').addClass('text_tr');
  let td = $('<td>');

  $.getJSON($SCRIPT_ROOT + '/admin/get_one_text/' + text_id, {
  }, function(data) {
    let text = data.result[1];
    td.text(text);
    td.attr({
      'id': 'text-' + text_id,
      'colspan': data.result.length,
    });
    text_tr.append(td);
  });
  $(tr).after(text_tr);
};


export function createText () {
  let content = $('textarea[name="content"]').val();
  let page_id = $('select[name="id_select"]').val();
  let page_index = $('input[name="page_index"]').val();
  $.getJSON($SCRIPT_ROOT + '/admin/create_text/', {
    'content': content,
    'page_id': page_id,
    'page_index': page_index,
  }, function(data) {
    $('#form_tr').remove();
    createCreationButton('text');

    let text_id = data.result[0];
    let tr = $('<tr>');
    tr.attr('id', text_id);

    let td0 = $('<td>').text(data.result[0]);
    let td1 = $('<td>').text(data.result[2]);
    let td2 = $('<td>').text(data.result[3]);

    let td3 = $('<td>').addClass('btn_cell');
    let buttons = createActionsButtons('text', data.result[0]);
    let look = buttons.look;
    let update = buttons.update;
    let delete_ = buttons.delete_;
    $(td3).append(look, update, delete_);

    $(tr).append(td0, td1, td2, td3);
    $('.table_admin').append(tr.hide());
    $(tr).fadeIn('slow');
  });
}

export function updateText (event) {
  let text_id = event.data.id;
  let content = $('textarea[name="content"]').val();
  let page_id = $('select[name="id_select"]').val();
  let page_index = $('input[name="page_index"]').val();
  $.getJSON($SCRIPT_ROOT + '/admin/update_text/' + text_id + '/', {
    'content': content,
    'page_id': page_id,
    'page_index': page_index,
  });

  let tr = $('tr#' + text_id);
  $(tr).fadeOut('fast', function () {
    tr.contents()[1].innerHTML = page_id;
    tr.contents()[2].innerHTML = page_index;
  });
  $(tr).fadeIn('slow');
  $('#form_tr').remove();
}

export function deleteText (event) {
  let text_id = event.data.id;
  $.getJSON($SCRIPT_ROOT + '/admin/delete_text/' + text_id + '/', {
  });

  let tr = $('tr#' + text_id);
  $(tr).fadeOut('slow', function () {
    tr.remove()
  });
}

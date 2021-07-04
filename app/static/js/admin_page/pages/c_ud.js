import {createCreationButton, createActionsButtons} from '../common_functions.js'


export function createPage () {
  let page_name = $('input[name="page_name"]').val();
  $.getJSON($SCRIPT_ROOT + '/admin/create_page/', {
    page_name: page_name
  }, function(data) {
    $('#form_tr').remove();
    createCreationButton('pages');

    let page_id = data.result[0];
    let tr = $('<tr>');
    tr.attr('id', page_id);

    let td0 = $('<td>').text(data.result[0]);
    let td1 = $('<td>').text(data.result[1]);

    let td2 = $('<td>').addClass('btn_cell');
    let buttons = createActionsButtons('pages', data.result[0]);
    let update = buttons.update;
    let delete_ = buttons.delete_;
    $(td2).append(update, delete_);

    $(tr).append(td0, td1, td2);
    $('.table_admin').append(tr.hide());
    $(tr).fadeIn('slow');
  });
};

export function updatePage (event) {
  let page_id = event.data.id;
  let page_name = $('input[name="page_name"]').val()
  $.getJSON($SCRIPT_ROOT + '/admin/update_page/' + page_id + '/', {
      page_name: page_name
  });

  let tr = $('tr#'+page_id)
  $(tr).fadeOut('fast', function () {
    tr.contents()[1].innerHTML = page_name
  });
  $(tr).fadeIn('slow');
  $('#form_tr').remove();
}

export function deletePage (event) {
  let page_id = event.data.id;
  $.getJSON($SCRIPT_ROOT + '/admin/delete_page/' + page_id + '/', {});

  let tr = $('tr#' + page_id)
  $(tr).fadeOut('slow', function () {
    tr.remove()
  });
}

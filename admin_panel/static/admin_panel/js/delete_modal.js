// delete modal that appears when delete buttons are clicked

$('#deleteModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); 
    var itemName = button.data('item-name'); 
    var deleteUrl = button.data('delete-url'); 
    var modal = $(this);
    modal.find('.itemName').text(itemName);
    modal.find('#deleteForm').attr('action', deleteUrl);
  });
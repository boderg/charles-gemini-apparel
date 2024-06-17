$('#deleteModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget) // Button that triggered the modal
    var itemName = button.data('item-name') // Extract info from data-* attributes
    var deleteUrl = button.data('delete-url') // Extract info from data-* attributes
    var modal = $(this)
    modal.find('.itemName').text(itemName)
    modal.find('#deleteForm').attr('action', deleteUrl)
  })
Dropzone.options.dropzoneForm = {
  maxFiles        : 1,
  paramName       : "file",
  uploadMultiple  : false,
  addRemoveLinks  : true,
  removedfile: function(file) {
      var _ref;
      console.log(file.name);
      var server_file = file.name;
      $.post("/delete-file", {deleted: server_file});
      $('.dropzone').addClass('dz-clickable');
      $('.dropzone')[0].addEventListener('click', this.listeners[1].events.click);
      return (_ref = file.previewElement) != null ? _ref.parentNode.removeChild(file.previewElement) : void 0;
    },
  init            : function(){
    dropzoneForm = this;
    this.on('maxfilesreached', function(){
      $('.dropzone').removeClass('dz-clickable');
      $('.dropzone')[0].removeEventListener('click', this.listeners[1].events.click);
    });
    this.on('success', function(file, response){
//console.log(response);
      if(response == 'success'){
        BootstrapDialog.show({
            message: 'Terima Kasih, assessment anda sudah diterima.. :)',
            buttons: [{
              label: 'Close',
                action: function(dialog) {
                  dialog.close();
                }
            }]
        });
      }
      else{
        BootstrapDialog.show({
            message: 'File anda gagal di-upload',
            buttons: [{
              label: 'Close',
                action: function(dialog) {
                  dialog.close();
                }
            }]
        });
      }


    });
  }
}

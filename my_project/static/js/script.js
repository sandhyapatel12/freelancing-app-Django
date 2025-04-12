
//--------------------------------------------------------create_gig.html------------------------------------------------------
// use ckeditor for description   which provide all text funcnality 

document.addEventListener("DOMContentLoaded", function () {
    const descField = document.querySelector('#id_description');
    if (descField) {
      ClassicEditor
        .create(descField, {
          toolbar: [
            'heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', '|',
            'undo', 'redo'
          ]
        })
        .then(editor => {
          const editableElement = editor.ui.view.editable.element;
  
          editableElement.style.backgroundColor = '#1f2937';
          editableElement.style.color = '#ffffff';
          editableElement.style.border = '1px solid #374151';
          editableElement.style.borderRadius = '0.75rem';
          editableElement.style.padding = '1rem';
          editableElement.style.height = '200px';
          editableElement.style.overflowY = 'auto';
          editableElement.style.marginTop = '1.25rem';
  
          const style = document.createElement('style');
          style.innerHTML = `
            .ck.ck-editor__main > .ck-editor__editable {
              background-color: #1f2937 !important;
              color: #ffffff !important;
              height: 200px !important;
              overflow-y: auto !important;
            }
            .ck.ck-editor__editable:focus {
              border-color: #06b6d4 !important;
              box-shadow: 0 0 0 2px #06b6d4 !important;
            }
            .ck.ck-toolbar {
              background-color: #111827 !important;
              border-color: #374151 !important;
            }
            .ck.ck-toolbar .ck-button .ck-icon {
              filter: invert(1);
            }
          `;
          document.head.appendChild(style);
        })
        .catch(error => {
          console.error("CKEditor init failed:", error);
        });
    }
 
//   for  slected image preview
const imageInput = document.getElementById("id_image");
const previewBox = document.getElementById("image-preview");
const previewImg = document.getElementById("preview-img");

  if (imageInput && previewBox && previewImg) {
    imageInput.addEventListener("change", function (event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
          previewImg.src = e.target.result;
          previewBox.classList.remove("hidden");
        };
        reader.readAsDataURL(file);
      } else {
        previewBox.classList.add("hidden");
        previewImg.src = "#";
      }
    });
  }
});
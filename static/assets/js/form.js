// script.js
function previewImage() {
    var input = document.getElementById('inputImage');
    var preview = document.getElementById('previewImage');

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            preview.src = e.target.result;
            preview.style.display = 'block'; // Show the preview image
        };

        reader.readAsDataURL(input.files[0]);
    }
}
function toggleRow(row) {
    var checkbox = row.querySelector('input[type="checkbox"]');
    checkbox.checked = !checkbox.checked;
}
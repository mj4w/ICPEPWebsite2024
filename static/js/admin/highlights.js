const searchBar = document.querySelector('.search-bar');

searchBar.addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    const highlightRows = document.querySelectorAll('.highlight-row');

    highlightRows.forEach(row => {
        const title = row.querySelector('.admin-cell.image span').textContent.toLowerCase();
        if (title.includes(searchTerm)) {
            row.style.display = 'flex';
        } else {
            row.style.display = 'none';
        }
    });
});

document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', function() {
        const highlightID = this.getAttribute('data-user-id');
        deleteHighlight(highlightID);
        this.closest('.products-row').remove();
    });
});


var modal = document.getElementById("update-modal");
var closeButton = modal.querySelector(".close");
function closeModal() {
  modal.style.display = "none";
}
closeButton.addEventListener("click", function() {
  closeModal();
});
window.addEventListener("click", function(event) {
  if (event.target === modal) {
    closeModal();
  }
});
var btn = document.getElementById("open-update");
btn.onclick = function() {
  modal.style.display = "block";
};
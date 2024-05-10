document.querySelectorAll('.approve-btn').forEach(button => {
    button.addEventListener('click', function() {
        const userId = this.getAttribute('data-user-id');
        approveUser(userId);
    });
});

document.querySelectorAll('.reject-btn').forEach(button => {
    button.addEventListener('click', function() {
        const userId = this.getAttribute('data-user-id');
        rejectUser(userId);
    });
});
document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', function() {
        const userId = this.getAttribute('data-user-id');
        deleteUser(userId);
        this.closest('.products-row').remove();
    });
});

function updateStatus(userId, isActive) {
    console.log('Updating status for user:', userId, 'isActive:', isActive);
    const statusElement = document.querySelector(`#user-status-${userId}`);
    console.log('Status element:', statusElement);
    if (statusElement) {
        if (isActive) {
            statusElement.textContent = 'Active';
            statusElement.classList.add('active');
            statusElement.classList.remove('inactive');
        } else {
            statusElement.textContent = 'Not Active';
            statusElement.classList.remove('active');
            statusElement.classList.add('inactive');
        }
    } else {
        console.error('Status element not found');
    }
}
// Search
const searchBar = document.getElementById('search-bar');

searchBar.addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    const userRows = document.querySelectorAll('.user-row');

    userRows.forEach(row => {
        const username = row.querySelector('.admin-cell.image span').textContent.toLowerCase();
        const email = row.querySelector('.admin-cell.category').textContent.toLowerCase();

        if (username.includes(searchTerm) || email.includes(searchTerm)) {
            row.style.display = 'flex';
        } else {
            row.style.display = 'none';
        }
    });
});
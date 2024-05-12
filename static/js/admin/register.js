document.querySelectorAll('.sem-1-add').forEach(button => {
    button.addEventListener('click', function() {
        const userId = this.getAttribute('data-user-id');
        sub_1_add(userId);
    });
});

document.querySelectorAll('.sem-1-remove').forEach(button => {
    button.addEventListener('click', function() {
        const userId = this.getAttribute('data-user-id');
        sub_1_remove(userId);
    });
});

document.querySelectorAll('.sem-2-add').forEach(button => {
    button.addEventListener('click', function() {
        const userId = this.getAttribute('data-user-id');
        sub_2_add(userId);
    });
});

document.querySelectorAll('.sem-2-remove').forEach(button => {
    button.addEventListener('click', function() {
        const userId = this.getAttribute('data-user-id');
        sub_2_remove(userId);
    });
});



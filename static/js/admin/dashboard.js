
var aboutPicModal = document.getElementById("openAboutPicModal");
var bannerModal = document.getElementById("openBannerModal");


var openAboutPicModalBtn = document.getElementById("openAboutPicModalBtn");
var openBannerModalBtn = document.getElementById("openBannerModalBtn");
var closeBtns = document.querySelectorAll(".close");


openAboutPicModalBtn.onclick = function() {
    aboutPicModal.style.display = "block";
}


openBannerModalBtn.onclick = function() {
    bannerModal.style.display = "block";
}

closeBtns.forEach(function(btn) {
    btn.onclick = function() {
        aboutPicModal.style.display = "none";
        bannerModal.style.display = "none";
    }
});

window.onclick = function(event) {
    if (event.target == aboutPicModal || event.target == bannerModal) {
        aboutPicModal.style.display = "none";
        bannerModal.style.display = "none";
    }
}

document.querySelectorAll('.edit-btn').forEach(button => {
    button.addEventListener('click', function() {
        const bannerId = this.getAttribute('data-id');
        openEditModal(bannerId);
    });
});

function openEditModal(bannerId) {
    const editModal = document.getElementById('editModal');
    editModal.style.display = 'block';
    
    const closeBtn = editModal.querySelector('.close');
    
    closeBtn.addEventListener('click', function() {
        editModal.style.display = 'none';
    });
}
document.querySelectorAll('.edit-btn1').forEach(button => {
    button.addEventListener('click', function() {
        const aboutId = this.getAttribute('data-id');
        openModal(aboutId);
    });
});

function openModal(aboutId) {
    const editModal = document.getElementById('editModal' + aboutId);
    editModal.style.display = 'block';
    
    const closeBtn = editModal.querySelector('.close');
    
    closeBtn.addEventListener('click', function() {
        editModal.style.display = 'none';
    });
}


// AJAX HANDLER 
document.querySelectorAll('.edit-btnModal').forEach(button =>{
    button.addEventListener('click', function() {
        const editBtn = this.getAttribute('data-id');
        editBanner(editBtn);
    });
});

function editBanner(editBtn) {
    const formData = new FormData(document.getElementById('editForm'));
    fetch(`/edit-banner/${editBtn}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: formData
    })
    .then(response => {
        alertify.set('notifier', 'position', 'top-right');
        if (response.ok) {

            // Close the modal
            document.getElementById('editModal').style.display = 'none';
            alertify.success(`Edit Banner Successfully`);
            setTimeout(() => {
                location.reload();
            }, 1000);
        } else {
            console.error('Failed to edit');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
document.querySelectorAll('.edit-btnModal1').forEach(button => {
    button.addEventListener('click', function() {
        const editBtn = this.getAttribute('data-id');
        editAboutPic(editBtn);
    });
});

function editAboutPic(editBtn) {
    const formData = new FormData(document.getElementById('editForm1'));
    fetch(`/edit-about/${editBtn}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: formData
    })
    .then(response => {
        alertify.set('notifier', 'position', 'top-right');
        if (response.ok) {
            // Close the modal
            document.getElementById('editModal1').style.display = 'none';
            alertify.success(`Edit Background Successfully`);
            setTimeout(() => {
                location.reload();
            }, 1000);
        } else {
            console.error('Failed to edit');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}  
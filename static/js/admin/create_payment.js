var aboutPicModal = document.getElementById("openAboutPicModal");

var openAboutPicModalBtn = document.getElementById("openAboutPicModalBtn");
var closeBtns = document.querySelectorAll(".close");

openAboutPicModalBtn.onclick = function() {
    aboutPicModal.style.display = "block";
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


document.querySelectorAll('.edit-btnModal1').forEach(button => {
    button.addEventListener('click', function() {
        const editpayment = this.getAttribute('data-id');
        editPayment(editpayment);
    });
});

function editPayment(editpayment) {
    const formData = new FormData(document.getElementById('editForm1'));
    fetch(`/edit-payment/${editpayment}/`, {
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
            alertify.success(`Edit Payment Successfully`);
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
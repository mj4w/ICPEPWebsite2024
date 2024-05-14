var aboutPicModal = document.getElementById("openAboutPicModal");

var openAboutPicModalBtn = document.getElementById("openAboutPicModalBtn");
var closeBtns = document.querySelectorAll(".close");

openAboutPicModalBtn.onclick = function() {
    aboutPicModal.style.display = "block";
}
document.querySelectorAll('.close').forEach(closeButton => {
    closeButton.addEventListener('click', function() {
        const modal = this.closest('.modal');
        modal.style.display = 'none';
    });
});

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
        const context = this.getAttribute('data-id');
        editContext(context);
    });
});

document.querySelectorAll('.edit-btn1').forEach(button => {
    button.addEventListener('click', function() {
        const vmgId = this.getAttribute('data-id');
        openEditModal(vmgId);
    });
});

function openEditModal(vmgId) {
    const editModal = document.getElementById('editModal1');
    editModal.style.display = 'block';

    // Set up the form data with the appropriate values
    const visionTextarea = editModal.querySelector('#vision');
    const missionTextarea = editModal.querySelector('#mission');
    const goalTextarea = editModal.querySelector('#goal');
    const vmg = document.querySelector(`[data-id="${vmgId}"]`);

    visionTextarea.value = vmg.querySelector('.vision').innerText;
    missionTextarea.value = vmg.querySelector('.mission').innerText;
    goalTextarea.value = vmg.querySelector('.goal').innerText;

    // Close the modal when the close button is clicked
    const closeButton = editModal.querySelector('.close');
    closeButton.addEventListener('click', function() {
        editModal.style.display = 'none';
    });
}

function editVmg(context) {
    const formData = new FormData(document.getElementById('editForm1'));
    fetch(`/edit-vmg/${context}/`, {
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
            alertify.success(`Edit Vision Mission Goal Successfully`);
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
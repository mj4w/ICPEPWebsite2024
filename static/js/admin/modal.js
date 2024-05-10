document.getElementById("addUserButton").addEventListener("click", function() {
    document.getElementById("addUserModal").style.display = "block";
  });
  
  document.querySelector(".close").addEventListener("click", function() {
    document.getElementById("addUserModal").style.display = "none";
  });
  
  window.addEventListener("click", function(event) {
    if (event.target == document.getElementById("addUserModal")) {
      document.getElementById("addUserModal").style.display = "none";
    }
  });


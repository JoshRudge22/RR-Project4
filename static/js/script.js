//-----Logout Onclick-----//

document.addEventListener("DOMContentLoaded", function() {
    const logoutLink = document.getElementById("logout");
    if (logoutLink) {
        logoutLink.addEventListener("click", function(event) {
            if (!confirm('Are you sure you want to logout?')) {
                event.preventDefault();
            }
        });
    }
});

//-----Saving Porifle-----//

document.addEventListener("DOMContentLoaded", function() {
    const save = document.getElementById("save");
    if (save) {
        save.addEventListener("click", function(event) {
            if (!confirm('Please confirm updates')) {
                event.preventDefault();
            }
        });
    }
});
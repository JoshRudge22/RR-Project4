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

document.addEventListener("DOMContentLoaded", function() {
    const cancel = document.getElementById("cancel");
    if (cancel) {
        cancel.addEventListener("click", function(event) {
            if (!confirm('Please confirm you would like to cancel this job application')) {
                event.preventDefault();
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const remove = document.getElementById("remove");
    if (remove) {
        remove.addEventListener("click", function(event) {
            if (!confirm('Please confirm you would like to cancel this job application')) {
                event.preventDefault();
            }
        });
    }
});
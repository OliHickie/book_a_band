$(document).ready(function () {
    // Trigger for Jquery toasts 
    let getToast = [].slice.call(document.querySelectorAll('.toast'));
    let displayToast = getToast.map(function (toastEl) {
        return new bootstrap.Toast(toastEl).show();
    });

    // Trigger Jquery tooltips 
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })

    // Replace all spaces in href tags with %20
    // https://stackoverflow.com/questions/853804/jquery-javascript-replace-space-in-anchor-link-with-20 
    $("a").each(function () {
        this.href = this.href.replace(/\s/g, "%20");
    });
})
document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.querySelector(".hamburger-menu");
    const sidebar = document.querySelector(".sidebar");
    const closeBtn = document.querySelector(".close-btn");

    hamburger.addEventListener("click", function () {
        sidebar.style.right = "0";
    });

    closeBtn.addEventListener("click", function () {
        sidebar.style.right = "-250px";
    });
});

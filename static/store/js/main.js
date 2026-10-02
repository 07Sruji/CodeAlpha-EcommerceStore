document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        document.querySelectorAll(".message").forEach(el => {
            el.style.transition = "opacity .3s";
            el.style.opacity = "0";
            setTimeout(() => el.remove(), 350);
        });
    }, 3000);
});



function toggleDropdown(button) {
    const dropdownMenu = button.nextElementSibling;
    dropdownMenu.classList.toggle('show');
}

window.onclick = function(event) {
    if (!event.target.matches('.add-button')) {
        const dropdowns = document.getElementsByClassName('dropdown-menu');
        for (let i = 0; i < dropdowns.length; i++) {
            const dropdownMenu = dropdowns[i];
            if (dropdownMenu.classList.contains('show')) {
                dropdownMenu.classList.remove('show');
            }
        }
    }
}

// to get crfs token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken'); // getting the cookie to pass as csrf tokenW

/*
const searchBtn = document.getElementById("search-btn");
// Agrega un evento clic al botón de búsqueda
function prevent(event) {
    event.preventDefault(); // Previene el envío automático del formulario
    // Aquí puedes agregar el código para mostrar el Modal según tus necesidades
    // Por ejemplo, puedes usar Bootstrap para mostrar el Modal programáticamente
    // $('#searchModal').modal('show'); // Suponiendo que estás usando jQuery y Bootstrap
    const searchModal = new bootstrap.Modal(document.getElementById('searchModal'));
    searchModal.show();
}

 */
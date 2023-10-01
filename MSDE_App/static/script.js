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

const csrftoken = getCookie('csrftoken'); // getting the cookie to pass as csrf token
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


function handleSearch() {
    // Esta función simula la búsqueda y actualización del resultado
    function handleSearch() {
        const searchBySelect = document.getElementById("search-by-select").value;
        const dataToSearch = document.getElementById("data-to-search").value;

        // Simula una solicitud AJAX, aquí debes realizar la búsqueda real en tu aplicación
        setTimeout(function () {
            const result = { student_code: "123", student_id: "456", student_name: "John Doe" }; // Ejemplo de resultado

            // Actualiza el contenido del modal con el resultado
            const searchResult = document.getElementById("search-result");
            if (result) {
                searchResult.innerHTML = `
                    <p>The student was found:</p>
                    <p>With code ${result.student_code}, ID ${result.student_id} and name ${result.student_name}</p>
                `;
            } else {
                searchResult.innerHTML = `
                    <p>We didn't find that student (maybe you didn't select a 'search by' option)</p>
                `;
            }

            // Muestra el modal
            $('#searchModal').modal('show');
        }, 1000); // Simula una demora en la búsqueda, reemplaza con tu lógica real
    }

    document.getElementById("search-btn").addEventListener("click", handleSearch);
}

function handleAddStudent(student) {
    fetch('/reports/add_student/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            student: student
        }),
    })
}

function handleQuitStudent(student) {
    fetch('/reports/quit_student/', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            student: student
        }),
    })
}
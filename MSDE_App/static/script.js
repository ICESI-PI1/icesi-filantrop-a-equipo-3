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

function handleSearch() {
    console.log("entro a ejecutar search")
    const search_by_select = document.getElementById("search-by-select").value
    const data_to_search = document.getElementById("data-to-search").value
    const csrftoken = getCookie('csrftoken'); // getting the cookie to pass as csrf token

    fetch('/reports/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            search_by: search_by_select,
            data: data_to_search
        })
    })
}

function handleAddStudent(student) {
    fetch('/reports/add_student/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
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
        },
        body: JSON.stringify({
            student: student
        }),
    })
}
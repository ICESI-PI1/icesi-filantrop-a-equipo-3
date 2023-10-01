function handleSearch() {
    const search_by_select = document.getElementById("search-by-select").value
    const data_to_search = document.getElementById("data-to-search").value

    fetch('reports/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            search_by: search_by_select,
            data: data_to_search
        }),
    })
}
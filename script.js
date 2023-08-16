// script.js

const searchResultsContainer = document.getElementById("search-results");

function createCard(link) {
    const card = document.createElement("div");
    card.classList.add("card");
    card.innerHTML = `<a href="${link.url}" target="_blank">${link.title}</a>`;
    return card;
}

async function performSearch() {
    const searchInput = document.getElementById("search-input").value;

    const response = await fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: searchInput })
    });

    const searchResults = await response.json();
    displaySearchResults(searchResults);
}

function displaySearchResults(results) {
    searchResultsContainer.innerHTML = "";
    results.forEach(result => {
        const card = createCard(result);
        searchResultsContainer.appendChild(card);
    });
}

// script.js
const newsContainer = document.getElementById("news-container");

function createNewsCard(url) {
    const card = document.createElement("div");
    card.classList.add("news-card");
    card.innerHTML = `<a href="${url}" target="_blank">${url}</a>`;
    return card;
}

async function fetchNews() {
    try {
        const response = await fetch('/get_news', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const newsResults = await response.json();
        displayNews(newsResults);
    } catch (error) {
        console.error("Error fetching news:", error);
    }
}

function displayNews(results) {
    results.forEach(result => {
        const card = createNewsCard(result);
        newsContainer.appendChild(card);
    });
}

window.onload = fetchNews;

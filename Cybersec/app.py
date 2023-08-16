from flask import Flask, render_template, request
from googlesearch import search
from itertools import islice

app = Flask(__name__, template_folder='temp')

def search_cybersecurity_news(query, num_results=5):
    results = []
    try:
        for url in search(query, lang='en', tbs='nws', stop=num_results):
            results.append(url)
    except Exception as e:
        print("Error searching:", e)
    return results

def get_top_cybersecurity_news(query, num_results=5):
    news_results = search_cybersecurity_news(query, num_results)
    return news_results

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []

    if request.method == 'POST':
        query = request.form['query']
        num_results = int(request.form['num_results'])
        print("Received query:", query)
        print("Number of results:", num_results)
        results = get_top_cybersecurity_news(query, num_results)

    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)

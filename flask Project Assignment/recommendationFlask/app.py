from flask import Flask, render_template, request

app = Flask(__name__)
articles = {
    1: {'title': 'Article 1', 'category': 'Technology'},
    2: {'title': 'Article 2', 'category': 'Travel'},
    3: {'title': 'Article 3', 'category': 'Technology'},
    4: {'title': 'Article 4', 'category': 'Travel'},
    5: {'title': 'Article 5', 'category': 'Food'},
}
def recommend_articles(preferred_category):
    recommendations = []
    for article_id, article in articles.items():
        if article['category'] == preferred_category:
            recommendations.append(article)
    return recommendations


@app.route('/')
def home():
    return 'Welcome to the Article Recommendation System!'

@app.route('/select-preferences', methods=['GET', 'POST'])
def select_preferences():
    if request.method == 'POST':
        preferred_category = request.form.get('category')
        recommendations = recommend_articles(preferred_category)
        return render_template('recommendations.html', recommendations=recommendations)
    return render_template('preferences.html')



if __name__ == '__main__':
    app.run(debug=True)


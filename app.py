from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Список новостей (в реальном приложении здесь была бы логика работы с базой данных)
news = []

@app.route('/detail/<int:news_id>')
def detail(news_id):
    news_item = news[news_id - 1]
    return render_template('detail.html', news=news_item, timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), author=news_item['author'])

@app.route('/')
def index():
    return render_template('index.html', news=news)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        password = request.form['password']
        if password == 'donews-password':
            news.append({'title': title, 'content': content, 'author': author, 'emoji': '😊'})
            return redirect(url_for('index'))
        else:
            return 'Неверный пароль'
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)
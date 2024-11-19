from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Запрос к API для получения случайной цитаты
        response = requests.get('https://api.quotable.io/random')
        response.raise_for_status()  # Проверка успешности запроса
        data = response.json()
        quote = data.get('content', 'Не удалось получить цитату.')
        author = data.get('author', 'Неизвестный автор')
    except requests.exceptions.RequestException as e:
        quote = 'Произошла ошибка при получении цитаты.'
        author = ''
        print(f"Ошибка запроса: {e}")

    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)
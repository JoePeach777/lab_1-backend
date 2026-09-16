from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# Консольное логирование каждого запроса (повышенный уровень)
@app.before_request
def log_request():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {request.method} {request.path}")

# 1. Текстовый эндпоинт (Корневой)
@app.route('/')
def home():
    return 'Привет из бэкенда'

# 2. JSON-эндпоинты (Задание 1, 2 и 3)
@app.route('/api/system')
def system_info():
    return jsonify({"os": "Linux", "arch": "x64"})

@app.route('/api/tickets')
def get_tickets():
    return jsonify([
        {"id": 1, "title": "Концерт рок-группы", "price": 1500},
        {"id": 2, "title": "Театральная постановка", "price": 2000}
    ])

@app.route('/api/events')
def get_events():
    return jsonify([
        {"id": 1, "name": "Rock Fest 2026", "date": "2026-10-15"},
        {"id": 2, "name": "Tech Meetup", "date": "2026-10-20"}
    ])

@app.route('/api/departments')
def get_departments():
    return jsonify([
        {"id": 1, "name": "Разработка"},
        {"id": 2, "name": "Тестирование"},
        {"id": 3, "name": "Маркетинг"}
    ])

# 3. JSON эндпоинт с параметром в пути (Повышенный уровень, Вариант 9)
@app.route('/api/tickets/<int:ticket_id>')
def get_ticket_by_id(ticket_id):
    return jsonify({
        "requestedId": ticket_id,
        "status": "success",
        "message": "Информация о билете"
    })

# 4. Кастомная обработка ошибки 404 (Средний и повышенный уровень)
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run(port=3000, debug=True)
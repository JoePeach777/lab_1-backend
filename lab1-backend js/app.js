const express = require('express');
const app = express();
const port = 3000;

// Логирование запросов (повышенный уровень)
app.use((req, res, next) => {
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
    next();
});

// Текстовый эндпоинт
app.get('/', (req, res) => {
    res.send('Привет из бэкенда');
});

// JSON-эндпоинты (Вариант 9)
app.get('/api/system', (req, res) => {
    res.json({ os: "Linux", arch: "x64" });
});

app.get('/api/tickets', (req, res) => {
    res.json([
        { id: 1, title: "Концерт рок-группы", price: 1500 },
        { id: 2, title: "Театральная постановка", price: 2000 }
    ]);
});

app.get('/api/events', (req, res) => {
    res.json([
        { id: 1, name: "Rock Fest 2026", date: "2026-10-15" },
        { id: 2, name: "Tech Meetup", date: "2026-10-20" }
    ]);
});

app.get('/api/departments', (req, res) => {
    res.json([
        { id: 1, name: "Разработка" },
        { id: 2, name: "Тестирование" },
        { id: 3, name: "Маркетинг" }
    ]);
});

// Эндпоинт с параметром (повышенный уровень)
app.get('/api/tickets/:id', (req, res) => {
    res.json({
        requestedId: req.params.id,
        status: "success",
        message: "Информация о билете"
    });
});

// Обработка 404
app.use((req, res) => {
    res.status(404).json({ error: "Not Found" });
});

app.listen(port, () => {
    console.log(`Сервер запущен на http://localhost:${port}`);
});
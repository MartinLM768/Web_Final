const express = require('express');

const app = express();

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.set('view engine', 'ejs');

// Datos en memoria (temporal)
let tasks = [];

// Ruta para el endpoint raíz
app.get('/', (req, res) => {
    res.send('Bienvenido a la API de tareas. Usa /tasks para ver las tareas.');
});

// Rutas integradas directamente
app.get('/tasks', (req, res) => {
    res.json(tasks); // Devuelve las tareas almacenadas en memoria
});

app.post('/tasks', (req, res) => {
    const { title, description } = req.body;
    if (!title) {
        return res.status(400).send('El título es obligatorio');
    }
    const newTask = { id: tasks.length + 1, title, description: description || '' };
    tasks.push(newTask); // Agrega la nueva tarea al arreglo
    res.status(201).json(newTask); // Devuelve la tarea creada
});

// Iniciar el servidor
app.listen(3000, () => {
    console.log('Servidor corriendo en http://localhost:3000');
});
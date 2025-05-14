const express = require('express');
const app = express();

app.use(express.json());

// Datos simulados (temporal)
let students = [
    { id: 1, name: 'Juan Pérez', email: 'juan@example.com' },
];
let grades = [
    { id: 1, studentId: 1, course: 'Matemáticas', grade: 90 },
];

// Endpoint para obtener las notas de un estudiante
app.get('/students/:id/grades', (req, res) => {
    const studentId = parseInt(req.params.id);
    const studentGrades = grades.filter(g => g.studentId === studentId);
    res.json(studentGrades);
});

// Endpoint para subir o actualizar notas
app.post('/grades', (req, res) => {
    const { studentId, course, grade } = req.body;
    grades.push({ id: grades.length + 1, studentId, course, grade });
    res.status(201).send('Nota guardada');
});

// Iniciar el servidor
app.listen(3000, () => {
    console.log('Servidor corriendo en http://localhost:3000');
});
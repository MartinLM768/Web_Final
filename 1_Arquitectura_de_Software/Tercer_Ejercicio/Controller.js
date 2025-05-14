const Task = require('../models/taskModel');

// Obtener todas las tareas
exports.getAllTasks = async (req, res) => {
    try {
        const tasks = await Task.find();
        res.render('tasks', { tasks });
    } catch (err) {
        res.status(500).send(err.message);
    }
};

// Crear una nueva tarea
exports.createTask = async (req, res) => {
    try {
        const task = new Task(req.body);
        await task.save();
        res.redirect('/tasks');
    } catch (err) {
        res.status(500).send(err.message);
    }
};
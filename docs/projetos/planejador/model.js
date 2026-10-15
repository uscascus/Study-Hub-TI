export const STORAGE_KEY = 'study-hub-tasks-v1';

export function validDate(value) {
  if (value === '') return true;
  if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(value)) return false;
  const date = new Date(`${value}T12:00:00Z`);
  return Number.isFinite(date.getTime()) && date.toISOString().slice(0, 10) === value;
}

export function readTasks(raw) {
  if (raw === null) return { tasks: [], recovered: false };
  let values;
  try { values = JSON.parse(raw); } catch { return { tasks: [], recovered: true }; }
  if (!Array.isArray(values)) return { tasks: [], recovered: true };
  const seen = new Set();
  const tasks = values.filter(task => {
    if (!task || typeof task.id !== 'string' || !task.id || seen.has(task.id) ||
        typeof task.title !== 'string' || !task.title.trim() || task.title.length > 120 ||
        typeof task.done !== 'boolean' || !validDate(task.due)) return false;
    seen.add(task.id);
    return true;
  }).map(({ id, title, done, due }) => ({ id, title: title.trim(), done, due }));
  return { tasks, recovered: tasks.length !== values.length };
}

export function addTask(tasks, title, due, id) {
  const clean = String(title).trim();
  if (!clean || clean.length > 120) throw new Error('Escreva uma tarefa de 1 a 120 caracteres.');
  if (!validDate(due)) throw new Error('Informe uma data válida ou deixe o prazo vazio.');
  if (typeof id !== 'string' || !id || tasks.some(task => task.id === id)) throw new Error('Não foi possível identificar a tarefa. Tente novamente.');
  return [...tasks, { id, title: clean, due, done: false }];
}

export function toggleTask(tasks, id) {
  return tasks.map(task => task.id === id ? { ...task, done: !task.done } : task);
}

export function deleteTask(tasks, id) {
  return tasks.filter(task => task.id !== id);
}

export function filterTasks(tasks, filter) {
  if (filter === 'pending') return tasks.filter(task => !task.done);
  if (filter === 'done') return tasks.filter(task => task.done);
  return tasks;
}

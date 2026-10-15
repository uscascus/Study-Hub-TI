import { STORAGE_KEY, readTasks, addTask, toggleTask, deleteTask, filterTasks } from './model.js';

const form = document.querySelector('#task-form');
const title = document.querySelector('#title');
const due = document.querySelector('#due');
const list = document.querySelector('#tasks');
const filter = document.querySelector('#filter');
const summary = document.querySelector('#summary');
const feedback = document.querySelector('#feedback');
let tasks = [];
let persistent = true;

function announce(message, error = false) {
  feedback.textContent = message;
  feedback.className = error ? 'notice error' : '';
}

try {
  const loaded = readTasks(localStorage.getItem(STORAGE_KEY));
  tasks = loaded.tasks;
  if (loaded.recovered) announce('Alguns dados salvos estavam inválidos. As tarefas válidas foram recuperadas.', true);
} catch {
  persistent = false;
  announce('O navegador bloqueou o armazenamento. Você pode usar a lista, mas as tarefas serão perdidas ao fechar ou atualizar a página.', true);
}

function persist(message) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
    persistent = true;
    announce(message);
  } catch {
    persistent = false;
    announce(`${message} O navegador não conseguiu salvar. Esta alteração será perdida ao atualizar a página.`, true);
  }
}

function render() {
  list.replaceChildren();
  const visible = filterTasks(tasks, filter.value);
  const completed = tasks.filter(task => task.done).length;
  summary.textContent = tasks.length ? `${completed} de ${tasks.length} tarefa(s) concluída(s).` : 'Nenhuma tarefa adicionada.';
  if (!visible.length) {
    const empty = document.createElement('li');
    empty.className = 'empty';
    empty.textContent = tasks.length ? 'Nenhuma tarefa neste filtro.' : 'Sua próxima conquista começa com uma tarefa. Adicione a primeira!';
    list.append(empty);
  }
  for (const task of visible) {
    const row = document.createElement('li');
    row.className = `task-row${task.done ? ' completed' : ''}`;
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = task.done;
    checkbox.setAttribute('aria-label', `${task.done ? 'Reabrir' : 'Concluir'} tarefa: ${task.title}`);
    checkbox.addEventListener('change', () => {
      tasks = toggleTask(tasks, task.id);
      persist('Situação da tarefa atualizada.');
      render();
      const target = Array.from(list.querySelectorAll('input')).find(input => input.dataset.id === task.id);
      (target || filter).focus();
    });
    checkbox.dataset.id = task.id;
    const text = document.createElement('div');
    text.className = 'task-text';
    const name = document.createElement('span');
    name.className = 'task-name';
    name.textContent = task.title;
    const date = document.createElement('span');
    date.className = 'task-date';
    date.textContent = task.due ? `Prazo: ${task.due.split('-').reverse().join('/')}` : 'Sem prazo definido';
    text.append(name, date);
    const remove = document.createElement('button');
    remove.type = 'button';
    remove.className = 'delete-task';
    remove.textContent = 'Excluir';
    remove.setAttribute('aria-label', `Excluir tarefa: ${task.title}`);
    remove.addEventListener('click', () => {
      tasks = deleteTask(tasks, task.id);
      persist('Tarefa excluída.');
      render();
      title.focus();
    });
    row.append(checkbox, text, remove);
    list.append(row);
  }
}

form.addEventListener('submit', event => {
  event.preventDefault();
  try {
    const id = globalThis.crypto?.randomUUID?.() || `${Date.now()}-${Math.random().toString(36).slice(2)}`;
    tasks = addTask(tasks, title.value, due.value, id);
    filter.value = 'all';
    persist('Tarefa adicionada.');
    form.reset();
    render();
    title.focus();
  } catch (error) {
    announce(error.message, true);
  }
});

filter.addEventListener('change', render);
window.addEventListener('storage', event => {
  if (event.key !== STORAGE_KEY && event.key !== null) return;
  const loaded = readTasks(event.newValue);
  tasks = loaded.tasks;
  render();
  announce(loaded.recovered ? 'A atualização de outra aba contém dados inválidos; somente as tarefas válidas foram carregadas.' : 'Lista atualizada a partir de outra aba.', loaded.recovered || !persistent);
});
render();

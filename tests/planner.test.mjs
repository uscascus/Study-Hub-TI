import test from 'node:test';
import assert from 'node:assert/strict';
import { addTask, readTasks, validDate, toggleTask, deleteTask, filterTasks } from '../docs/projetos/planejador/model.js';

test('permite tarefa sem prazo e preserva o estado anterior ao adicionar', () => {
  const previous = [];
  const next = addTask(previous, '  Estudar Git  ', '', 'a');
  assert.deepEqual(next, [{ id: 'a', title: 'Estudar Git', due: '', done: false }]);
  assert.deepEqual(previous, []);
});
test('rejeita tarefa vazia, longa e identificador duplicado', () => {
  assert.throws(() => addTask([], '   ', '', 'a'));
  assert.throws(() => addTask([], 'x'.repeat(121), '', 'a'));
  const tasks = addTask([], 'Git', '', 'a');
  assert.throws(() => addTask(tasks, 'HTML', '', 'a'));
});
test('valida calendário, inclusive anos bissextos, sem converter datas impossíveis', () => {
  assert.equal(validDate('2028-02-29'), true);
  for (const date of ['2026-02-29', '2026-04-31', '2026-13-01', '15/10/2026', null, undefined]) assert.equal(validDate(date), false);
  assert.throws(() => addTask([], 'Git', '2026-02-29', 'a'));
});
test('recupera armazenamento ausente, JSON quebrado e formato inesperado', () => {
  assert.deepEqual(readTasks(null), { tasks: [], recovered: false });
  for (const raw of ['{', '{}', 'null', '12']) assert.deepEqual(readTasks(raw), { tasks: [], recovered: true });
});
test('preserva tarefas válidas e descarta entradas inválidas e ids duplicados', () => {
  const good = { id: 'a', title: 'Git', due: '2026-10-16', done: false };
  const loaded = readTasks(JSON.stringify([null, good, { ...good }, { ...good, id: 'b', done: 'false' }, { ...good, id: 'c', due: '2026-02-30' }]));
  assert.deepEqual(loaded, { tasks: [good], recovered: true });
});
test('concluir, reabrir e filtrar mantém título e prazo e não altera a origem', () => {
  const tasks = addTask([], 'Revisar', '2026-10-16', 'a');
  const changed = toggleTask(tasks, 'a');
  assert.equal(tasks[0].done, false);
  assert.deepEqual(changed[0], { ...tasks[0], done: true });
  assert.equal(filterTasks(changed, 'pending').length, 0);
  assert.equal(filterTasks(changed, 'done').length, 1);
  assert.deepEqual(toggleTask(changed, 'a'), tasks);
});
test('excluir uma tarefa preserva as demais e excluir id desconhecido não remove tarefas', () => {
  const tasks = addTask(addTask([], 'Git', '', 'a'), 'CSS', '', 'b');
  assert.deepEqual(deleteTask(tasks, 'a'), [tasks[1]]);
  assert.deepEqual(deleteTask(tasks, 'missing'), tasks);
  assert.equal(tasks.length, 2);
});

# Planejador de estudos

Projeto pessoal de aplicação web para praticar JavaScript e organização de estudos. Permite criar tarefas, definir prazo opcional, concluir, reabrir, filtrar e excluir atividades.

**[Usar a aplicação](https://uscascus.github.io/Study-Hub-TI/projetos/planejador/)** · [Código-fonte](../../docs/projetos/planejador/)

## Tecnologias e organização

- HTML semântico e CSS responsivo compartilhado com o portfólio.
- JavaScript em módulos: `model.js` contém as regras de dados e `app.js` faz a interface e a persistência.
- `localStorage` guarda somente a lista no navegador. Não há API, conta ou banco remoto.
- Testes com `node:test` e `node:assert`, incluídos no Node.js, sem pacotes externos.

O código executável fica em `docs/projetos/planejador` para publicação pelo GitHub Pages. Esta pasta documenta o projeto pessoal, sem duplicar sua implementação.

## Executar

Na raiz do repositório, execute `python -m http.server 8000 --directory docs` e abra `http://localhost:8000/projetos/planejador/`. Para os testes: `node --test tests/planner.test.mjs` (Node.js 18+).

## Uso

1. Escreva uma tarefa entre 1 e 120 caracteres e, se quiser, informe um prazo.
2. Clique em **Adicionar**. A tarefa aparece como pendente.
3. Marque a caixa para concluir; desmarque para reabrir.
4. Use o filtro para ver todas, pendentes ou concluídas.
5. Recarregue a página para conferir a persistência. **Excluir** remove uma tarefa definitivamente.

## Validação e decisões

O modelo rejeita nomes vazios e datas inexistentes, trata JSON corrompido e descarta registros inválidos ou duplicados. O texto informado pelo usuário é inserido com `textContent`, sem interpretação como HTML. Falhas de acesso ou de gravação no armazenamento geram aviso visível; a lista continua utilizável durante a sessão. Alterações em outra aba do mesmo endereço atualizam a lista.

Os testes cobrem inclusão, limites de entrada, datas bissextas, recuperação de dados corrompidos, conclusão/reabertura, filtros e exclusão. A validação em navegador complementa os testes do modelo com os fluxos reais da interface.

## Limitações e aprendizados

Não há sincronização entre dispositivos, autenticação, backup, edição do texto nem notificações. Limpar o armazenamento apaga os dados; em navegação privada ou com armazenamento bloqueado, a persistência pode não funcionar. Duas abas gravando simultaneamente podem sobrescrever alterações; o projeto não implementa resolução de conflitos.

O projeto exercita separação entre dados e interface, eventos, renderização segura, persistência local, acessibilidade e testes de entradas inválidas. Próximas evoluções possíveis: editar tarefas e exportar/importar uma cópia da lista.

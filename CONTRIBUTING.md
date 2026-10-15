# Como contribuir

Sugestões, correções e melhorias são bem-vindas. Use as issues para discutir uma ideia antes de alterar o projeto.

## Propor uma alteração

1. Abra uma issue descrevendo o problema, resultado esperado e, se possível, os passos para reproduzir.
2. Faça um fork e crie uma branch a partir de `Pitu/bootcamp-intermediaria`, que contém a versão atual do site.
3. Mantenha o escopo pequeno. Novas branches do projeto usam o prefixo `Pitu/`; exemplos: `Pitu/corrigir-menu` ou `Pitu/documentar-projeto`.
4. Execute o site por HTTP e confira a alteração em tela larga e estreita. Se mudar o planejador, rode `node --test tests/planner.test.mjs`. Rode também `python scripts/check_links.py`.
5. Faça commits que expliquem a intenção: `feat: permite filtrar tarefas`, `fix: valida datas impossiveis`, `docs: explica armazenamento local`.
6. Abra um pull request para a branch ativa, descrevendo o problema, a solução e os testes realizados.

## Revisão

- Verificar se os links e recursos continuam funcionando no subdiretório do GitHub Pages.
- Conferir teclado, rótulos dos campos, contraste e layout móvel.
- Verificar se o código trata entradas inválidas e falhas no armazenamento.
- Não inserir credenciais, dados privados ou conteúdo de terceiros sem permissão.
- Fazer revisão do diff antes do merge; resolver conflitos preservando o trabalho existente.

## Comandos de referência

```sh
git fetch origin
git switch Pitu/bootcamp-intermediaria
git pull --ff-only origin Pitu/bootcamp-intermediaria
git switch -c Pitu/minha-alteracao
python -m http.server 8000 --directory docs
node --test tests/planner.test.mjs
python scripts/check_links.py
git add caminho/do/arquivo
git commit -m "docs: esclarece instrucoes de execucao"
git push -u origin Pitu/minha-alteracao
```

Antes de executar comandos, confira `git status`; não descarte alterações locais para trocar de branch.

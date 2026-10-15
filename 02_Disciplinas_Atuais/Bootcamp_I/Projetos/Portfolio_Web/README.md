# Portfólio web - Study Hub TI

Projeto acadêmico do Bootcamp I para apresentar o perfil de Lucas Coutinho, projetos, materiais e evolução do repositório.

**[Site publicado](https://uscascus.github.io/Study-Hub-TI/)** · [Código-fonte](../../../../docs/)

## Funcionalidades

- Apresentação pessoal e interesses em back-end e segurança da informação.
- Seções de projetos acadêmicos e pessoais, percurso, documentos e contato.
- Links para o GitHub, LinkedIn, PDFs e apresentação com roteiro.
- Layout para desktop e celular, navegação por teclado e link para pular ao conteúdo.
- Planejador pessoal acessível pela seção de projetos.

## Tecnologias e execução

HTML5 e CSS3, sem dependências externas. A página principal funciona sem JavaScript; apenas o planejador precisa dele. Execute `python -m http.server 8000 --directory docs` na raiz e abra `http://localhost:8000`.

## Publicação

O GitHub Pages publica a pasta `/docs` da branch `Pitu/bootcamp-intermediaria`. Arquivos usam caminhos relativos para funcionar em `/Study-Hub-TI/`. O arquivo `.nojekyll` mantém a publicação estática sem processamento por Jekyll. A `main` não é alterada nesta etapa.

## Materiais e decisões

O conteúdo parte do documento da etapa inicial e dos projetos desta entrega; não inclui experiências, certificados ou métricas inventadas. A foto e os contatos já integravam o repositório. PDFs e apresentação são servidos junto com o site para evitar depender da navegação do GitHub.

As alterações são registradas por commits e tags, com descrição em [CHANGELOG.md](../../../../CHANGELOG.md). Verificação: `python scripts/check_links.py`, testes do planejador e revisão visual em navegador. Para contribuir, consulte [CONTRIBUTING.md](../../../../CONTRIBUTING.md).

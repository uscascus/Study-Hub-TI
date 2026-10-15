CEUB / CIÊNCIA DA COMPUTAÇÃO / BOOTCAMP I

# Study Hub TI

## Portfólio acadêmico
com versionamento

Entrega intermediária - Criação de Repositório com Versionamento

Estudante | Identificação
--- | ---
Lucas Coutinho | Ciência da Computação - CEUB
Turma A - 0726 | Entrega individual - 15/10/2026

O Study Hub reúne atividades, projetos e documentos em um repositório organizado. Nesta etapa, o planejamento inicial evolui para um portfólio web e uma aplicação pessoal, com histórico de versões e instruções de execução.

**Portfólio no GitHub Pages**
[https://uscascus.github.io/Study-Hub-TI/](https://uscascus.github.io/Study-Hub-TI/)

**Código da etapa intermediária**
[https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria](https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria)

O site está publicado. Ainda falta adicionar o projeto ao meu LinkedIn e gravar a apresentação no YouTube.

Prazo indicado no enunciado: 17/10/2026, às 23h55.

BOOTCAMP I / 01

## Planejamento e organização

Criei o Study Hub para reunir minhas atividades e projetos em um lugar só. Mantive a estrutura da etapa inicial e acrescentei o portfólio web e o planejador de estudos. Assim consigo revisar o que estudei e apresentar meus trabalhos.

```text
Study-Hub-TI/
|-- 01_Apresentacao_e_Perfil/
|-- 02_Disciplinas_Atuais/Bootcamp_I/
|   |-- Atividades_e_Entregas/
|   `-- Projetos/Portfolio_Web/
|-- 03_Projetos_e_Certificados/Planejador_de_Estudos/
|-- 04_Recursos_e_Referencias/
|-- docs/
|   |-- index.html e assets/
|   |-- materiais/ (PDFs e apresentacao)
|   `-- projetos/planejador/ (aplicacao)
|-- documento/ e entrega/
|-- scripts/
`-- tests/
```

### Decisões de organização

O portfólio web é o projeto acadêmico do Bootcamp I. O planejador é o projeto pessoal. Cada um possui README com objetivo, tecnologias, execução, decisões e limitações. A implementação executável fica em docs, raiz pública do GitHub Pages; a documentação de cada projeto permanece na área correspondente, evitando duplicação de código.

### Manutenção

Pretendo atualizar o repositório durante o semestre, separar os materiais por disciplina e registrar cada alteração em um commit. Cada projeto terá um README com instruções de uso e os principais aprendizados.

**Estrutura e instruções do repositório**
[https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria/README.md](https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria/README.md)

BOOTCAMP I / 02

## Projetos implementados

### Acadêmico: portfólio web

Página em HTML e CSS com apresentação, interesses em back-end e segurança da informação, projetos, percurso, PDFs, slides e contato. O layout se adapta a computador e celular. A navegação inclui rótulos, foco visível e acesso direto ao conteúdo pelo teclado.

Figura 1. Página inicial do Study Hub TI no GitHub Pages.

### Pessoal: planejador de estudos

Aplicação em JavaScript que permite adicionar tarefas com prazo opcional, concluir e reabrir, filtrar por situação e excluir. Os dados ficam no localStorage do navegador. As regras de dados são separadas da interface para permitir testes sem dependências externas.

**Experimentar o planejador**
[https://uscascus.github.io/Study-Hub-TI/projetos/planejador/](https://uscascus.github.io/Study-Hub-TI/projetos/planejador/)

Limites: não há conta, sincronização, backup, notificações ou edição de títulos. Limpar os dados do navegador remove as tarefas. Gravações simultâneas em duas abas podem sobrescrever alterações. Se o armazenamento falhar, um aviso informa que os dados da sessão não foram salvos.

BOOTCAMP I / 03

## Versionamento e colaboração

A etapa inicial ficou registrada no commit d3c9894 da main. Para desenvolver o site, usei a branch Pitu/bootcamp-intermediaria. Os commits registram as mudanças, e as tags permitem consultar cada versão.

Marco | Registro e finalidade
--- | ---
Base anterior | d3c9894: etapa inicial preservada em main.
Branch de trabalho | Pitu/bootcamp-intermediaria: desenvolvimento e publicação desta etapa.
Versão 1.0.0 | Primeira versão do portfólio, planejador e testes.
Versão 1.1.0 | Documentação, apresentação e relatório intermediário.
Versão 1.1.1 | Revisão dos textos do site e da entrega.

### Fluxo de trabalho

Antes de alterar os arquivos, confiro o estado do repositório e atualizo as referências remotas. Depois executo os testes, reviso as mudanças e faço o commit. O GitHub Pages publica a branch intermediária; a main mantém a etapa inicial.

### Como colaborar

Sugestões e problemas podem ser registrados nas issues. Para propor uma mudança, o guia CONTRIBUTING explica como criar uma branch, testar a alteração e abrir um pull request. A revisão inclui funcionamento, acessibilidade e links.

**Histórico de commits**
[https://github.com/uscascus/Study-Hub-TI/commits/Pitu/bootcamp-intermediaria/](https://github.com/uscascus/Study-Hub-TI/commits/Pitu/bootcamp-intermediaria/)

**Versões e tags**
[https://github.com/uscascus/Study-Hub-TI/tags](https://github.com/uscascus/Study-Hub-TI/tags)

**Guia de contribuição**
[https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria/CONTRIBUTING.md](https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria/CONTRIBUTING.md)

BOOTCAMP I / 04

## Publicação e verificação

O repositório é público. O GitHub Pages utiliza a pasta /docs da branch Pitu/bootcamp-intermediaria. Caminhos relativos permitem servir o site no subdiretório /Study-Hub-TI/. O arquivo .nojekyll mantém a publicação estática.

Verificação | Resultado
--- | ---
Regras do planejador | 7 testes automatizados aprovados: inclusão, limites, datas, recuperação, filtros, conclusão e exclusão.
Navegador | Inclusão com prazo, conclusão, filtro de pendentes, persistência após recarregar, reabertura e exclusão conferidos.
Layout | Revisão em computador (1366 px) e celular (390 px); sem rolagem horizontal nas telas verificadas.
Links e arquivos | Verificação automatizada dos destinos e âncoras locais; PDFs revisados visualmente.
Publicação HTTPS | GitHub Pages publicado e respostas HTTP 200 conferidas.

### Reproduzir os testes

O teste local revelou que arquivos .mjs eram servidos como texto neste Windows. Os módulos foram alterados para .js e a configuração type: module foi adicionada ao projeto. O fluxo foi novamente verificado no navegador após a correção.

Os testes automatizados cobrem as regras das tarefas. A persistência foi conferida no navegador. O bloqueio do armazenamento é tratado no código, mas ainda não foi simulado no navegador.

BOOTCAMP I / 05

## LinkedIn e apresentação

### Integração com o perfil profissional

O site e o README têm um link para meu LinkedIn. Ainda vou adicionar o Study Hub à seção de projetos do perfil. A descrição que usarei está em documento/Integracao_LinkedIn.md.

**Projeto:** Study Hub TI - Portfólio acadêmico e planejador de estudos.
**Descrição:** Projeto desenvolvido no Bootcamp I de Ciência da Computação no CEUB para organizar atividades e documentar minha evolução. Inclui portfólio no GitHub Pages e planejador com JavaScript, armazenamento local e testes.

**Perfil profissional**
[https://www.linkedin.com/in/lucas-coutinho-chaul-27a139268/](https://www.linkedin.com/in/lucas-coutinho-chaul-27a139268/)

### Apresentação de cinco minutos

Tempo | Conteúdo e demonstração
--- | ---
0:00 - 0:40 | Perfil, contexto e objetivo do Study Hub.
0:40 - 1:30 | Estrutura do repositório e README de um projeto.
1:30 - 2:20 | Página publicada e materiais disponíveis.
2:20 - 3:25 | Planejador: adicionar, concluir, filtrar e recarregar.
3:25 - 4:20 | Commits, tags, testes e fluxo de colaboração.
4:20 - 5:00 | Contato, integração profissional e próximos passos.

**Slides e roteiro completo**
[https://uscascus.github.io/Study-Hub-TI/materiais/apresentacao.html](https://uscascus.github.io/Study-Hub-TI/materiais/apresentacao.html)

Ainda falta gravar e publicar o vídeo no YouTube. Organizei a apresentação em seis partes, com demonstração do repositório e do planejador. Depois da gravação, vou incluir o link neste relatório.

BOOTCAMP I / 06

## Critérios e finalização

Requisito do desafio | Evidência e estado
--- | ---
Planejamento e diretórios | Estrutura mantida e ampliada; planejamento e READMEs disponíveis.
Projeto web e versão 1.0 | Portfólio e planejador, com commits e tags no GitHub.
Alterações enviadas | Branch intermediária publicada, com revisão na versão 1.1.1.
Documentação por projeto | README do portfólio, README do planejador e guia de contribuição.
Repositório público e Pages | Repositório público e site HTTPS verificado.
Integração com LinkedIn | Link no site. Falta adicionar o projeto ao meu perfil.
Apresentação no YouTube | Slides e roteiro prontos. Gravação, publicação e URL pendentes.
Entrega individual em PDF | Relatório com os projetos, testes e links da entrega.

### Falta concluir

1. Adicionar o projeto ao meu LinkedIn.
2. Gravar e publicar a apresentação no YouTube.
3. Incluir o link do vídeo e o registro do LinkedIn neste relatório antes do envio, até 17/10/2026 às 23h55.

### Próximas evoluções

Quero acrescentar os trabalhos das próximas disciplinas e manter os READMEs atualizados. No planejador, pretendo estudar como editar tarefas e exportar uma cópia da lista.

Referências: enunciado da Entrega Intermediária do Bootcamp I; materiais da etapa inicial deste repositório; documentação oficial do GitHub Pages e da API de Pages.

**GitHub Pages - documentação oficial**
[https://docs.github.com/en/pages](https://docs.github.com/en/pages)

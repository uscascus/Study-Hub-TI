# Study Hub TI - Entrega intermediária

Lucas Coutinho | Ciência da Computação | CEUB | Turma A - 0726

Data: 15/10/2026

CEUB / CIÊNCIA DA COMPUTAÇÃO / BOOTCAMP I

Study Hub TI

Portfólio acadêmico
com versionamento

Entrega intermediária - Criação de Repositório com Versionamento

Estudante | Identificação
--- | ---
Lucas Coutinho | Ciência da Computação - CEUB
Turma A - 0726 | Entrega individual - 15/10/2026

O Study Hub reúne atividades, projetos e documentos em um repositório organizado. Nesta etapa, o planejamento inicial evolui para um portfólio web e uma aplicação pessoal, com histórico de versões e instruções de execução.

**Portfólio no GitHub Pages**
<link href="https://uscascus.github.io/Study-Hub-TI/" color="#245a4f">https://uscascus.github.io/Study-Hub-TI/</link>

**Código da etapa intermediária**
<link href="https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria" color="#245a4f">https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria</link>

Estado desta revisão: implementação e testes locais concluídos; publicação web em preparação. LinkedIn e vídeo no YouTube pendentes.

Prazo indicado no enunciado: 17/10/2026, às 23h55.

BOOTCAMP I / 01

Planejamento e organização

## Planejamento e organização

Objetivo: centralizar minha produção acadêmica e pessoal, facilitar revisões e apresentar projetos reais como parte do perfil profissional. O repositório existente foi aproveitado para preservar o histórico e os materiais da etapa inicial.

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

Decisões de organização

O portfólio web é o projeto acadêmico do Bootcamp I. O planejador é o projeto pessoal. Cada um possui README com objetivo, tecnologias, execução, decisões e limitações. A implementação executável fica em docs, raiz pública do GitHub Pages; a documentação de cada projeto permanece na área correspondente, evitando duplicação de código.

Manutenção

Usar nomes claros, atualizar materiais durante o semestre e criar commits com um objetivo específico. Não publicar credenciais ou dados de terceiros. Certificados, experiências e colaboração só serão apresentados quando existirem evidências reais.

**Estrutura e instruções do repositório**
<link href="https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria/README.md" color="#245a4f">https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria/README.md</link>

BOOTCAMP I / 02

Projetos implementados

## Projetos implementados

Acadêmico: portfólio web

Página em HTML e CSS com apresentação, interesses em back-end e segurança da informação, projetos, percurso, PDFs, slides e contato. O layout se adapta a computador e celular. A navegação inclui rótulos, foco visível e acesso direto ao conteúdo pelo teclado.

Figura 1. Página inicial do portfólio em revisão local. Conteúdo e foto partem dos materiais já existentes no Study Hub.

Pessoal: planejador de estudos

Aplicação em JavaScript que permite adicionar tarefas com prazo opcional, concluir e reabrir, filtrar por situação e excluir. Os dados ficam no localStorage do navegador. As regras de dados são separadas da interface para permitir testes sem dependências externas.

**Experimentar o planejador**
<link href="https://uscascus.github.io/Study-Hub-TI/projetos/planejador/" color="#245a4f">https://uscascus.github.io/Study-Hub-TI/projetos/planejador/</link>

Limites: não há conta, sincronização, backup, notificações ou edição de títulos. Limpar os dados do navegador remove as tarefas. Gravações simultâneas em duas abas podem sobrescrever alterações. Se o armazenamento falhar, um aviso informa que os dados da sessão não foram salvos.

BOOTCAMP I / 03

Versionamento e colaboração

## Versionamento e colaboração

O remoto foi atualizado antes do desenvolvimento. A base é o commit d3c9894 de origin/main, que consolidava a etapa inicial. Não havia alterações locais, outras branches remotas ativas ou pull requests abertos na checagem inicial.

Marco | Registro e finalidade
--- | ---
Base anterior | d3c9894: etapa inicial preservada em main.
Branch de trabalho | Pitu/bootcamp-intermediaria: desenvolvimento e publicação desta etapa.
Versão 1.0.0 | Primeira versão do portfólio, planejador e testes.
Versão 1.1.0 | Evolução da documentação, apresentação e relatório intermediário.

Fluxo de trabalho

Conferir git status e atualizar referências; trabalhar na branch ativa; executar os testes; revisar o diff; criar commits específicos e enviar a branch para o GitHub. As tags identificam versões recuperáveis. A main só recebe integração mediante autorização específica.

Colaboração preparada

O guia CONTRIBUTING descreve abertura de issues, criação de branches, testes e pull requests. A revisão deve conferir funcionamento, acessibilidade, links e ausência de credenciais. Este é um trabalho individual; o fluxo está documentado, sem alegar participação ou revisão de terceiros.

**Histórico de commits**
<link href="https://github.com/uscascus/Study-Hub-TI/commits/Pitu/bootcamp-intermediaria/" color="#245a4f">https://github.com/uscascus/Study-Hub-TI/commits/Pitu/bootcamp-intermediaria/</link>

**Versões e tags**
<link href="https://github.com/uscascus/Study-Hub-TI/tags" color="#245a4f">https://github.com/uscascus/Study-Hub-TI/tags</link>

**Guia de contribuição**
<link href="https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria/CONTRIBUTING.md" color="#245a4f">https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria/CONTRIBUTING.md</link>

BOOTCAMP I / 04

Publicação e verificação

## Publicação e verificação

O repositório é público. O GitHub Pages utiliza a pasta /docs da branch Pitu/bootcamp-intermediaria. Caminhos relativos permitem servir o site no subdiretório /Study-Hub-TI/. O arquivo .nojekyll mantém a publicação estática.

Verificação | Resultado
--- | ---
Regras do planejador | 7 testes automatizados aprovados: inclusão, limites, datas, recuperação, filtros, conclusão e exclusão.
Navegador | Inclusão com prazo, conclusão, filtro de pendentes, persistência após recarregar, reabertura e exclusão conferidos.
Layout | Revisão em computador (1366 px) e celular (390 px); sem rolagem horizontal nas telas verificadas.
Links e arquivos | Verificação automatizada dos destinos e âncoras locais; PDFs revisados visualmente.
Publicação HTTPS | Pendente de verificação remota nesta revisão.

Reproduzir os testes

O teste local revelou que arquivos .mjs eram servidos como texto neste Windows. Os módulos foram alterados para .js e a configuração type: module foi adicionada ao projeto. O fluxo foi novamente verificado no navegador após a correção.

Os testes validam os cenários descritos, não todos os navegadores ou situações possíveis. Falha de armazenamento é tratada no código; sua simulação em navegador não integra as evidências desta entrega.

BOOTCAMP I / 05

LinkedIn e apresentação

## LinkedIn e apresentação

Integração com o perfil profissional

O site e o README apontam para o LinkedIn existente. A inclusão do portfólio no próprio perfil permanece pendente e será realizada pelo estudante, conforme escolha feita durante a preparação. O texto completo para copiar está em documento/Integracao_LinkedIn.md.

**Título sugerido:** Study Hub TI - Portfólio acadêmico e planejador de estudos.
**Descrição:** Projeto desenvolvido no Bootcamp I de Ciência da Computação no CEUB para organizar atividades e documentar minha evolução. Inclui portfólio no GitHub Pages e planejador com JavaScript, armazenamento local e testes.

**Perfil profissional**
<link href="https://www.linkedin.com/in/lucas-coutinho-chaul-27a139268/" color="#245a4f">https://www.linkedin.com/in/lucas-coutinho-chaul-27a139268/</link>

Apresentação de cinco minutos

Tempo | Conteúdo e demonstração
--- | ---
0:00 - 0:40 | Perfil, contexto e objetivo do Study Hub.
0:40 - 1:30 | Estrutura do repositório e README de um projeto.
1:30 - 2:20 | Página publicada e materiais disponíveis.
2:20 - 3:25 | Planejador: adicionar, concluir, filtrar e recarregar.
3:25 - 4:20 | Commits, tags, testes e fluxo de colaboração.
4:20 - 5:00 | Contato, integração profissional e próximos passos.

**Slides e roteiro completo**
<link href="https://uscascus.github.io/Study-Hub-TI/materiais/apresentacao.html" color="#245a4f">https://uscascus.github.io/Study-Hub-TI/materiais/apresentacao.html</link>

Vídeo no YouTube: ainda não gravado/publicado. O roteiro inclui falas e momentos de demonstração; a duração final deve ser ajustada em ensaio com cronômetro. O link do vídeo precisa ser acrescentado antes da entrega definitiva.

BOOTCAMP I / 06

Critérios e finalização

## Critérios e finalização

Requisito do desafio | Evidência e estado
--- | ---
Planejamento e diretórios | Estrutura mantida e ampliada; planejamento e READMEs disponíveis.
Projeto web e versão 1.0 | Portfólio e planejador; commits e tags reais no GitHub.
Alterações enviadas | Branch preparada; envio remoto em andamento.
Documentação por projeto | README do portfólio, README do planejador e guia de contribuição.
Repositório público e Pages | Repositório público; site em preparação.
Integração com LinkedIn | Links no site prontos. Inclusão no perfil pendente pelo estudante.
Apresentação no YouTube | Slides e roteiro prontos. Gravação, publicação e URL pendentes.
Entrega individual em PDF | Este relatório, com estado real dos requisitos e links clicáveis.

Passos restantes antes do envio

1. Adicionar o projeto ao LinkedIn com o texto preparado e conferir o link salvo.
2. Gravar a apresentação, publicar no YouTube e testar a URL sem login.
3. Incluir o link do vídeo e a evidência do LinkedIn no relatório, atualizar o PDF e enviar no ambiente da disciplina até 17/10/2026 às 23h55.

Próximas evoluções

Adicionar trabalhos das próximas disciplinas e manter os READMEs atualizados. No planejador, avaliar edição de tarefas e exportação/importação de uma cópia dos dados. Nenhuma evolução futura é apresentada como funcionalidade já entregue.

Referências: enunciado da Entrega Intermediária do Bootcamp I; materiais da etapa inicial deste repositório; documentação oficial do GitHub Pages e da API de Pages.

**GitHub Pages - documentação oficial**
<link href="https://docs.github.com/en/pages" color="#245a4f">https://docs.github.com/en/pages</link>

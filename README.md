# Study Hub TI

Portfólio e espaço de organização acadêmica de **Lucas Coutinho**, estudante de **Ciência da Computação no CEUB**, turma A - 0726. Reúne projetos, atividades, documentação e um histórico de evolução durante o curso.

**[Acessar o portfólio](https://uscascus.github.io/Study-Hub-TI/)** · **[Experimentar o planejador](https://uscascus.github.io/Study-Hub-TI/projetos/planejador/)** · **[Entrega intermediária em PDF](entrega/Study_Hub_Etapa_Intermediaria_Lucas_Coutinho.pdf)**

## Projetos

| Projeto | Tipo | O que faz | Documentação |
| --- | --- | --- | --- |
| Study Hub TI / Portfólio web | Acadêmico, Bootcamp I | Apresenta perfil, projetos, percurso e materiais; publicado no GitHub Pages | [README do portfólio](02_Disciplinas_Atuais/Bootcamp_I/Projetos/Portfolio_Web/README.md) |
| Planejador de estudos | Pessoal | Adiciona tarefas com prazo opcional, permite concluir, filtrar e excluir; salva no navegador | [README do planejador](03_Projetos_e_Certificados/Planejador_de_Estudos/README.md) |

## Organização

```text
Study-Hub-TI/
├── 01_Apresentacao_e_Perfil/       # Perfil e foto
├── 02_Disciplinas_Atuais/          # Atividades e projetos acadêmicos
│   └── Bootcamp_I/
│       ├── Atividades_e_Entregas/  # Etapa inicial e intermediária
│       └── Projetos/Portfolio_Web/
├── 03_Projetos_e_Certificados/     # Projetos pessoais documentados
│   └── Planejador_de_Estudos/
├── 04_Recursos_e_Referencias/      # Referências utilizadas
├── docs/                         # Site publicado pelo GitHub Pages
│   ├── assets/                   # Estilos, foto e favicon
│   ├── materiais/                # PDFs e slides com roteiro
│   └── projetos/planejador/       # Código da aplicação pessoal
├── documento/                    # Documentos editáveis
├── entrega/                      # PDFs para entrega
├── scripts/                      # Verificação dos links locais
└── tests/                        # Testes do planejador
```

## Executar localmente

O site é estático e não precisa de instalação de pacotes. Com Python 3 instalado:

```sh
python -m http.server 8000 --directory docs
```

Abra `http://localhost:8000`. Use um servidor HTTP para carregar os módulos JavaScript do planejador; abrir o HTML diretamente por `file://` pode bloquear os módulos.

Com Node.js 18 ou superior e Python 3, valide o projeto:

```sh
node --test tests/planner.test.mjs
python scripts/check_links.py
```

## Versionamento e colaboração

A etapa intermediária é desenvolvida na branch `Pitu/bootcamp-intermediaria`, baseada no commit `d3c9894` da `main`. A publicação do GitHub Pages usa a pasta `/docs` desta branch. A `main` preserva a etapa anterior até autorização de integração.

- `v1.0.0`: primeira versão do portfólio e do planejador.
- `v1.1.0`: documentação, apresentação e entrega intermediária revisadas.
- Histórico e decisões: [CHANGELOG](CHANGELOG.md) e [planejamento](documento/Planejamento_Intermediaria.md).
- Contribuições: consulte [CONTRIBUTING.md](CONTRIBUTING.md). Sugestões e problemas podem ser registrados em [Issues](https://github.com/uscascus/Study-Hub-TI/issues).

## Materiais da etapa intermediária

- [Relatório editável](documento/Etapa_Intermediaria_Lucas_Coutinho.md)
- [Slides e roteiro de cinco minutos](docs/materiais/apresentacao.html)
- [Texto e orientações para integração no LinkedIn](documento/Integracao_LinkedIn.md)
- [Mapa de requisitos e verificação](02_Disciplinas_Atuais/Bootcamp_I/Atividades_e_Entregas/Etapa_Intermediaria/README.md)

O roteiro e os slides apoiam a gravação. A inclusão no perfil do LinkedIn e o vídeo no YouTube só devem ser tratados como concluídos quando houver evidência dos respectivos registros.

## Privacidade e limites

O portfólio usa apenas os dados de contato já presentes neste repositório. O planejador guarda tarefas no `localStorage`, sem servidor ou sincronização; limpar os dados do navegador remove as tarefas. Não publique credenciais, dados de terceiros ou materiais sem autorização. Esta versão não apresenta certificações ou experiências profissionais não comprovadas.

## Contato

- LinkedIn: [Lucas Coutinho](https://www.linkedin.com/in/lucas-coutinho-chaul-27a139268/)
- GitHub: [uscascus](https://github.com/uscascus)
- E-mail: [lucascoutinhoc.contato@gmail.com](mailto:lucascoutinhoc.contato@gmail.com)

from pathlib import Path
import argparse
import shutil
from html import escape, unescape
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, Preformatted
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--published', action='store_true')
args = parser.parse_args()
INK = colors.HexColor('#132c2b')
MUTED = colors.HexColor('#526360')
LIME = colors.HexColor('#d7ef8b')
PAPER = colors.HexColor('#f6f5ee')
LINE = colors.HexColor('#d5dbd0')
SITE = 'https://uscascus.github.io/Study-Hub-TI/'
REPO = 'https://github.com/uscascus/Study-Hub-TI/tree/Pitu/bootcamp-intermediaria'
PROFILE = 'https://www.linkedin.com/in/lucas-coutinho-chaul-27a139268/'
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Kicker', fontName='Helvetica-Bold', fontSize=9, leading=13, textColor=MUTED, spaceAfter=18))
styles.add(ParagraphStyle(name='TitleCustom', fontName='Helvetica', fontSize=40, leading=43, textColor=INK, spaceAfter=20))
styles.add(ParagraphStyle(name='H1Custom', fontName='Helvetica', fontSize=25, leading=29, textColor=INK, spaceAfter=18))
styles.add(ParagraphStyle(name='H2Custom', fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=INK, spaceBefore=17, spaceAfter=8))
styles.add(ParagraphStyle(name='BodyCustom', fontName='Helvetica', fontSize=10, leading=15, textColor=INK, spaceAfter=9))
styles.add(ParagraphStyle(name='SmallCustom', fontName='Helvetica', fontSize=8.5, leading=12, textColor=MUTED, spaceAfter=8))
styles.add(ParagraphStyle(name='CellCustom', fontName='Helvetica', fontSize=9, leading=13, textColor=INK))
styles.add(ParagraphStyle(name='MonoCustom', fontName='Courier', fontSize=8.2, leading=13, textColor=INK, backColor=PAPER, borderPadding=12, spaceAfter=14))
story = []
md = []

def p(text, style='BodyCustom'):
    story.append(Paragraph(text, styles[style]))
    clean = re.sub(r'<link href="([^"]+)"[^>]*>(.*?)</link>', lambda m: f'[{m[2]}]({m[1]})', text)
    clean = unescape(clean.replace('<b>', '**').replace('</b>', '**').replace('<br/>', '\n'))
    prefix = {'TitleCustom': '# ', 'H1Custom': '## ', 'H2Custom': '### '}.get(style, '')
    md.extend([prefix + clean, ''])

def heading(index, title):
    if story:
        story.append(PageBreak())
    p(f'BOOTCAMP I / {index:02d}', 'Kicker')
    p(title, 'H1Custom')

def sub(title):
    p(title, 'H2Custom')

def link(label, url):
    p(f'<b>{escape(label)}</b><br/><link href="{escape(url, quote=True)}" color="#245a4f">{escape(url)}</link>', 'SmallCustom')

def table(headers, rows, widths):
    vals = [[Paragraph(f'<b>{escape(x)}</b>', styles['CellCustom']) for x in headers]]
    vals += [[Paragraph(escape(x), styles['CellCustom']) for x in row] for row in rows]
    t = Table(vals, colWidths=widths, hAlign='LEFT', repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), LIME), ('VALIGN',(0,0),(-1,-1),'TOP'), ('TOPPADDING',(0,0),(-1,-1),10), ('BOTTOMPADDING',(0,0),(-1,-1),10), ('LEFTPADDING',(0,0),(-1,-1),10), ('RIGHTPADDING',(0,0),(-1,-1),10), ('LINEBELOW',(0,0),(-1,0),.7,INK), ('LINEBELOW',(0,1),(-1,-1),.4,LINE)]))
    story.append(t)
    md.extend([' | '.join(headers), ' | '.join(['---']*len(headers))] + [' | '.join(row) for row in rows] + [''])

p('CEUB / CIÊNCIA DA COMPUTAÇÃO / BOOTCAMP I', 'Kicker')
story.append(Spacer(1, 35))
p('Study Hub TI', 'TitleCustom')
p('Portfólio acadêmico<br/>com versionamento', 'H1Custom')
p('Entrega intermediária - Criação de Repositório com Versionamento', 'BodyCustom')
story.append(Spacer(1, 25))
table(['Estudante', 'Identificação'], [('Lucas Coutinho', 'Ciência da Computação - CEUB'), ('Turma A - 0726', 'Entrega individual - 15/10/2026')], [237, 250])
story.append(Spacer(1, 24))
p('O Study Hub reúne atividades, projetos e documentos em um repositório organizado. Nesta etapa, o planejamento inicial evolui para um portfólio web e uma aplicação pessoal, com histórico de versões e instruções de execução.')
link('Portfólio no GitHub Pages', SITE)
link('Código da etapa intermediária', REPO)
p('O site está publicado e o projeto foi adicionado ao meu LinkedIn. Ainda falta gravar e publicar a apresentação no YouTube.' if args.published else 'O site foi implementado e testado localmente. A publicação, a inclusão no LinkedIn e o vídeo no YouTube ainda estão em andamento.', 'SmallCustom')
p('Prazo indicado no enunciado: 17/10/2026, às 23h55.', 'SmallCustom')

heading(1, 'Planejamento e organização')
p('Criei o Study Hub para reunir minhas atividades e projetos em um lugar só. Mantive a estrutura da etapa inicial e acrescentei o portfólio web e o planejador de estudos. Assim consigo revisar o que estudei e apresentar meus trabalhos.')
tree = '''Study-Hub-TI/
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
`-- tests/'''
story.append(Preformatted(tree, styles['MonoCustom']))
md.extend(['```text', tree, '```', ''])
sub('Decisões de organização')
p('O portfólio web é o projeto acadêmico do Bootcamp I. O planejador é o projeto pessoal. Cada um possui README com objetivo, tecnologias, execução, decisões e limitações. A implementação executável fica em docs, raiz pública do GitHub Pages; a documentação de cada projeto permanece na área correspondente, evitando duplicação de código.')
sub('Manutenção')
p('Pretendo atualizar o repositório durante o semestre, separar os materiais por disciplina e registrar cada alteração em um commit. Cada projeto terá um README com instruções de uso e os principais aprendizados.')
link('Estrutura e instruções do repositório', REPO + '/README.md')

heading(2, 'Projetos implementados')
sub('Acadêmico: portfólio web')
p('Página em HTML e CSS com apresentação, interesses em back-end e segurança da informação, projetos, percurso, PDFs, slides e contato. O layout se adapta a computador e celular. A navegação inclui rótulos, foco visível e acesso direto ao conteúdo pelo teclado.')
shot = ROOT / 'documento/evidencias/portfolio-desktop.png'
if shot.exists():
    image = Image(str(shot))
    image.drawHeight = 487 * image.imageHeight / image.imageWidth
    image.drawWidth = 487
    story.append(image)
    p('Figura 1. Página inicial do Study Hub TI no GitHub Pages.', 'SmallCustom')
sub('Pessoal: planejador de estudos')
p('Aplicação em JavaScript que permite adicionar tarefas com prazo opcional, concluir e reabrir, filtrar por situação e excluir. Os dados ficam no localStorage do navegador. As regras de dados são separadas da interface para permitir testes sem dependências externas.')
link('Experimentar o planejador', SITE + 'projetos/planejador/')
p('Limites: não há conta, sincronização, backup, notificações ou edição de títulos. Limpar os dados do navegador remove as tarefas. Gravações simultâneas em duas abas podem sobrescrever alterações. Se o armazenamento falhar, um aviso informa que os dados da sessão não foram salvos.', 'SmallCustom')

heading(3, 'Versionamento e colaboração')
p('A etapa inicial ficou registrada no commit d3c9894 da main. Para desenvolver o site, usei a branch Pitu/bootcamp-intermediaria. Os commits registram as mudanças, e as tags permitem consultar cada versão.')
table(['Marco', 'Registro e finalidade'], [('Base anterior', 'd3c9894: etapa inicial preservada em main.'), ('Branch de trabalho', 'Pitu/bootcamp-intermediaria: desenvolvimento e publicação desta etapa.'), ('Versão 1.0.0', 'Primeira versão do portfólio, planejador e testes.'), ('Versão 1.1.0', 'Documentação, apresentação e relatório intermediário.'), ('Versão 1.1.1', 'Revisão dos textos do site e da entrega.'), ('Versão 1.1.2', 'Registro do projeto no LinkedIn e atualização do relatório.')], [125, 362])
sub('Fluxo de trabalho')
p('Antes de alterar os arquivos, confiro o estado do repositório e atualizo as referências remotas. Depois executo os testes, reviso as mudanças e faço o commit. O GitHub Pages publica a branch intermediária; a main mantém a etapa inicial.')
sub('Como colaborar')
p('Sugestões e problemas podem ser registrados nas issues. Para propor uma mudança, o guia CONTRIBUTING explica como criar uma branch, testar a alteração e abrir um pull request. A revisão inclui funcionamento, acessibilidade e links.')
link('Histórico de commits', 'https://github.com/uscascus/Study-Hub-TI/commits/Pitu/bootcamp-intermediaria/')
link('Versões e tags', 'https://github.com/uscascus/Study-Hub-TI/tags')
link('Guia de contribuição', REPO + '/CONTRIBUTING.md')

heading(4, 'Publicação e verificação')
p('O repositório é público. O GitHub Pages utiliza a pasta /docs da branch Pitu/bootcamp-intermediaria. Caminhos relativos permitem servir o site no subdiretório /Study-Hub-TI/. O arquivo .nojekyll mantém a publicação estática.')
table(['Verificação', 'Resultado'], [('Regras do planejador', '7 testes automatizados aprovados: inclusão, limites, datas, recuperação, filtros, conclusão e exclusão.'), ('Navegador', 'Inclusão com prazo, conclusão, filtro de pendentes, persistência após recarregar, reabertura e exclusão conferidos.'), ('Layout', 'Revisão em computador (1366 px) e celular (390 px); sem rolagem horizontal nas telas verificadas.'), ('Links e arquivos', 'Verificação automatizada dos destinos e âncoras locais; PDFs revisados visualmente.'), ('Publicação HTTPS', 'GitHub Pages publicado e respostas HTTP 200 conferidas.' if args.published else 'Pendente de verificação remota nesta revisão.')], [125, 362])
sub('Reproduzir os testes')
story.append(Preformatted('python -m http.server 8000 --directory docs\nnode --test tests/planner.test.mjs\npython scripts/check_links.py', styles['MonoCustom']))
p('O teste local revelou que arquivos .mjs eram servidos como texto neste Windows. Os módulos foram alterados para .js e a configuração type: module foi adicionada ao projeto. O fluxo foi novamente verificado no navegador após a correção.', 'SmallCustom')
p('Os testes automatizados cobrem as regras das tarefas. A persistência foi conferida no navegador. O bloqueio do armazenamento é tratado no código, mas ainda não foi simulado no navegador.', 'SmallCustom')

heading(5, 'LinkedIn e apresentação')
sub('Integração com o perfil profissional')
p('Adicionei o Study Hub à seção Projetos do meu LinkedIn em 15/10/2026, associado ao UniCEUB. A descrição apresenta o trabalho do Bootcamp I e inclui os endereços do portfólio e do código. O site e o README também têm um link para meu perfil.')
p('<b>Projeto:</b> Study Hub TI - Portfólio acadêmico e planejador de estudos.<br/><b>Descrição:</b> Projeto desenvolvido no Bootcamp I de Ciência da Computação no CEUB para organizar atividades e documentar minha evolução. Inclui portfólio no GitHub Pages e planejador com JavaScript, armazenamento local e testes.')
link('Projeto no perfil profissional', PROFILE + 'details/projects/')
sub('Apresentação de cinco minutos')
table(['Tempo', 'Conteúdo e demonstração'], [('0:00 - 0:40', 'Perfil, contexto e objetivo do Study Hub.'), ('0:40 - 1:30', 'Estrutura do repositório e README de um projeto.'), ('1:30 - 2:20', 'Página publicada e materiais disponíveis.'), ('2:20 - 3:25', 'Planejador: adicionar, concluir, filtrar e recarregar.'), ('3:25 - 4:20', 'Commits, tags, testes e fluxo de colaboração.'), ('4:20 - 5:00', 'Contato, integração profissional e próximos passos.')], [105, 382])
link('Slides e roteiro completo', SITE + 'materiais/apresentacao.html')
p('Ainda falta gravar e publicar o vídeo no YouTube. Organizei a apresentação em seis partes, com demonstração do repositório e do planejador. Depois da gravação, vou incluir o link neste relatório.', 'SmallCustom')

heading(6, 'Critérios e finalização')
table(['Requisito do desafio', 'Evidência e estado'], [('Planejamento e diretórios', 'Estrutura mantida e ampliada; planejamento e READMEs disponíveis.'), ('Projeto web e versão 1.0', 'Portfólio e planejador, com commits e tags no GitHub.'), ('Alterações enviadas', 'Branch intermediária publicada, com revisão na versão 1.1.2.' if args.published else 'Branch preparada; envio remoto em andamento.'), ('Documentação por projeto', 'README do portfólio, README do planejador e guia de contribuição.'), ('Repositório público e Pages', 'Repositório público e site HTTPS verificado.' if args.published else 'Repositório público; site em preparação.'), ('Integração com LinkedIn', 'Projeto adicionado ao perfil, com descrição e endereços do portfólio e do código.'), ('Apresentação no YouTube', 'Slides e roteiro prontos. Gravação, publicação e URL pendentes.'), ('Entrega individual em PDF', 'Relatório com os projetos, testes e links da entrega.')], [165, 322])
sub('Falta concluir')
p('1. Gravar e publicar a apresentação no YouTube.<br/>2. Incluir o link do vídeo neste relatório e enviar a entrega até 17/10/2026 às 23h55.')
sub('Próximas evoluções')
p('Quero acrescentar os trabalhos das próximas disciplinas e manter os READMEs atualizados. No planejador, pretendo estudar como editar tarefas e exportar uma cópia da lista.')
p('Referências: enunciado da Entrega Intermediária do Bootcamp I; materiais da etapa inicial deste repositório; documentação oficial do GitHub Pages e da API de Pages.', 'SmallCustom')
link('GitHub Pages - documentação oficial', 'https://docs.github.com/en/pages')

def footer(c, doc):
    c.saveState()
    width, height = A4
    c.setStrokeColor(LINE)
    c.line(54, 46, width-54, 46)
    c.setFont('Helvetica', 8)
    c.setFillColor(MUTED)
    c.drawString(54, 32, 'LUCAS COUTINHO  /  STUDY HUB TI  /  15.10.2026')
    c.drawRightString(width-54, 32, f'{doc.page:02d}')
    c.restoreState()

target = ROOT / 'entrega/Study_Hub_Etapa_Intermediaria_Lucas_Coutinho.pdf'
doc = SimpleDocTemplate(str(target), pagesize=A4, leftMargin=54, rightMargin=54, topMargin=52, bottomMargin=65, title='Study Hub TI - Entrega Intermediária', author='Lucas Coutinho', subject='Bootcamp I - Repositório com versionamento')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
(ROOT / 'documento/Etapa_Intermediaria_Lucas_Coutinho.md').write_text('\n'.join(md), encoding='utf-8')
shutil.copy2(target, ROOT / 'docs/materiais/etapa-intermediaria.pdf')
print(target)

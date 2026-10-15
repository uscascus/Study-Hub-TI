"""Build the intermediate report. Requires reportlab; no network or credentials.

Run from any directory. Add --published only after checking the live Pages site.
"""
from pathlib import Path
import argparse
import shutil
from html import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, Preformatted, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
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
md = ['# Study Hub TI - Entrega intermediária', '', 'Lucas Coutinho | Ciência da Computação | CEUB | Turma A - 0726', '', 'Data: 15/10/2026', '']

def p(text, style='BodyCustom'):
    story.append(Paragraph(text, styles[style]))
    md.extend([text.replace('<b>', '**').replace('</b>', '**').replace('<br/>', '\n'), ''])

def heading(index, title):
    if story:
        story.append(PageBreak())
    p(f'BOOTCAMP I / {index:02d}', 'Kicker')
    p(title, 'H1Custom')
    md.extend(['## ' + title, ''])

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
p('Estado desta entrega: site publicado e verificado. A inclusão do projeto no LinkedIn e a gravação/publicação do vídeo no YouTube permanecem pendentes.' if args.published else 'Estado desta revisão: implementação e testes locais concluídos; publicação web em preparação. LinkedIn e vídeo no YouTube pendentes.', 'SmallCustom')
p('Prazo indicado no enunciado: 17/10/2026, às 23h55.', 'SmallCustom')

heading(1, 'Planejamento e organização')
p('Objetivo: centralizar minha produção acadêmica e pessoal, facilitar revisões e apresentar projetos reais como parte do perfil profissional. O repositório existente foi aproveitado para preservar o histórico e os materiais da etapa inicial.')
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
p('Usar nomes claros, atualizar materiais durante o semestre e criar commits com um objetivo específico. Não publicar credenciais ou dados de terceiros. Certificados, experiências e colaboração só serão apresentados quando existirem evidências reais.')
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
    p('Figura 1. Página inicial do portfólio em revisão local. Conteúdo e foto partem dos materiais já existentes no Study Hub.', 'SmallCustom')
sub('Pessoal: planejador de estudos')
p('Aplicação em JavaScript que permite adicionar tarefas com prazo opcional, concluir e reabrir, filtrar por situação e excluir. Os dados ficam no localStorage do navegador. As regras de dados são separadas da interface para permitir testes sem dependências externas.')
link('Experimentar o planejador', SITE + 'projetos/planejador/')
p('Limites: não há conta, sincronização, backup, notificações ou edição de títulos. Limpar os dados do navegador remove as tarefas. Gravações simultâneas em duas abas podem sobrescrever alterações. Se o armazenamento falhar, um aviso informa que os dados da sessão não foram salvos.', 'SmallCustom')

heading(3, 'Versionamento e colaboração')
p('O remoto foi atualizado antes do desenvolvimento. A base é o commit d3c9894 de origin/main, que consolidava a etapa inicial. Não havia alterações locais, outras branches remotas ativas ou pull requests abertos na checagem inicial.')
table(['Marco', 'Registro e finalidade'], [('Base anterior', 'd3c9894: etapa inicial preservada em main.'), ('Branch de trabalho', 'Pitu/bootcamp-intermediaria: desenvolvimento e publicação desta etapa.'), ('Versão 1.0.0', 'Primeira versão do portfólio, planejador e testes.'), ('Versão 1.1.0', 'Evolução da documentação, apresentação e relatório intermediário.')], [125, 362])
sub('Fluxo de trabalho')
p('Conferir git status e atualizar referências; trabalhar na branch ativa; executar os testes; revisar o diff; criar commits específicos e enviar a branch para o GitHub. As tags identificam versões recuperáveis. A main só recebe integração mediante autorização específica.')
sub('Colaboração preparada')
p('O guia CONTRIBUTING descreve abertura de issues, criação de branches, testes e pull requests. A revisão deve conferir funcionamento, acessibilidade, links e ausência de credenciais. Este é um trabalho individual; o fluxo está documentado, sem alegar participação ou revisão de terceiros.')
link('Histórico de commits', 'https://github.com/uscascus/Study-Hub-TI/commits/Pitu/bootcamp-intermediaria/')
link('Versões e tags', 'https://github.com/uscascus/Study-Hub-TI/tags')
link('Guia de contribuição', REPO + '/CONTRIBUTING.md')

heading(4, 'Publicação e verificação')
p('O repositório é público. O GitHub Pages utiliza a pasta /docs da branch Pitu/bootcamp-intermediaria. Caminhos relativos permitem servir o site no subdiretório /Study-Hub-TI/. O arquivo .nojekyll mantém a publicação estática.')
table(['Verificação', 'Resultado'], [('Regras do planejador', '7 testes automatizados aprovados: inclusão, limites, datas, recuperação, filtros, conclusão e exclusão.'), ('Navegador', 'Inclusão com prazo, conclusão, filtro de pendentes, persistência após recarregar, reabertura e exclusão conferidos.'), ('Layout', 'Revisão em computador (1366 px) e celular (390 px); sem rolagem horizontal nas telas verificadas.'), ('Links e arquivos', 'Verificação automatizada dos destinos e âncoras locais; PDFs revisados visualmente.'), ('Publicação HTTPS', 'GitHub Pages publicado e respostas HTTP 200 conferidas.' if args.published else 'Pendente de verificação remota nesta revisão.')], [125, 362])
sub('Reproduzir os testes')
story.append(Preformatted('python -m http.server 8000 --directory docs\nnode --test tests/planner.test.mjs\npython scripts/check_links.py', styles['MonoCustom']))
p('O teste local revelou que arquivos .mjs eram servidos como texto neste Windows. Os módulos foram alterados para .js e a configuração type: module foi adicionada ao projeto. O fluxo foi novamente verificado no navegador após a correção.', 'SmallCustom')
p('Os testes validam os cenários descritos, não todos os navegadores ou situações possíveis. Falha de armazenamento é tratada no código; sua simulação em navegador não integra as evidências desta entrega.', 'SmallCustom')

heading(5, 'LinkedIn e apresentação')
sub('Integração com o perfil profissional')
p('O site e o README apontam para o LinkedIn existente. A inclusão do portfólio no próprio perfil permanece pendente e será realizada pelo estudante, conforme escolha feita durante a preparação. O texto completo para copiar está em documento/Integracao_LinkedIn.md.')
p('<b>Título sugerido:</b> Study Hub TI - Portfólio acadêmico e planejador de estudos.<br/><b>Descrição:</b> Projeto desenvolvido no Bootcamp I de Ciência da Computação no CEUB para organizar atividades e documentar minha evolução. Inclui portfólio no GitHub Pages e planejador com JavaScript, armazenamento local e testes.')
link('Perfil profissional', PROFILE)
sub('Apresentação de cinco minutos')
table(['Tempo', 'Conteúdo e demonstração'], [('0:00 - 0:40', 'Perfil, contexto e objetivo do Study Hub.'), ('0:40 - 1:30', 'Estrutura do repositório e README de um projeto.'), ('1:30 - 2:20', 'Página publicada e materiais disponíveis.'), ('2:20 - 3:25', 'Planejador: adicionar, concluir, filtrar e recarregar.'), ('3:25 - 4:20', 'Commits, tags, testes e fluxo de colaboração.'), ('4:20 - 5:00', 'Contato, integração profissional e próximos passos.')], [105, 382])
link('Slides e roteiro completo', SITE + 'materiais/apresentacao.html')
p('Vídeo no YouTube: ainda não gravado/publicado. O roteiro inclui falas e momentos de demonstração; a duração final deve ser ajustada em ensaio com cronômetro. O link do vídeo precisa ser acrescentado antes da entrega definitiva.', 'SmallCustom')

heading(6, 'Critérios e finalização')
table(['Requisito do desafio', 'Evidência e estado'], [('Planejamento e diretórios', 'Estrutura mantida e ampliada; planejamento e READMEs disponíveis.'), ('Projeto web e versão 1.0', 'Portfólio e planejador; commits e tags reais no GitHub.'), ('Alterações enviadas', 'Branch intermediária publicada, com evolução até a versão 1.1.0.' if args.published else 'Branch preparada; envio remoto em andamento.'), ('Documentação por projeto', 'README do portfólio, README do planejador e guia de contribuição.'), ('Repositório público e Pages', 'Repositório público e site HTTPS verificado.' if args.published else 'Repositório público; site em preparação.'), ('Integração com LinkedIn', 'Links no site prontos. Inclusão no perfil pendente pelo estudante.'), ('Apresentação no YouTube', 'Slides e roteiro prontos. Gravação, publicação e URL pendentes.'), ('Entrega individual em PDF', 'Este relatório, com estado real dos requisitos e links clicáveis.')], [165, 322])
sub('Passos restantes antes do envio')
p('1. Adicionar o projeto ao LinkedIn com o texto preparado e conferir o link salvo.<br/>2. Gravar a apresentação, publicar no YouTube e testar a URL sem login.<br/>3. Incluir o link do vídeo e a evidência do LinkedIn no relatório, atualizar o PDF e enviar no ambiente da disciplina até 17/10/2026 às 23h55.')
sub('Próximas evoluções')
p('Adicionar trabalhos das próximas disciplinas e manter os READMEs atualizados. No planejador, avaliar edição de tarefas e exportação/importação de uma cópia dos dados. Nenhuma evolução futura é apresentada como funcionalidade já entregue.')
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

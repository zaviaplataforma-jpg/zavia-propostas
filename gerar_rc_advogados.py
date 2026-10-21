"""Gera rc-advogados/index.html a partir do formulário de RC (rc/index.html), com os campos que as seguradoras pedem para advogado."""
import os
base = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(base, "rc", "index.html"), encoding="utf-8").read()

def rep(old, new):
    global s
    assert s.count(old) == 1, old[:80]
    s = s.replace(old, new)

rep("<title>Proposta de RC Profissional · Zavia Seguros</title>", "<title>RC Profissional para advogados · Zavia Seguros</title>")
rep('content="Preencha em 1 minuto e receba uma proposta de seguro de Responsabilidade Civil Profissional para o seu escritório."',
    'content="Preencha em 1 minuto e receba uma proposta de seguro de Responsabilidade Civil Profissional para advogados."')
rep("<h1>Receba uma proposta de <em>RC Profissional</em> para o seu escritório</h1>", "<h1>Receba uma proposta de <em>RC Profissional</em> para advogados</h1>")
rep("""    <li>Defesa e indenização quando um cliente cobra um erro, uma omissão ou um prazo perdido</li>
    <li>Custos com advogado e acordo, sem tirar do caixa do escritório</li>""",
    """    <li>Defesa e indenização quando um cliente alega erro, omissão ou perda de prazo</li>
    <li>Para quem advoga sozinho, em sociedade ou como associado</li>""")
rep("""    <label><b>Nome do escritório</b><input name="escritorio" autocomplete="organization" maxlength="100" required></label>""",
    """    <label><b>Escritório ou sociedade</b> (se tiver)<input name="escritorio" autocomplete="organization" maxlength="100"></label>""")
rep("""    <h2>Sobre o escritório</h2>
    <div class="dois">
      <label><b>Profissionais</b>""",
    """    <h2>Sobre a sua atuação</h2>
    <label><b>Como você atua</b>
      <select name="atuacao" required><option value="">Escolha</option><option>Advogado autônomo</option><option>Sócio de escritório</option><option>Associado ou contratado de escritório</option><option>Jurídico de empresa</option></select></label>
    <div class="dois">
      <label><b>Área principal</b>
        <select name="area" required><option value="">Escolha</option><option>Cível</option><option>Trabalhista</option><option>Tributária</option><option>Empresarial</option><option>Família e sucessões</option><option>Previdenciária</option><option>Consumidor</option><option>Criminal</option><option>Outra</option></select></label>
      <label><b>Inscrito na OAB há</b>
        <select name="oab" required><option value="">Escolha</option><option>Menos de 2 anos</option><option>2 a 5 anos</option><option>6 a 10 anos</option><option>Mais de 10 anos</option><option>Ainda não inscrito</option></select></label>
    </div>
    <div class="dois">
      <label><b>Advogados no escritório</b>""")
rep("<label><b>Faturamento anual do escritório</b>", "<label><b>Faturamento anual (seu ou do escritório)</b>")
rep('''["nome", "whatsapp", "escritorio", "cnpj", "cidade", "profissionais", "clientes", "faturamento", "limite"].forEach''',
    '''["nome", "whatsapp", "escritorio", "cnpj", "cidade", "atuacao", "area", "oab", "profissionais", "clientes", "faturamento", "limite"].forEach''')
rep('''["nome", "escritorio", "cidade", "profissionais", "clientes", "faturamento", "limite"].forEach(function (k) { marcar''',
    '''["nome", "cidade", "atuacao", "area", "oab", "profissionais", "clientes", "faturamento", "limite"].forEach(function (k) { marcar''')
rep('''      "Quero uma proposta de RC Profissional.",''', '''      "Quero uma proposta de RC Profissional para advogados.",''')
rep('''      "Escritório: " + d.escritorio,''', '''      d.escritorio ? "Escritório: " + d.escritorio : null,''')
rep('''      "Profissionais: " + d.profissionais,''', '''      "Atuação: " + d.atuacao,
      "Área: " + d.area,
      "OAB: " + d.oab,
      "Profissionais: " + d.profissionais,''')
rep('''      "Código: ZV-RC" + ''', '''      "Código: ZV-RCADV" + ''')

os.makedirs(os.path.join(base, "rc-advogados"), exist_ok=True)
open(os.path.join(base, "rc-advogados", "index.html"), "w", encoding="utf-8").write(s)
print("ok")


import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="Validade Estendida", layout="centered")
st.title("📦 Calculadora de Validade Estendida")

# 👇 DICIONÁRIO DE ITENS
from validade_sem_dia_ajustada import itens  # ou copie os itens diretamente aqui, se estiver usando local

# 🔎 CAMPO DE BUSCA
st.subheader("🔎 Buscar produto pelo nome:")
filtro = st.text_input("Digite parte do nome do produto...").upper()
opcoes_filtradas = [nome for nome in sorted(itens.keys()) if filtro in nome]
produto = st.selectbox("Produto:", opcoes_filtradas if filtro else sorted(itens.keys()))

validade_padrao = itens[produto]
anos, meses, dias = validade_padrao["anos"], validade_padrao["meses"], validade_padrao["dias"]

# ⚙️ AJUSTE MANUAL
ajuste_manual = st.checkbox("Deseja ajustar manualmente a validade deste item?")
if ajuste_manual:
    col1, col2, col3 = st.columns(3)
    with col1:
        anos = st.number_input("Anos", min_value=0, step=1, key="anos_custom")
    with col2:
        meses = st.number_input("Meses", min_value=0, step=1, key="meses_custom")
    with col3:
        dias = st.number_input("Dias", min_value=0, step=1, key="dias_custom")

val_texto = []
if anos: val_texto.append(f"{anos} ano{'s' if anos > 1 else ''}")
if meses: val_texto.append(f"{meses} mês{'es' if meses > 1 else ''}")
if dias: val_texto.append(f"{dias} dia{'s' if dias > 1 else ''}")
st.info("⏳ Validade usada: **" + " e ".join(val_texto) + "**")

# 📌 BASE DE CÁLCULO
opcao_base = st.radio("📌 Qual base de data você deseja usar?", [
    "Usar o início do mês informado",
    "Usar a data de hoje se já estiver dentro do mês informado"
])

# 📅 DATA DE FABRICAÇÃO
if not ajuste_manual:
    st.subheader("📅 Informe o mês e o ano de fabricação da matéria-prima:")
    col1, col2 = st.columns(2)
    with col1:
        mes = st.selectbox("Mês", list(range(1, 13)), format_func=lambda m: datetime(2000, m, 1).strftime('%B').capitalize())
    with col2:
        ano = st.number_input("Ano", min_value=2020, max_value=2035, step=1)

# ▶️ BOTÃO CALCULAR
if st.button("Calcular validade"):
    if ajuste_manual:
        data_base = datetime.today()
    else:
        data_base = datetime(int(ano), int(mes), 1)
        if opcao_base == "Usar a data de hoje se já estiver dentro do mês informado":
            hoje = datetime.today()
            if (int(ano), int(mes)) <= (hoje.year, hoje.month):
                data_base = hoje

    data_vencimento = data_base + relativedelta(years=anos, months=meses, days=dias)
    dias_ate_nova = (data_vencimento - datetime.today()).days

    st.markdown(f"📅 **Nova validade (mês/ano):** {data_vencimento.strftime('%m/%Y')}")
    st.markdown(f"⏳ **Dias restantes até o novo vencimento:** {dias_ate_nova} dias")

    # 🧾 TABELA DE RESULTADO
    dados_exportar = pd.DataFrame([{
        "Produto": produto,
        "Data base usada": data_base.strftime('%d/%m/%Y'),
        "Validade aplicada": " e ".join(val_texto),
        "Nova validade": data_vencimento.strftime('%d/%m/%Y'),
        "Dias restantes": dias_ate_nova
    }])
    st.dataframe(dados_exportar)

    # 📥 EXPORTAR EXCEL
    excel_buffer = BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
        dados_exportar.to_excel(writer, index=False, sheet_name="Validades")

    st.download_button(
        label="📥 Baixar cálculo em Excel",
        data=excel_buffer.getvalue(),
        file_name=f"validade_{produto[:30].replace(' ', '_')}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# ➕ NOVO ITEM NA SIDEBAR
st.sidebar.subheader("➕ Adicionar novo item (sessão atual)")
with st.sidebar.form("form_novo_item"):
    novo_nome = st.text_input("Nome do novo produto:")
    col_a, col_m, col_d = st.columns(3)
    with col_a:
        novo_anos = st.number_input("Anos", min_value=0, step=1, key="anos_novo")
    with col_m:
        novo_meses = st.number_input("Meses", min_value=0, step=1, key="meses_novo")
    with col_d:
        novo_dias = st.number_input("Dias", min_value=0, step=1, key="dias_novo")
    submit = st.form_submit_button("Adicionar")
    if submit and novo_nome.strip():
        itens[novo_nome.strip().upper()] = {
            "anos": int(novo_anos),
            "meses": int(novo_meses),
            "dias": int(novo_dias)
        }
        st.sidebar.success("Item adicionado com sucesso!")

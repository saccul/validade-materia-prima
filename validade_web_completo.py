
import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="Validade de Matéria-Prima", layout="centered")
st.title("📦 Verificador de Validade de Matéria-Prima")

# Lista inicial de itens fixos (pode ser expandida)
itens = {
    "AÇAFRÃO 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "LEMON HERBIS 6X20G LENA C&E": {"anos": 1, "meses": 5, "dias": 0},
    "PÁPRICA PICANTE 6X20G LENA C&E": {"anos": 1, "meses": 5, "dias": 0},
}

# 🔸 Adicionar novo item
st.sidebar.subheader("➕ Adicionar novo item (temporário)")
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

# 🔸 ESCOLHA DO PRODUTO
st.subheader("🧾 Selecione o item da matéria-prima:")
produto = st.selectbox("Produto:", sorted(itens.keys()))

# 🔸 Validar se vai usar a validade padrão ou personalizada
validade_padrao = itens[produto]
anos, meses, dias = validade_padrao["anos"], validade_padrao["meses"], validade_padrao["dias"]

if st.checkbox("Desejo ajustar manualmente a validade deste item"):
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

# 🔸 DATA DE FABRICAÇÃO
st.subheader("📅 Informe o mês e ano de fabricação:")
col1, col2 = st.columns(2)
with col1:
    mes = st.selectbox("Mês", list(range(1, 13)), format_func=lambda m: datetime(2000, m, 1).strftime('%B').capitalize())
with col2:
    ano = st.number_input("Ano", min_value=2020, max_value=2035, step=1)

# 🔸 CÁLCULO FINAL
if st.button("Calcular validade"):
    data_fabricacao = datetime(ano, mes, 1)
    data_vencimento = data_fabricacao + relativedelta(years=anos, months=meses, days=dias)
    hoje = datetime.today()
    dias_restantes = (data_vencimento - hoje).days

    st.markdown(f"📆 **Data de vencimento:** {data_vencimento.strftime('%d/%m/%Y')}")
    if dias_restantes < 0:
        st.error("❌ Produto VENCIDO")
    elif dias_restantes <= 7:
        st.warning(f"⚠️ Próximo do vencimento! Restam {dias_restantes} dias")
    else:
        st.success(f"✅ Produto dentro do prazo! Restam {dias_restantes} dias")

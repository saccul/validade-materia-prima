
import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="Validade Estendida", layout="centered")
st.title("📦 Calculadora de Validade Estendida")

# Lista de itens com validade padrão atualizada
itens = {
    "AÇAFRÃO 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "ALECRIM 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "ALHO FRITO GRANULADAO 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "ALHO GRANULADAO 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "BICARBONATO SODIO 6X100G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CEBOLA GRANULADA 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "CHIMICHURRI  6X20G LENAC&E": {"anos": 1, "meses": 6, "dias": 0},
    "CHIMICHURRI S/ PIMENTA 6X20G LENAC&E": {"anos": 1, "meses": 6, "dias": 0},
    "COENTRO SEMENTE 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CONDIMENTO NOZ MOSCADA LENA 6X20G C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CRAVO EM FLOR 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CRAVO EM PÓ 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CURRY 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "ERVAS FINAS 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "LEMON HERBS LENA 6X20g": {"anos": 1, "meses": 6, "dias": 0},
    "LEMON PEPPER 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "LOURO FOLHAS  6X10G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "MANJERICÃO 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "MOSTARDA MOIDA 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "OREGANO 6X15G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "PAPRICA DEFUMADA LENA C&E 6X20G": {"anos": 1, "meses": 6, "dias": 0},
    "PAPRICA DOCE 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "PAPRICA PICANTE 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "PIMENTA CALABRESA 6X10G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "PIMENTA DO REINO EM GRÃOS 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "PIMENTA DO REINO EM PÓ 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "SALSA DESIDRATADA 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "TEMPERO ANA MARIA  6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "TEMPERO BAIANO  6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "TEMPERO COMINHO PÓ 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "TEMPERO EDU GUEDES 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "TOMILHO 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "NOZ MOSCADA GRÃO LENA 6X10G C&E": {"anos": 2, "meses": 0, "dias": 0},
    "COMINHO COM PIMENTA  6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "TEMPERO PEGA MARIDO 6X20G LENA": {"anos": 1, "meses": 6, "dias": 0},
    "GUARANÁ EM PÓ 6X50G LENA": {"anos": 1, "meses": 6, "dias": 0},
}


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

st.subheader("🧾 Selecione o produto:")
produto = st.selectbox("Produto:", sorted(itens.keys()))

validade_padrao = itens[produto]
anos, meses, dias = validade_padrao["anos"], validade_padrao["meses"], validade_padrao["dias"]

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

if not ajuste_manual:
    st.subheader("📅 Informe o mês e o ano de fabricação da matéria-prima:")
    col1, col2 = st.columns(2)
    with col1:
        mes = st.selectbox("Mês", list(range(1, 13)), format_func=lambda m: datetime(2000, m, 1).strftime('%B').capitalize())
    with col2:
        ano = st.number_input("Ano", min_value=2020, max_value=2035, step=1)

if st.button("Calcular validade"):
    if ajuste_manual:
        data_base = datetime.today()
    else:
        data_base = datetime(ano, mes, 1)
    data_vencimento = data_base + relativedelta(years=anos, months=meses, days=dias)
    dias_ate_nova = (data_vencimento - datetime.today()).days

    st.markdown(f"📅 **Nova data de vencimento:** {data_vencimento.strftime('%d/%m/%Y')}")
    st.markdown(f"⏳ **Dias restantes até o novo vencimento:** {dias_ate_nova} dias")

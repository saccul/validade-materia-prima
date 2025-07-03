
import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="Validade Estendida", layout="centered")
st.title("📦 Calculadora de Validade Estendida")

itens = {
    "127 - AÇAFRÃO 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "83 - ALECRIM 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "175 - ALHO FRITO GRANULADO 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "169 - ALHO GRANULADAO 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "210 - BICARBONATO SODIO 6X100G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "170 - CEBOLA GRANULADA 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "216 - CHIMICHURRI  6X20G LENAC&E": {"anos": 1, "meses": 6, "dias": 0},
    "209 - CHIMICHURRI S/ PIMENTA 6X20G LENAC&E": {"anos": 1, "meses": 6, "dias": 0},
    "99 - COENTRO SEMENTE 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "195 - CONDIMENTO NOZ MOSCADA LENA 6X20G C&E": {"anos": 2, "meses": 0, "dias": 0},
    "93 - CRAVO EM FLOR 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "92 - CRAVO EM PÓ 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "94 - CURRY 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "101 - ERVAS FINAS 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "315 - LEMON HERBS LENA 6X20g": {"anos": 1, "meses": 6, "dias": 0},
    "277 - LEMON PEPPER 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "100 - LOURO FOLHAS  6X10G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "279 - MANJERICÃO 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "165 - MOSTARDA MOIDA 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "64 - OREGANO 6X15G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "200 - PAPRICA DEFUMADA LENA C&E 6X20G": {"anos": 1, "meses": 6, "dias": 0},
    "95 - PAPRICA DOCE 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "96 - PAPRICA PICANTE 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "118 - PIMENTA CALABRESA 6X10G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "63 - PIMENTA DO REINO EM GRÃOS 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "12 - PIMENTA DO REINO EM PÓ 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "102 - SALSA DESIDRATADA 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "217 - TEMPERO ANA MARIA  6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "126 - TEMPERO BAIANO  6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "208 - TEMPERO COMINHO PÓ 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "303 - TEMPERO EDU GUEDES 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "313 - TOMILHO 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "328 - NOZ MOSCADA GRÃO LENA 6X10G C&E": {"anos": 2, "meses": 0, "dias": 0},
    "323 - COMINHO COM PIMENTA  6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "354 - TEMPERO PEGA MARIDO 6X20G LENA": {"anos": 1, "meses": 6, "dias": 0},
    "322 - GUARANÁ EM PÓ 6X50G LENA": {"anos": 1, "meses": 6, "dias": 0},
    "168 - CANELA CASCA 6 CM PREMIUM 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "87 - CANELA MOIDA 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "177 - CHA CAPIM CIDREIRA LENA C&E 6X10G": {"anos": 1, "meses": 6, "dias": 0},
    "85 - CHA DE BOLDO 6X10G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "86 - CHA DE CAMOMILA 6X10G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "88 - CHA DE ENDRO SEMENTE 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "158 - CHA EUCALIPTO LENA C&E 6X10G": {"anos": 1, "meses": 6, "dias": 0},
    "196 - CHA HIBISCO FLOR LENA 6X10G": {"anos": 1, "meses": 6, "dias": 0},
    "265 - CHA MACELA LENA C&E 6X20G": {"anos": 1, "meses": 6, "dias": 0},
    "219 - CHIA SEMENTE 6X50G LENA": {"anos": 1, "meses": 6, "dias": 0},
    "250 - ERVA DOCE 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "89 - ERVA DOCE MOIDA 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "90 - GENGIBRE PÓ 6X20G LENA C&E": {"anos": 1, "meses": 6, "dias": 0},
    "338 - GENGIBRE COM LIMÃO LENA 6X20G": {"anos": 1, "meses": 6, "dias": 0},
    "339 - GENGIBRE COM LARANJA LENA 6X20G": {"anos": 1, "meses": 6, "dias": 0},
    "162 - HORTELA LENA C&E 6X20G": {"anos": 1, "meses": 6, "dias": 0},
    "355 - CHA VERDE 6X15G LENA": {"anos": 1, "meses": 6, "dias": 0},
    "356 - CHA ERVA CIDREIRA 6X10G LENA": {"anos": 1, "meses": 6, "dias": 0},
    "269 - AÇAFRÃO LENA FR 6X60g": {"anos": 2, "meses": 0, "dias": 0},
    "271 - CANELA EM PÓ LENA FR 6X60G": {"anos": 2, "meses": 0, "dias": 0},
    "272 - OREGANO LENA FR 6X20G": {"anos": 2, "meses": 0, "dias": 0},
    "273 - PIMENTA DO REINO MOÍDA LENA FR 6X52G": {"anos": 2, "meses": 0, "dias": 0},
    "481 - ALHO GRANULADO FRASCO LENA 6X60G": {"anos": 1, "meses": 10, "dias": 0},
    "482 - ALHO FRITO GRANULADO FRASCO LENA 6X60G": {"anos": 1, "meses": 10, "dias": 0},
    "483 - TEMPERO ANA MARIA FRASCO LENA 6X80G": {"anos": 1, "meses": 10, "dias": 0},
    "485 - LEMON PEPPER FRASCO LENA 6X80G LENA": {"anos": 1, "meses": 10, "dias": 0},
    "484 - TEMPERO EDU GUEDES FRASCO LENA 6X80G": {"anos": 1, "meses": 10, "dias": 0},
    "486 - PAPRICA DEFUMADA FRASCO LENA 6X80G": {"anos": 1, "meses": 10, "dias": 0},
    "487 - PAPRICA DOCE FRASCO LENA 6X80G": {"anos": 1, "meses": 10, "dias": 0},
    "488 - PAPRICA PICANTE FRASCO LENA 6X80G": {"anos": 1, "meses": 10, "dias": 0},
    "334 - CANELA POTE TRADICIONAL (PURA) 6X30g": {"anos": 2, "meses": 0, "dias": 0},
    "372 - FARINHA DE LINHACA DOURADA LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "360 - OREGANO LENA 4X120G": {"anos": 2, "meses": 0, "dias": 0},
    "361 - AÇAFRÃO 4X250G LENA": {"anos": 2, "meses": 0, "dias": 0},
    "374 - GERGELIM BRANCO LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "373 - GERGELIM COM CASCA LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "370 - COCO EM FLOCOS LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "369 - COCO RALADO LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "358 - FARINHA COCO BRANCA LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "357 - LEITE COCO PO LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "396 - CACAU EM PÓ 100% LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "421 - FARINHA DE AVEIA INTEGRAL LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "422 - FARINHA DE AVEIA SEM GLÚTEN LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "430 - AVEIA EM FLOCOS S/GLUTEN FINA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "431 - AVEIA EM FLOCOS GROSSA LENA S/GLUTEN 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "423 - FARINHA DE BERIJELA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "424 - FARINHA DE CENOURA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "410 - FARINHA DE CHIA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "418 - FARINHA DE MACA PERUANA PRETA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "419 - FARINHA DE UVA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "417 - SEMENTE LINHAÇA DOURADA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "420 - FARINHA DE QUINOA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "425 - FARINHA DE LINHACA MARROM LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "432 - FARINHA DE BETERRABA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
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


# Nova opção: usuário escolhe a base de cálculo
opcao_base = st.radio("📌 Qual base de data você deseja usar?", [
    "Usar o início do mês informado",
    "Usar a data de hoje se já estiver dentro do mês informado"
])

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
        
    data_base = datetime(int(ano), int(mes), 1)
    if opcao_base == "Usar a data de hoje se já estiver dentro do mês informado":
        hoje = datetime.today()
        if (int(ano), int(mes)) <= (hoje.year, hoje.month):
            data_base = hoje
    
    data_vencimento = data_base + relativedelta(years=anos, months=meses, days=dias)
    dias_ate_nova = (data_vencimento - datetime.today()).days

    st.markdown(f"📅 **Nova validade (mês/ano):** {data_vencimento.strftime('%m/%Y')}")
    st.markdown(f"⏳ **Dias restantes até o novo vencimento:** {dias_ate_nova} dias")

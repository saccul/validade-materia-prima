
import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="Validade Estendida da Matéria-Prima", layout="centered")
st.title("📦 Calculadora de Validade Estendida")

# 🔸 Lista completa de produtos com validade padrão
produtos = {'100': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'LOURO FOLHAS  6X10G LENA C&E'},
 '101': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'ERVAS FINAS 6X20G LENA C&E'},
 '102': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'SALSA DESIDRATADA 6X20G LENA C&E'},
 '118': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'PIMENTA CALABRESA 6X10G LENA C&E'},
 '12': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'PIMENTA DO REINO EM PÓ 6X20G LENA C&E'},
 '126': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'TEMPERO BAIANO  6X20G LENA C&E'},
 '127': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'AÇAFRÃO 6X20G LENA C&E'},
 '158': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CHA EUCALIPTO LENA C&E 6X10G'},
 '162': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'HORTELA LENA C&E 6X20G'},
 '165': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'MOSTARDA MOIDA 6X20G LENA C&E'},
 '168': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'CANELA CASCA 6 CM PREMIUM 6X20G LENA C&E'},
 '169': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'ALHO GRANULADO 6X20G LENA C&E'},
 '170': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CEBOLA GRANULADA 6X20G LENA C&E'},
 '175': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'ALHO FRITO GRANULADO 6X20G LENA C&E'},
 '177': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CHA CAPIM CIDREIRA LENA C&E 6X10G'},
 '195': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'CONDIMENTO NOZ MOSCADA LENA 6X20G C&E'},
 '196': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CHA HIBISCO FLOR LENA 6X10G'},
 '200': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'PAPRICA DEFUMADA LENA C&E 6X20G'},
 '208': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'TEMPERO COMINHO PÓ 6X20G LENA C&E'},
 '209': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CHIMICHURRI S/ PIMENTA 6X20G LENAC&E'},
 '210': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'BICARBONATO SODIO 6X100G LENA C&E'},
 '216': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CHIMICHURRI  6X20G LENAC&E'},
 '217': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'TEMPERO ANA MARIA  6X20G LENA C&E'},
 '219': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CHIA SEMENTE 6X50G LENA'},
 '250': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'ERVA DOCE 6X20G LENA C&E'},
 '265': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CHA MACELA LENA C&E 6X20G'},
 '269': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'AÇAFRÃO LENA FR 6X60g'},
 '271': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'CANELA EM PÓ LENA FR 6X60G'},
 '272': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'OREGANO LENA FR 6X20G'},
 '273': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'PIMENTA DO REINO MOÍDA LENA FR 6X52G'},
 '277': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'LEMON PEPPER 6X20G LENA C&E'},
 '279': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'MANJERICÃO 6X20G LENA C&E'},
 '303': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'TEMPERO EDU GUEDES 6X20G LENA C&E'},
 '313': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'TOMILHO 6X20G LENA C&E'},
 '315': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'LEMON HERBS LENA 6X20g'},
 '322': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'GUARANÁ EM PÓ 6X50G LENA'},
 '323': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'COMINHO COM PIMENTA  6X20G LENA C&E'},
 '328': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'NOZ MOSCADA GRÃO LENA 6X10G C&E'},
 '334': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'CANELA POTE TRADICIONAL (PURA) 6X30g'},
 '338': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'GENGIBRE COM LIMÃO LENA 6X20G'},
 '339': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'GENGIBRE COM LARANJA LENA 6X20G'},
 '354': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'TEMPERO PEGA MARIDO 6X20G LENA'},
 '355': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CHA VERDE 6X15G LENA'},
 '356': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CHA ERVA CIDREIRA 6X10G LENA'},
 '357': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'LEITE COCO PO LENA 4X250G'},
 '358': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'FARINHA COCO BRANCA LENA 4X250G'},
 '360': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'OREGANO LENA  4X120G'},
 '361': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'AÇAFRÃO 4X250G LENA'},
 '369': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'COCO RALADO LENA 4X250G'},
 '370': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'COCO EM FLOCOS LENA 4X250G'},
 '372': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'FARINHA DE LINHACA DOURADA LENA 4X250G'},
 '373': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'GERGELIM COM CASCA LENA 4X250G'},
 '374': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'GERGELIM BRANCO LENA 4X250G'},
 '396': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'CACAU EM PÓ 100% LENA 4X200G'},
 '410': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'FARINHA DE CHIA LENA 4X200G'},
 '417': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'SEMENTE LINHAÇA DOURADA 4X200G'},
 '418': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'FARINHA DE MACA PERUANA PRETA LENA 4X200G'},
 '419': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'FARINHA DE UVA LENA 4X200G'},
 '420': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'FARINHA DE QUINOA LENA 4X200G'},
 '421': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'FARINHA DE AVEIA INTEGRAL LENA 4X200G'},
 '422': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'FARINHA DE AVEIA SEM GLÚTEN LENA 4X200G'},
 '423': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'FARINHA DE BERIJELA LENA 4X200G'},
 '424': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'FARINHA DE CENOURA LENA 4X200G'},
 '425': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'FARINHA DE LINHACA MARROM LENA 4X200G'},
 '430': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'AVEIA EM FLOCOS S/GLUTEN FINA LENA 4X200G'},
 '431': {'anos': 1, 'dias': 0, 'meses': 0, 'nome': 'AVEIA EM FLOCOS GROSSA LENA  S/GLUTEN 4X200G'},
 '481': {'anos': 1, 'dias': 0, 'meses': 8, 'nome': 'ALHO GRANULADO FRASCO LENA 6X60G'},
 '482': {'anos': 1, 'dias': 0, 'meses': 8, 'nome': 'ALHO FRITO GRANULADO FRASCO LENA 6X60G'},
 '483': {'anos': 1, 'dias': 0, 'meses': 8, 'nome': 'TEMPERO ANA MARIA FRASCO LENA 6X80G'},
 '484': {'anos': 1, 'dias': 0, 'meses': 8, 'nome': 'TEMPERO EDU GUEDES FRASCO LENA 6X80G'},
 '485': {'anos': 1, 'dias': 0, 'meses': 8, 'nome': 'LEMON PEPPER FRASCO LENA 6X80G LENA'},
 '486': {'anos': 1, 'dias': 0, 'meses': 8, 'nome': 'PAPRICA DEFUMADA FRASCO LENA  6X80G'},
 '487': {'anos': 1, 'dias': 0, 'meses': 8, 'nome': 'PAPRICA DOCE FRASCO LENA  6X80G'},
 '488': {'anos': 1, 'dias': 0, 'meses': 8, 'nome': 'PAPRICA PICANTE FRASCO LENA  6X80G'},
 '63': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'PIMENTA DO REINO EM GRÃOS 6X20G LENA C&E'},
 '64': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'OREGANO 6X15G LENA C&E'},
 '83': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'ALECRIM 6X20G LENA C&E'},
 '85': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CHA DE BOLDO 6X10G LENA C&E'},
 '86': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CHA DE CAMOMILA 6X10G LENA C&E'},
 '87': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'CANELA MOIDA 6X20G LENA C&E'},
 '88': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'CHA DE ENDRO SEMENTE  6X20G LENA C&E'},
 '89': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'ERVA DOCE MOIDA 6X20G LENA C&E'},
 '90': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'GENGIBRE PÓ 6X20G LENA C&E'},
 '92': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'CRAVO EM PÓ 6X20G LENA C&E'},
 '93': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'CRAVO EM FLOR 6X20G LENA C&E'},
 '94': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'CURRY 6X20G LENA C&E'},
 '95': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'PAPRICA DOCE 6X20G LENA C&E'},
 '96': {'anos': 1, 'dias': 0, 'meses': 5, 'nome': 'PAPRICA PICANTE 6X20G LENA C&E'},
 '99': {'anos': 2, 'dias': 0, 'meses': 0, 'nome': 'COENTRO SEMENTE 6X20G LENA C&E'}}


# ➕ Adicionar novo item manualmente (sessão atual)
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

# 🔎 Seleção do produto
st.subheader("🧾 Selecione o produto:")
produto = st.selectbox("Produto:", sorted([f'{c} - {produtos[c]['nome']}' for c in produtos]))

# 🔧 Ajuste de validade (opcional)

codigo_selecionado = produto.split(' - ')[0]
validade_padrao = produtos[codigo_selecionado]

anos, meses, dias = validade_padrao["anos"], validade_padrao["meses"], validade_padrao["dias"]

if st.checkbox("Deseja ajustar manualmente a validade deste item?"):
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
st.info("⏳ Validade a ser somada: **" + " e ".join(val_texto) + "**")

# 📅 Data de validade original da matéria-prima

# 📆 Selecione o mês e ano base para o cálculo da validade
st.subheader("📆 Data base considerada para cálculo:")
col1, col2 = st.columns(2)
with col1:
    mes_atual = datetime.today().month
    mes = st.selectbox("Mês", list(range(1, 13)), index=mes_atual - 1,
                       format_func=lambda m: datetime(2000, m, 1).strftime('%B').capitalize())
with col2:
    ano_atual = datetime.today().year
    ano = st.number_input("Ano", value=ano_atual, min_value=2020, max_value=2035, step=1)

# 📆 Cálculo da nova validade estendida com base na data escolhida
if st.button("Calcular nova validade"):
    validade_atual = datetime(ano, mes, 1)
    nova_validade = validade_atual + relativedelta(years=anos, months=meses, days=dias)
    dias_ate_nova = (nova_validade - datetime.today()).days

    st.markdown(f"📅 **Nova data de vencimento:** {nova_validade.strftime('%B de %Y').capitalize()}")
    st.markdown(f"⏳ **Dias restantes até o novo vencimento:** {dias_ate_nova} dias")


import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="Validade de Matéria-Prima", layout="centered")
st.title("📦 Verificador de Validade de Matéria-Prima")

# 🔸 TABELA COM TODOS OS ITENS E SUAS RESPECTIVAS VALIDADES
itens = {
    "AÇAFRÃO 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "ALECRIM 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "ALHO FRITO GRANULADAO 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "ALHO GRANULADAO 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "BICARBONATO SODIO 6X100G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CEBOLA GRANULADA 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CHIMICHURRI  6X20G LENAC&E": {"anos": 2, "meses": 0, "dias": 0},
    "CHIMICHURRI S/ PIMENTA 6X20G LENAC&E": {"anos": 2, "meses": 0, "dias": 0},
    "COENTRO SEMENTE 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CONDIMENTO NOZ MOSCADA LENA 6X20G C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CRAVO EM FLOR 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CRAVO EM PÓ 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CURRY 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "ERVAS FINAS 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "LEMON HERBIS 6X20G LENA C&E": {"anos": 1, "meses": 5, "dias": 0},
    "LEMON PEPPER 6X20G LENA C&E": {"anos": 1, "meses": 5, "dias": 0},
    "LOURO FOLHAS  6X10G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "MANJERICÃO 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "MOSTARDA MOIDA 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "OREGANO 6X15G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "PAPRICA DEFUMADA LENA C&E 6X20G": {"anos": 1, "meses": 5, "dias": 0},
    "PAPRICA DOCE 6X20G LENA C&E": {"anos": 1, "meses": 5, "dias": 0},
    "PAPRICA PICANTE 6X20G LENA C&E": {"anos": 1, "meses": 5, "dias": 0},
    "PIMENTA CALABRESA 6X10G LENA C&E": {"anos": 1, "meses": 5, "dias": 0},
    "PIMENTA DO REIRO EM GRÃOS 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "PIMENTA DO REIRO EM PÓ 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "SALSA DESIDRATADA 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "TEMPERO ANA MARIA  6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "TEMPERO BAIANO  6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "TEMPERO COMINHO PÓ 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "TEMPERO EDU GUEDES 6X20G LENA C&E": {"anos": 1, "meses": 5, "dias": 0},
    "TOMILHO 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "NOZ MOSCADA GRÃO LENA 6X10G C&E": {"anos": 2, "meses": 0, "dias": 0},
    "COMINHO COM PIMENTA  6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "TEMPERO PEGA MARIDO 6X20G LENA": {"anos": 1, "meses": 5, "dias": 0},
    "GUARANA EM PÓ 6X50G LENA": {"anos": 2, "meses": 0, "dias": 0},
    "CANELA CASCA 6 CM PREMIUM 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CANELA MOIDA 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CHA CAPIM CIDREIRA LENA C&E 6X10G": {"anos": 2, "meses": 0, "dias": 0},
    "CHA DE BOLDO 6X10G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CHA DE CAMOMILA 6X10G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CHA DE ENDRO SEMENTE  6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "CHA EUCALIPTO LENA C&E 6X10G": {"anos": 2, "meses": 0, "dias": 0},
    "CHA HIBISCO FLOR LENA 6X10G": {"anos": 2, "meses": 0, "dias": 0},
    "CHA MACELA LENA C&E 6X20G": {"anos": 2, "meses": 0, "dias": 0},
    "CHIA SEMENTE 6X50G LENA": {"anos": 2, "meses": 0, "dias": 0},
    "ERVA DOCE 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "ERVA DOCE MOIDA 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "GENGIBRE PÓ 6X20G LENA C&E": {"anos": 2, "meses": 0, "dias": 0},
    "GEMGIBRE COM LIMÃO LENA 6X20G": {"anos": 2, "meses": 0, "dias": 0},
    "GEMGIBRE COM LARANJA LENA 6X20G": {"anos": 2, "meses": 0, "dias": 0},
    "HORTELA LENA C&E 6X20G": {"anos": 2, "meses": 0, "dias": 0},
    "CHA VERDE 6X15G LENA": {"anos": 2, "meses": 0, "dias": 0},
    "CHA ERVA CIDREIRA 6X10G LENA": {"anos": 2, "meses": 0, "dias": 0},
    "AÇAFRÃO LENA FR 6X60g": {"anos": 2, "meses": 0, "dias": 0},
    "CANELA EM PÓ LENA FR 6X60G": {"anos": 2, "meses": 0, "dias": 0},
    "OREGANO LENA FR 6X20G": {"anos": 2, "meses": 0, "dias": 0},
    "PIMENTA DO REIRO MOÍDA LENA FR 6X52G": {"anos": 2, "meses": 0, "dias": 0},
    "CANELA POTE TRADICIONAL (PURA) 6X30g": {"anos": 2, "meses": 0, "dias": 0},
    "FARINHA DE MACA PERUANA LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "FARINHA DE LINHACA DOURADA LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "OREGANO LENA  4X120G": {"anos": 2, "meses": 0, "dias": 0},
    "AÇAFRÃO 4X250G LENA": {"anos": 2, "meses": 0, "dias": 0},
    "GERGELIM BRANCO LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "GERGELIM COM CASCA LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "COCO EM FLOCOS LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "COCO RALADO LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "FARINHA COCO BRANCA LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "LEITE COCO PO LENA 4X250G": {"anos": 1, "meses": 0, "dias": 0},
    "CACAU EM PÓ 100% LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "FARINHA DE AVEIA INTEGRAL LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "FARINHA DE AVEIA SEM GLÚTEN LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "FARINHA DE BERIJELA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "FARINHA DE CENOURA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "FARINHA DE CHIA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "FARINHA DE MACA PERUANA PRETA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "FARINHA DE UVA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "SEMENTE LINHAÇA DOURADA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "FARINHA DE QUINOA LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
    "FARINHA DE LINHACA MARROM LENA 4X200G": {"anos": 1, "meses": 0, "dias": 0},
}


# 🔸 ESCOLHA DO PRODUTO
st.subheader("🧾 Selecione o item da matéria-prima:")
produto = st.selectbox("Produto:", sorted(itens.keys()))

# 🔸 EXIBE VALIDADE PADRÃO
validade = itens[produto]
anos, meses, dias = validade["anos"], validade["meses"], validade["dias"]

val_texto = []
if anos: val_texto.append(f"{anos} ano{'s' if anos > 1 else ''}")
if meses: val_texto.append(f"{meses} mês{'es' if meses > 1 else ''}")
if dias: val_texto.append(f"{dias} dia{'s' if dias > 1 else ''}")
st.info(f"⏳ Validade padrão: **{' e '.join(val_texto)}**")

# 🔸 DATA DE FABRICAÇÃO (MÊS E ANO)
st.subheader("📅 Informe o mês e ano de fabricação:")
col1, col2 = st.columns(2)
with col1:
    mes = st.selectbox("Mês", list(range(1, 13)), format_func=lambda m: datetime(2000, m, 1).strftime('%B').capitalize())
with col2:
    ano = st.number_input("Ano", min_value=2020, max_value=2035, step=1)

# 🔸 CÁLCULO
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

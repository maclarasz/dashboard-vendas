import streamlit as st
import pandas as pd
import plotly.express as px

# ── Configuração da página ──────────────────────────────
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

# ── Dados fictícios ─────────────────────────────────────
dados = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
             "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
    "Vendas": [12000, 15000, 13500, 17000, 19500, 22000,
               20000, 23000, 21000, 25000, 27000, 30000],
    "Meta":   [14000, 14000, 15000, 15000, 18000, 18000,
               20000, 20000, 22000, 22000, 25000, 25000],
    "Categoria": ["Eletrônicos", "Roupas", "Eletrônicos", "Alimentos",
                  "Roupas", "Eletrônicos", "Alimentos", "Roupas",
                  "Eletrônicos", "Alimentos", "Roupas", "Eletrônicos"]
}

df = pd.DataFrame(dados)

# ── Cabeçalho ───────────────────────────────────────────
st.title("📊 Dashboard de Vendas 2024")
st.markdown("Acompanhamento mensal de vendas e metas")

# ── Métricas no topo ────────────────────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("Total de Vendas", f"R$ {df['Vendas'].sum():,.0f}")
col2.metric("Melhor Mês", f"R$ {df['Vendas'].max():,.0f}")
col3.metric("Meta Anual", f"R$ {df['Meta'].sum():,.0f}")

st.divider()

# ── Gráfico de linha: Vendas x Meta ─────────────────────
st.subheader("Vendas vs Meta por Mês")
fig1 = px.line(df, x="Mês", y=["Vendas", "Meta"],
               markers=True,
               labels={"value": "R$", "variable": "Legenda"})
st.plotly_chart(fig1, use_container_width=True)

# ── Gráfico de barras: Vendas por Categoria ─────────────
st.subheader("Vendas por Categoria")
df_cat = df.groupby("Categoria")["Vendas"].sum().reset_index()
fig2 = px.bar(df_cat, x="Categoria", y="Vendas",
              color="Categoria",
              labels={"Vendas": "R$"})
st.plotly_chart(fig2, use_container_width=True)

# ── Tabela de dados ─────────────────────────────────────
st.subheader("Dados completos")
st.dataframe(df, use_container_width=True)


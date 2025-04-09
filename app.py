
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

# Configuración de la página con tema claro forzado
st.set_page_config(
    page_title="Calculadora de Intereses",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="auto"
)

# Cargar logo
logo = Image.open("logo.png")

# Mostrar el logo centrado
st.image(logo, width=150)

# Título y frase inspiradora
st.markdown(
    "<h1 style='text-align: center; color: #000000; font-family: Kompot Sans, Myriad, sans-serif;'>Calculadora de Intereses</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align: center; color: #000000; font-weight: normal; font-family: Kompot Sans, Myriad, sans-serif;'>Tus sueños tienen un plan: empieza hoy.</h4>",
    unsafe_allow_html=True
)

st.markdown("---")

# Entradas de usuario
col1, col2 = st.columns(2)
with col1:
    monto = st.number_input("💵 Monto del préstamo", min_value=0.0, step=100.0)
with col2:
    tasa_anual = st.number_input("📈 Tasa de interés anual (%)", min_value=0.0, step=0.1)

plazo = st.slider("⏳ Plazo del préstamo (en meses)", min_value=1, max_value=60, step=1, value=12)

# Cálculo del interés compuesto mensual
if st.button("Calcular", use_container_width=True) and monto > 0 and tasa_anual > 0:
    tasa_mensual = tasa_anual / 12 / 100
    pago_mensual = monto * (tasa_mensual * (1 + tasa_mensual)**plazo) / ((1 + tasa_mensual)**plazo - 1)
    
    saldo = monto
    tabla = []
    for mes in range(1, plazo + 1):
        interes = saldo * tasa_mensual
        capital = pago_mensual - interes
        saldo -= capital
        tabla.append([mes, round(pago_mensual, 2), round(interes, 2), round(capital, 2), round(max(saldo, 0), 2)])
    
    df = pd.DataFrame(tabla, columns=["Mes", "Pago mensual", "Interés", "Capital", "Saldo restante"])
    
    st.markdown("### Detalle de pagos mensuales:")
    st.dataframe(df, use_container_width=True)

    st.markdown("---")
    st.markdown(
        f"<div style='background-color:#ffe67a; padding:20px; border-radius:10px;'>"
        f"<h3 style='color:#000000; font-family: Kompot Sans, Myriad;'>💰 Total a pagar: <strong>${round(pago_mensual * plazo, 2):,.2f}</strong></h3>"
        f"<h3 style='color:#000000; font-family: Kompot Sans, Myriad;'>📈 Interés total generado: <strong>${round(pago_mensual * plazo - monto, 2):,.2f}</strong></h3>"
        f"</div>", unsafe_allow_html=True
    )

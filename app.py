
import streamlit as st
from PIL import Image

# Cargar logo
logo = Image.open("logo.png")

# Configuración de la página
st.set_page_config(
    page_title="Calculadora de Intereses",
    page_icon="💸",
    layout="centered"
)

# Colores personalizados
COLOR_PRIMARIO = "#f7b731"
COLOR_SECUNDARIO = "#ffe67a"
COLOR_TEXTO = "#000000"
FONDO = "#ffffff"

# Mostrar el logo centrado
st.image(logo, width=150)

# Título personalizado
st.markdown(
    f"<h1 style='text-align: center; color: {COLOR_TEXTO}; font-family: Kompot Sans, Myriad, sans-serif;'>Calculadora de Intereses</h1>",
    unsafe_allow_html=True
)

# Subtítulo o frase
st.markdown(
    f"<h4 style='text-align: center; color: {COLOR_TEXTO}; font-weight: normal; font-family: Kompot Sans, Myriad, sans-serif;'>Lo que se puede medir, se puede gestionar ✨</h4>",
    unsafe_allow_html=True
)

st.markdown("---")

# Entradas en columnas
col1, col2 = st.columns(2)
with col1:
    monto = st.number_input("💵 Monto del préstamo", min_value=0.0, step=100.0)
with col2:
    tasa = st.number_input("📈 Tasa de interés anual (%)", min_value=0.0, step=0.1)

plazo = st.slider("⏳ Plazo del préstamo (en meses)", min_value=1, max_value=60, step=1, value=12)

# Botón para calcular
if st.button("Calcular", use_container_width=True):
    interes_anual = (monto * tasa) / 100
    interes_mensual = interes_anual / 12
    total_interes = interes_mensual * plazo
    total_a_pagar = monto + total_interes

    st.markdown("---")
    st.markdown(
        f"<div style='background-color:{COLOR_SECUNDARIO}; padding:20px; border-radius:10px;'>"
        f"<h3 style='color:{COLOR_TEXTO}; font-family: Kompot Sans, Myriad;'>💰 Interés total generado: <strong>${total_interes:,.2f}</strong></h3>"
        f"<h3 style='color:{COLOR_TEXTO}; font-family: Kompot Sans, Myriad;'>💵 Total a pagar: <strong>${total_a_pagar:,.2f}</strong></h3>"
        f"</div>", unsafe_allow_html=True
    )

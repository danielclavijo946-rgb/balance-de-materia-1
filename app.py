import streamlit as st

# Título de la aplicación
st.title('🍎 Calculadora de Balance de Masa')
st.markdown('---')

# Introducción y descripción del problema
st.header('Descripción del problema')
st.write(
    'Luego de procesar una fruta para obtener pulpa, se necesita ajustar los grados °Brix '
    'para cumplir con los estándares de calidad. Este aplicativo te ayudará a calcular la '
    'cantidad de azúcar necesaria para alcanzar el °Brix deseado.'
)

# Sección de entrada de datos
st.markdown('---')
st.header('Entrada de datos')

# Campos para que el usuario ingrese los valores
pulpa_inicial = st.number_input('Peso inicial de la pulpa (kg)', min_value=0.0, value=50.0, format="%.2f")
brix_inicial = st.number_input('°Brix inicial de la pulpa (%)', min_value=0.0, max_value=100.0, value=7.0, format="%.2f")
brix_final = st.number_input('°Brix deseado final (%)', min_value=0.0, max_value=100.0, value=10.0, format="%.2f")

# Botón para calcular
if st.button('Calcular cantidad de azúcar'):
    # Validación de los datos
    if brix_inicial >= brix_final:
        st.error('El °Brix inicial debe ser menor que el °Brix final deseado.')
    else:
        # Lógica para el balance de masa
        azucar_a_agregar = (pulpa_inicial * (brix_final - brix_inicial)) / (100 - brix_final)
        pulpa_final = pulpa_inicial + azucar_a_agregar

        # Mostrar el resultado
        st.markdown('---')
        st.header('Resultados')
        st.success(f'**Cantidad de azúcar a agregar:** {azucar_a_agregar:.2f} kg')
        st.info(f'Peso final de la pulpa: {pulpa_final:.2f} kg')

        # Explicación del cálculo
        st.markdown('---')
        st.header('Explicación del cálculo')
        st.write('Se utiliza la fórmula de balance de masa para sólidos (azúcares):')
        
        # Fórmula mejorada con LaTeX y variables
        st.latex(f'M_1 \cdot C_1 + M_{{azucar}} \cdot C_{{azucar}} = (M_1 + M_{{azucar}}) \cdot C_2')

        st.write('Donde:')
        st.write(f'- $M_1$: Masa inicial de la pulpa = **{pulpa_inicial} kg**')
        st.write(f'- $C_1$: Concentración inicial (°Brix) = **{brix_inicial}%**')
        st.write(f'- $M_{{azucar}}$: Masa de azúcar a agregar = **{azucar_a_agregar:.2f} kg**')
        st.write(f'- $C_{{azucar}}$: Concentración del azúcar = **100%**')
        st.write(f'- $C_2$: Concentración final deseada (°Brix) = **{brix_final}%**')
        st.write('Al despejar $M_{{azucar}}$ de la ecuación, se obtiene el resultado.')

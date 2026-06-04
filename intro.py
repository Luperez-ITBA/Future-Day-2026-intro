import streamlit as st
import base64
import os

# Configuración de la página
st.set_page_config(page_title="ITBA - Introducción Teórica", layout="wide", initial_sidebar_state="collapsed")

# Función para cargar imágenes locales en el HTML (Base64)
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
    return "https://via.placeholder.com/180x240?text=Imagen+Local"

# Estilos CSS unificados con el Hub
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    
    /* El recuadro azul/gris estructurado */
    .intro-box {
        background-color: #e2e8f0;
        border-radius: 15px;
        border-left: 10px solid #0074D9;
        padding: 35px;
        display: flex;
        align-items: center;
        gap: 40px;
        margin-bottom: 35px;
    }

    /* Contenedor de la imagen izquierda */
    .image-side {
        min-width: 180px;
        max-width: 180px;
        text-align: center;
    }
    
    .image-side img {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    /* Lado del texto */
    .text-side {
        flex-grow: 1;
        font-size: 18px;
        line-height: 1.6;
        color: #1e293b;
    }

    .text-side h2 {
        color: #0074D9;
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 28px;
    }
    
    .text-side ul {
        margin-top: 10px;
        margin-bottom: 15px;
        padding-left: 20px;
    }
    
    .text-side li {
        margin-bottom: 8px;
    }

    .math-container {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #cbd5e1;
        display: inline-block;
        margin: 10px 0;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
    }
    
    @media (max-width: 768px) {
        .intro-box {
            flex-direction: column;
            gap: 20px;
            padding: 20px;
        }
        .image-side {
            min-width: 140px;
            max-width: 140px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Cuerpo principal
st.title("🎲 Introducción a las Probabilidades")
st.write("---")

# --- RECUADRO 1: MODIFICADO A PEDIDO DEL JEFE ---
st.markdown(f"""
    <div class="intro-box">
        <div class="image-side">
            <img src="{get_base64_image('image_31ad20.png')}" width="180" alt="Dados Romanos">
        </div>
        <div class="text-side">
            <h2>Fenómenos Aleatorios y Regularidades</h2>
            <p>
                Los romanos fueron pioneros en los juegos de azar, tanto es así que su juego de dados <i>aleae</i> ha resultado un modelo para pensar en probabilidades hasta la actualidad.
            </p>
            <p>
                Al jugar repetidamente fueron notando que, si bien el resultado de un tiro era totalmente impredecible (¡aleatorio!), existían ciertas <b><i>regularidades</i></b>, ya que algunos resultados aparecían regularmente con ciertas <b>frecuencias fijas</b>. Por ejemplo: 
            </p>
            <ul>
                <li>Cada número ocurría, en promedio 1/6 de las veces.</li>
                <li>Los números pares (2,4,6) aparecían en promedio la mitad de las veces, lo mismo que los impares (1,3,5).</li>
                <li>Ciertas combinaciones, por ejemplo <i>obtener 3 dos veces seguidas</i> salían 1 de cada 36 veces.</li>
            </ul>
            <p>
                <b>¿Pueden intuir por qué?</b> Hint: ¡pensar en una rifa!  
            </p>
            <p>
                Esas frecuencias <i>estables</i> son lo que hoy día conocemos como <b><i>probabilidades</i></b>.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- RECUADRO 2: INTACTO ---
st.markdown(f"""
    <div class="intro-box">
        <div class="image-side">
            <img src="{get_base64_image('image_313bc8.png')}" width="180" alt="Paradoja del Cumpleaños">
        </div>
        <div class="text-side">
            <h2>La Paradoja del Cumpleaños</h2>
            <p>
                ¿Sabías que en un grupo de solo 23 personas, la probabilidad de que dos cumplan años el mismo día es mayor al 50%? 
                Aislados, estos eventos parecen raros, pero al considerar todas las combinaciones posibles de pares, 
                la probabilidad crece de forma sorprendente. Esto desafía nuestra intuición lineal del azar.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- RECUADRO 3: INTACTO ---
st.markdown(f"""
    <div class="intro-box">
        <div class="image-side">
            <img src="{get_base64_image('image_8f4464.png')}" width="180" alt="Fenómenos Aleatorios">
        </div>
        <div class="text-side">
            <h2>Fenómenos Aleatorios</h2>
            <p>
                Por supuesto, la vida diaria nos bombardea con <b>probabilidades</b> de eventos cotidianos. 
                El celular nos dice <i>50% de probabilidades de lluvia para esta tarde</i>, un periodista nos dice que 
                la probabilidad de que gane nuestro equipo es muy alta, etc.
            </p>
            <p>
                En estos casos la idea intuitiva detrás de estos razonamientos es:
            </p>
            <div style="text-align: center;">
                <div class="math-container" style="font-size: 21px;">
                    <i>P(Evento)</i> = Proporción de veces que el evento ocurrió en el pasado bajo estas condiciones
                </div>
            </div>
            <p>
                Esta es la base del enfoque probabilístico de los <b><i>modelos predictivos</i></b> y su <b><i>entrenamiento estadístico.</i></b>.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- BOTÓN DE RETORNO AL HUB ---
st.write("---")
col_vacia1, col_boton_regreso, col_vacia2 = st.columns([1, 1, 1])
with col_boton_regreso:
    st.link_button("🔙 Volver al Hub Principal", "https://future-day-2026-app-bbynemlxetszzudwtcup4u.streamlit.app/")

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
        width: 100%;
        height: auto;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }

    /* Texto e información de la derecha */
    .text-side {
        flex: 1;
    }
    .text-side h2 {
        color: #001f3f;
        margin-top: 0;
        margin-bottom: 15px;
        font-size: 30px !important;
    }
    .text-side p {
        font-size: 20px !important;
        line-height: 1.6;
        color: #1e293b;
        margin-bottom: 15px;
    }
    .text-side ul {
        margin-top: 10px;
        margin-bottom: 15px;
        padding-left: 20px;
    }
    .text-side li {
        font-size: 20px !important;
        line-height: 1.6;
        color: #1e293b;
        margin-bottom: 8px;
    }

    /* Formateo de Fracciones Matemáticas en un recuadro blanco redondeado para resaltar */
    .math-container {
        text-align: center; 
        font-size: 24px; 
        margin: 15px auto; 
        color: #001f3f;
        font-family: 'Times New Roman', Times, serif;
        background-color: white;
        padding: 15px 30px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.06);
        display: inline-block;
    }
    .fraction {
        display: inline-block; 
        vertical-align: middle; 
        text-align: center; 
        font-size: 21px;
        margin-left: 5px;
        margin-right: 5px;
    }
    .numerator {
        display: block; 
        border-bottom: 2px solid #001f3f; 
        padding: 0 10px;
    }
    .denominator {
        display: block; 
        padding: 5px 10px 0 10px;
    }
            
    .numerator {
        display: block; 
        border-bottom: 2px solid #001f3f; 
        padding: 0 10px;
    }
    .denominator {
        display: block; 
        padding: 5px 10px 0 10px;
    }

    /* --- PARCHE RESPONSIVO PARA CELULARES --- */
    @media (max-width: 768px) {
        h1 { font-size: 26px !important; }
        h3 { font-size: 16px !important; }
        .intro-box {
            flex-direction: column !important;
            padding: 20px !important;
            gap: 20px !important;
            text-align: center !important;
        }
        .image-side {
            margin: 0 auto !important;
        }
        .text-side h2 { font-size: 22px !important; }
        .text-side p { font-size: 16px !important; }
        .text-side li { font-size: 16px !important; }
        .math-container {
            font-size: 15px !important;
            padding: 10px 15px !important;
            display: block !important;
            width: 100% !important;
            box-sizing: border-box !important;
            word-wrap: break-word !important;
        }
        .fraction { font-size: 14px !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    if os.path.exists('logo_itba.png'):
        st.image('logo_itba.png', width=150)
    else:
        st.write("### ITBA")
with col_titulo:
    st.markdown("<h1 style='font-size: 46px; margin-bottom: 0;'><span style='color: #000000;'>Las Probabilidades:</span> <span style='color: #0074D9;'>su Significado y su Cálculo</span></h1>", unsafe_allow_html=True)
    st.write("Future Day 2026 - Fundamentos del análisis aleatorio")

st.write("---")

# Carga de imágenes locales
img_roman = get_base64_image('roman-aleae.png')
img_laplace = get_base64_image('laplace-bernoulli.png')
img_dibu = get_base64_image('dibu-rain.png')


# --- RECUADRO 1: MODIFICADO CON EL TEXTO NUEVO ---
st.markdown(f"""
    <div class="intro-box">
        <div class="image-side">
            <img src="{img_roman}" alt="Roman Aleae">
        </div>
        <div class="text-side">
            <h2>Significado de las Probabilidades</h2>
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


# --- RECUADRO 2: ENFOQUE FRECUENCIAL (INTACTO) ---
st.markdown(f"""
    <div class="intro-box">
        <div class="image-side">
            <img src="{img_laplace}" alt="Pierre-Simon Laplace">
        </div>
        <div class="text-side">
            <h2>Probabilidades Frecuenciales</h2>
            <p>
                Usando esa idea muchos años más tarde, los matemáticos Jacob <b>Bernoulli</b> y Pierre-Simon <b>Laplace</b>, establecieron la famosa <b><i>Ley de los Grandes Números</i></b> 
                : <b>repitiendo </b> un experimento aleatorio una buena cantidad de veces, la <b>frecuencia de ocurrencia</b> de los eventos se acercará a su 
                probabilidad. 
            </p>
            <div style="text-align: center;">
                <div class="math-container">
                    <i>P(Evento)</i> &approx; 
                    <div class="fraction">
                        <span class="numerator"># Ocurrencias</span>
                        <span class="denominator"># Repeticiones</span>
                    </div>
                </div>
            </div>
            <p>
                Sabíamos ya que si tiramos un dado muchas, muchas veces, tendremos números pares, en promedio, la mitad de las veces. Bernoulli y Laplace llevaron esto al extremo, usando el método para calcular la probabilidad de cualquier >b>evento</b>. Estas ideas, tan sencillas como potentes, las seguimos usando hasta la actualidad, cuando con 
                herramientas computacionales modernas realizamos <b><i>simulaciones</i></b> y <b><i>remuestreos</i></b> en 
                probabilidades y estadística.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)


# --- RECUADRO 3: ENFOQUE PREDICTIVO / VIDA COTIDIANA (INTACTO) ---
st.markdown(f"""
    <div class="intro-box">
        <div class="image-side">
            <img src="{img_dibu}" alt="Fenómenos Aleatorios en la vida diaria">
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
    st.link_button("🔙 Volver al Hub Principal", "https://future-day-2026-app-bbynemlxetszzudwtcup4u.streamlit.app/", use_container_width=True)

# --- PIE DE PÁGINA ---
st.write("---")
st.caption("ITBA Future Day 2026 - Departamento de Ciencias Exactas y Naturales")

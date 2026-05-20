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
    # Título modificado con colores específicos según lo solicitado
    st.markdown("<h1 style='font-size: 46px; margin-bottom: 0;'><span style='color: #000000;'>Las Probabilidades:</span> <span style='color: #0074D9;'>su Significado y su Cálculo</span></h1>", unsafe_allow_html=True)
    st.write("Future Day 2026 - Fundamentos del análisis aleatorio")

st.write("---")

# Carga de imágenes locales
img_roman = get_base64_image('roman-aleae.png')
img_laplace = get_base64_image('laplace-bernoulli.png')
img_dibu = get_base64_image('dibu-rain.png')


# --- RECUADRO 1: SIGNIFICADO CLÁSICO ---
st.markdown(f"""
    <div class="intro-box">
        <div class="image-side">
            <img src="{img_roman}" alt="Roman Aleae">
        </div>
        <div class="text-side">
            <h2>Significado de las Probabilidades</h2>
            <p>
                Los romanos fueron pioneros en los juegos de azar, tanto es así que su juego de dados <b><i>aleae</i></b> 
                ha resultado un modelo para pensar en <b>probabilidades</b> hasta la actualidad.
            </p>
            <p>
                Así, sabemos que la <b><i>probabilidad</i></b> de obtener el número 3 al arrojar un dado al azar es de 1/6, 
                y que la probabilidad de obtener un número par es 1/2. En ambos casos estamos pensando intuitivamente en la <b>fórmula</b>:
            </p>
            <div style="text-align: center;">
                <div class="math-container">
                    <i>P(Evento)</i> = 
                    <div class="fraction">
                        <span class="numerator"># Casos Favorables</span>
                        <span class="denominator"># Casos Posibles</span>
                    </div>
                </div>
            </div>
            <p>
                Con esa idea, resulta también intuitivo que las <i>probabilidades de eventos independientes se multiplican</i>. 
                Por ejemplo si arrojo dos veces el dado, la probabilidad de obtener 5 dos veces seguidas es:
            </p>
            <div style="text-align: center;">
                <div class="math-container">
                    <div class="fraction">
                        <span class="numerator">1</span>
                        <span class="denominator">6</span>
                    </div>
                    &middot;
                    <div class="fraction">
                        <span class="numerator">1</span>
                        <span class="denominator">6</span>
                    </div>
                    =
                    <div class="fraction">
                        <span class="numerator">1</span>
                        <span class="denominator">36</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


# --- RECUADRO 2: ENFOQUE FRECUENCIAL ---
st.markdown(f"""
    <div class="intro-box">
        <div class="image-side">
            <img src="{img_laplace}" alt="Pierre-Simon Laplace">
        </div>
        <div class="text-side">
            <h2>Probabilidades Frecuenciales</h2>
            <p>
                Usando una idea de Jacob <b>Bernoulli</b> y Pierre-Simon <b>Laplace</b>, la famosa <b><i>Ley de los Grandes Números</i></b> 
                podemos computar probabilidades sin necesidad de contar casos, simplemente <b>repetimos</b> el experimento 
                aleatorio una buena cantidad de veces y la <b>frecuencia de ocurrencia</b> de los eventos se acercará a su 
                probabilidad. Por ejemplo, si tiramos un dado muchas, muchas veces, tendremos números pares, en promedio, 
                la mitad de las veces.
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
                Estas ideas, tan sencillas como potentes, las seguimos usando hasta la actualidad, cuando con 
                herramientas computacionales modernas realizamos <b><i>simulaciones</i></b> y <b><i>remuestreos</i></b> en 
                probabilidades y estadística.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)


# --- RECUADRO 3: ENFOQUE PREDICTIVO / VIDA COTIDIANA ---
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
                Esta es la base del enfoque probabilístico de los <b><i>modelos predictivos</i></b>.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)


# --- BOTÓN DE RETORNO AL HUB ---
st.write("---")
col_vacia1, col_boton_regreso, col_vacia2 = st.columns([1, 1, 1])
with col_boton_regreso:
    st.link_button("🔙 Volver al Hub Principal", "https://share.streamlit.io/...", use_container_width=True)

# --- PIE DE PÁGINA ---
st.write("---")
st.caption("ITBA Future Day 2026 - Departamento de Ciencias Exactas y Naturales")
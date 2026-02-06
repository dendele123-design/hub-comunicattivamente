import streamlit as st

# =================================================================
# 1. CONFIGURAZIONE E DESIGN
# =================================================================
st.set_page_config(page_title="comunicAttivamente Hub", page_icon="🛡️", layout="centered")

ROSSO_BRAND = "#DC0612"

st.markdown(f"""
    <style>
    /* ANTI DARK-MODE */
    .stApp {{ background-color: #ffffff !important; }}
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label {{
        color: #1a1a1a !important;
    }}

    /* HEADER HUB */
    .hub-header {{
        text-align: center;
        padding: 30px;
        border-bottom: 3px solid {ROSSO_BRAND};
        margin-bottom: 30px;
    }}
    .super-text {{ color: {ROSSO_BRAND} !important; font-weight: 900; }}

    /* CARD APP */
    .app-card {{
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        border-left: 8px solid #1a1a1a;
        margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }}
    .app-title {{ font-size: 20px; font-weight: bold; color: #1a1a1a; margin-bottom: 5px; }}
    .app-desc {{ font-size: 14px; color: #555; margin-bottom: 15px; line-height: 1.4; }}

    /* AREA EBOOK EVIDENZIATA */
    .ebook-section {{
        background-color: #1a1a1a;
        color: #ffffff !important;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-top: 40px;
        border: 2px solid {ROSSO_BRAND};
    }}
    .ebook-section h2, .ebook-section p {{ color: #ffffff !important; }}

    /* BOTTONI */
    .stLinkButton>a {{
        width: 100% !important;
        background-color: {ROSSO_BRAND} !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        height: 3em !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-decoration: none !important;
    }}
    
    header {{visibility: hidden !important;}}
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. INTESTAZIONE
# =================================================================
st.markdown(f"""
    <div class="hub-header">
        <h1>comunicattivamente | <span class="super-text">SuPeR</span></h1>
        <p>Benvenuto nella tua Centrale di Comando per l'Efficienza Aziendale</p>
    </div>
""", unsafe_allow_html=True)

# =================================================================
# 3. ELENCO DELLE APP (MODIFICABILE)
# =================================================================
# VUOI AGGIUNGERE UN'APP? 
# Copia da { a }, e incollalo subito sotto l'ultimo. 
# Ricordati di mettere la virgola tra uno e l'altro!

lista_app = [
    {
        "titolo": "📊 Test ANSIA S.P.A.",
        "descrizione": "Il test diagnostico completo in 20 punti per individuare i virus che bloccano la tua azienda.",
        "url": "https://ansia-spa.streamlit.app" # <--- METTI IL LINK REALE QUI
    },
    {
        "titolo": "🛠️ Toolkit dell'Efficienza",
        "descrizione": "Strumenti operativi: Timer dello spreco, Calcolatore di libertà e Tassa sulle notifiche.",
        "url": "https://toolkit-efficienza.streamlit.app" # <--- METTI IL LINK REALE QUI
    },
    {
        "titolo": "🏢 SuPeR - HORECA Manager",
        "descrizione": "Gestione professionale per la ristorazione: Registro HACCP Cloud e Chiusura Cassa Digitale.",
        "url": "https://super-horeca.streamlit.app" # <--- METTI IL LINK REALE QUI
    },
    {
        "titolo": "🍷 Wine Selector 2.0",
        "descrizione": "Il Sommelier Digitale e la Carta Vini interattiva per un'esperienza cliente di lusso.",
        "url": "https://wine-selector.streamlit.app" # <--- METTI IL LINK REALE QUI
    }
]

# Ciclo che crea i tasti automaticamente
for app in lista_app:
    st.markdown(f"""
        <div class="app-card">
            <div class="app-title">{app['titolo']}</div>
            <div class="app-desc">{app['descrizione']}</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("APRI WEB APP 🚀", app['url'])
    st.write("")

# =================================================================
# 4. AREA EBOOK EVIDENZIATA
# =================================================================
st.markdown(f"""
    <div class="ebook-section">
        <h2 style="margin-top:0;">📘 RISORSA GRATUITA</h2>
        <p>Scarica l'Ebook <b>"ANSIA S.P.A."</b> e scopri come smettere di correre sulla ruota del criceto.</p>
        <a href="https://www.comunicattivamente.it/ebook-ansia-spa" target="_blank" 
           style="background-color:{ROSSO_BRAND}; color:white; padding:12px 25px; border-radius:50px; text-decoration:none; font-weight:bold; display:inline-block; margin-top:10px;">
           SCARICA L'EBOOK ORA
        </a>
    </div>
""", unsafe_allow_html=True)

# =================================================================
# 5. CONTATTI E FOOTER
# =================================================================
st.write("")
st.write("---")
st.markdown(f"""
    <div style="text-align: center; padding: 20px;">
        <p style="font-weight:bold;">Daniele Salvatori | comunicAttivamente</p>
        📞 <a href="tel:+393929334563" style="color:{ROSSO_BRAND}; text-decoration:none; font-weight:bold;">+39 392 933 4563</a><br>
        🌐 <a href="https://www.superstart.it" target="_blank" style="color:{ROSSO_BRAND}; text-decoration:none; font-weight:bold;">Visita SuPeR (superstart.it)</a>
    </div>
""", unsafe_allow_html=True)

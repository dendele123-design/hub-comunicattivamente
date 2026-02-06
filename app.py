import streamlit as st

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (comunicAttivamente & SuPeR)
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
        padding: 20px;
        border-bottom: 2px solid #eee;
        margin-bottom: 30px;
    }}
    .super-text {{ color: {ROSSO_BRAND} !important; font-weight: 900; }}

    /* CARD APP CON STRISCIA ROSSA */
    .app-card {{
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        border-left: 10px solid {ROSSO_BRAND} !important; /* STRISCIA ROSSA AZIENDALE */
        margin-bottom: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }}
    .app-title {{ font-size: 22px; font-weight: bold; color: #1a1a1a; margin-bottom: 5px; }}
    .app-desc {{ font-size: 15px; color: #555; line-height: 1.4; }}

    /* BOTTONI ROSSI DESATURATI */
    .stLinkButton>a {{
        width: 200px !important;
        background-color: {ROSSO_BRAND} !important;
        opacity: 0.9; /* Scarica un po' il rosso per renderlo elegante */
        color: white !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        height: 3em !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-decoration: none !important;
        margin-bottom: 30px;
        transition: 0.3s;
    }}
    .stLinkButton>a:hover {{ opacity: 1; transform: scale(1.02); }}

    /* AREA EBOOK EVIDENZIATA */
    .ebook-section {{
        background-color: #1a1a1a;
        color: #ffffff !important;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin: 40px 0;
        border: 2px solid {ROSSO_BRAND};
    }}
    .ebook-section h2, .ebook-section p {{ color: #ffffff !important; }}

    /* FOOTER STILE RICHIESTO */
    .footer-container {{
        text-align: center;
        padding: 30px;
        background-color: #f1f1f1;
        border-radius: 20px;
        margin-top: 50px;
    }}
    .footer-container a {{ color: {ROSSO_BRAND} !important; text-decoration: none; font-weight: bold; }}
    .wa-button {{
        background-color: #25D366;
        color: white !important;
        padding: 12px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 15px;
        font-size: 16px;
        box-shadow: 0 4px 10px rgba(37, 211, 102, 0.3);
    }}
    
    header {{visibility: hidden !important;}}
    </style>
    """, unsafe_allow_html=True)

# =================================================================
# 2. INTESTAZIONE
# =================================================================
st.markdown(f"""
    <div class="hub-header">
        <h1 style="font-size: 28px;">comunicattivamente | <span class="super-text">SuPeR</span></h1>
        <p style="font-weight: bold; color: #666;">Esorcismo del Caos Aziendale</p>
    </div>
""", unsafe_allow_html=True)

# =================================================================
# 3. ELENCO DELLE APP (MODIFICABILE)
# =================================================================
# Qui puoi aggiungere o togliere app come preferisci
apps = [
    {
        "titolo": "📊 Test Diagnostico ANSIA S.P.A.",
        "descrizione": "Scopri se sei un Titolare Criceto con il test completo in 20 punti.",
        "url": "https://ansia-spa-test.streamlit.app" # <--- METTI I TUOI LINK REALI
    },
    {
        "titolo": "🚑 Pronto Soccorso Aziendale",
        "descrizione": "Calcola il tuo Profit Leak: quanto ti costano riunioni e notifiche ogni anno.",
        "url": "https://pronto-soccorso.streamlit.app"
    },
    {
        "titolo": "🏢 SuPeR - HORECA Edition",
        "descrizione": "Gestione operativa per ristorazione: Chiusura Cassa e Registro HACCP digitale.",
        "url": "https://super-horeca.streamlit.app"
    },
    {
        "titolo": "🍷 Wine Selector 2.0",
        "descrizione": "Sommelier Digitale e Carta Vini interattiva per un servizio al tavolo di lusso.",
        "url": "https://wine-selector.streamlit.app"
    }
]

for app in apps:
    st.markdown(f"""
        <div class="app-card">
            <div class="app-title">{app['titolo']}</div>
            <div class="app-desc">{app['descrizione']}</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("APRI WEB APP 🚀", app['url'])

# =================================================================
# 4. AREA EBOOK EVIDENZIATA
# =================================================================
st.markdown(f"""
    <div class="ebook-section">
        <h2 style="margin-top:0;">📘 RISORSA GRATUITA</h2>
        <p>Scarica l'Ebook <b>"ANSIA S.P.A."</b> e impara a riprenderti il tuo tempo.</p>
        <a href="https://www.comunicattivamente.it/ebook-ansia-spa" target="_blank" 
           style="background-color:{ROSSO_BRAND}; color:white; padding:12px 25px; border-radius:50px; text-decoration:none; font-weight:bold; display:inline-block; margin-top:10px;">
           SCARICA L'EBOOK ORA
        </a>
    </div>
""", unsafe_allow_html=True)

# =================================================================
# 5. FOOTER (LAYOT RICHIESTO)
# =================================================================
st.markdown(f"""
    <div class="footer-container">
        <p style="font-size: 18px; font-weight: bold; margin-bottom: 5px;">
            Daniele Salvatori | <a href="https://www.comunicattivamente.it" target="_blank">comunicAttivamente</a>
        </p>
        <p style="margin-bottom: 20px; font-weight: bold; color: #555;">Esorcismo del Caos Aziendale</p>
        
        <p style="margin-bottom: 5px;">
            📧 <a href="mailto:daniele@comunicattivamente.it">daniele@comunicattivamente.it</a>
        </p>
        <p style="margin-bottom: 20px;">
            📞 <a href="tel:+393929334563" style="font-size: 20px;">+39 392 933 4563</a>
        </p>
        
        <a href="https://wa.me/393929334563" class="wa-button">🗨️ WHATSAPP</a>
        
        <div style="margin-top: 30px; font-size: 12px; color: #888;">
            Partner <a href="https://www.superstart.it" target="_blank">SuPeR</a> | Powered by Streamlit
        </div>
    </div>
""", unsafe_allow_html=True)

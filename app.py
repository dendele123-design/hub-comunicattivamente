import streamlit as st

# =================================================================
# 1. CONFIGURAZIONE E DESIGN (#DC0612)
# =================================================================
st.set_page_config(page_title="comunicAttivamente Hub", page_icon="🛡️", layout="centered")

ROSSO_BRAND = "#DC0612"

st.markdown(f"""
<style>
header {{visibility: hidden !important;}}
.stApp {{ background-color: #ffffff !important; }}

/* FORZA TUTTI I TESTI FUORI DEI BOX */
html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, div {{
color: #1a1a1a !important;
}}

/* HEADER HUB */
.hub-header {{
text-align: center;
padding: 10px;
border-bottom: 2px solid #eee;
margin-bottom: 30px;
}}
.super-text {{ color: {ROSSO_BRAND} !important; font-weight: 900; }}

/* CARD APP CON STRISCIA ROSSA */
.app-card {{
background-color: #f8f9fa !important;
padding: 20px;
border-radius: 15px;
border-left: 10px solid {ROSSO_BRAND} !important;
margin-bottom: 10px;
box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}}
.app-title {{ font-size: 22px; font-weight: bold; color: #1a1a1a !important; margin-bottom: 5px; }}
.app-desc {{ font-size: 15px; color: #555 !important; line-height: 1.4; }}

/* BOTTONI ROSSI DESATURATI */
.stLinkButton>a {{
width: 200px !important;
background-color: {ROSSO_BRAND} !important;
opacity: 0.9;
color: white !important;
font-weight: bold !important;
border-radius: 10px !important;
height: 3.5em !important;
display: flex !important;
align-items: center !important;
justify-content: center !important;
text-decoration: none !important;
margin-bottom: 30px !important;
}}

/* AREA EBOOK CHIARA */
.ebook-section-light {{
background-color: #f9f9f9 !important;
padding: 30px;
border-radius: 20px;
text-align: center;
margin: 40px 0;
border: 2px dashed {ROSSO_BRAND};
}}

/* FOOTER CONTENITORE */
.footer-container {{
text-align: center;
padding: 30px;
background-color: #f1f1f1 !important;
border-radius: 20px;
margin-top: 50px;
}}
.wa-button {{
background-color: #25D366;
color: white !important;
padding: 12px 30px;
border-radius: 50px;
text-decoration: none;
font-weight: bold;
display: inline-block;
margin-top: 15px;
}}
</style>
""", unsafe_allow_html=True)

# =================================================================
# 2. INTESTAZIONE
# =================================================================
st.markdown(f"""
<div class="hub-header">
<h1 style="font-size: 28px; margin:0;">comunicattivamente | <span class="super-text">SuPeR</span></h1>
<p style="font-weight: bold; color: #666 !important; margin:0;">Esorcismo del Caos Aziendale</p>
</div>
""", unsafe_allow_html=True)

# =================================================================
# 3. ELENCO DELLE APP (CORRETTO)
# =================================================================
apps = [
    {
        "titolo": "📊 Test Diagnostico ANSIA S.P.A.", 
        "desc": "Scopri se sei un Titolare Criceto con il test completo in 20 punti.", 
        "url": "https://comunicattivamente-test.streamlit.app/"
    },
    {
        "titolo": "🚑 Pronto Soccorso Aziendale", 
        "desc": "Calcola il tuo Profit Leak: quanto ti costano riunioni e notifiche ogni anno.", 
        "url": "https://toolkit-comunicattivamente.streamlit.app/"
    },
    {
        "titolo": "🏢 SuPeR - HORECA Edition", 
        "desc": "Gestione operativa per ristorazione: Chiusura Cassa e Registro HACCP.", 
        "url": "https://super-horeca-yewtxo4nqtumhvvo2c27zu.streamlit.app/"
    },
    {
        "titolo": "🍷 Wine Selector 2.0", 
        "desc": "Sommelier Digitale e Carta Vini interattiva per un servizio di lusso.", 
        "url": "https://carta-vini-digitale-2-0.streamlit.app/"
    }
]

for app in apps:
    st.markdown(f"""
<div class="app-card">
<div class="app-title">{app['titolo']}</div>
<div class="app-desc">{app['desc']}</div>
</div>
""", unsafe_allow_html=True)
    st.link_button("APRI WEB APP 🚀", app['url'])

# =================================================================
# 4. AREA EBOOK CHIARA
# =================================================================
st.markdown(f"""
<div class="ebook-section-light">
<h2 style="margin-top:0; color:{ROSSO_BRAND} !important;">📘 RISORSA GRATUITA</h2>
<p style="font-size:16px;">Scarica l'Ebook <b>"ANSIA S.P.A."</b> e impara a riprenderti il tuo tempo.</p>
<a href="https://www.comunicattivamente.it/ebook-ansia-spa" target="_blank" 
style="background-color:{ROSSO_BRAND}; color:white !important; padding:12px 25px; border-radius:50px; text-decoration:none; font-weight:bold; display:inline-block; margin-top:10px;">
SCARICA L'EBOOK ORA
</a>
</div>
""", unsafe_allow_html=True)

# =================================================================
# 5. FOOTER (STILE RICHIESTO)
# =================================================================
footer_html = f"""
<div class="footer-container">
<p style="font-size: 18px; font-weight: bold; margin-bottom: 5px;">
Daniele Salvatori | <a href="https://www.comunicattivamente.it" target="_blank" style="color:{ROSSO_BRAND} !important;">comunicAttivamente</a>
</p>
<p style="margin-bottom: 20px; font-weight: bold; color: #555 !important;">Esorcismo del Caos Aziendale</p>
<p style="margin-bottom: 5px;">
📧 <a href="mailto:daniele@comunicattivamente.it" style="color:{ROSSO_BRAND} !important;">daniele@comunicattivamente.it</a>
</p>
<p style="margin-bottom: 20px;">
📞 <a href="tel:+393929334563" style="font-size: 20px; color:{ROSSO_BRAND} !important; text-decoration:none;">+39 392 933 4563</a>
</p>
<a href="https://wa.me/393929334563" class="wa-button">🗨️ WHATSAPP</a>
<div style="margin-top: 30px; font-size: 12px; color: #888 !important;">
Partner <a href="https://www.superstart.it" target="_blank" style="color:#888 !important; text-decoration:underline;">SuPeR</a> | Powered by Streamlit
</div>
</div>"""

st.markdown(footer_html, unsafe_allow_html=True)

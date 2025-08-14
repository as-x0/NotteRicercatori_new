import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# --- Caricamento dati ---
df = pd.read_csv("FAOSTAT_data_en_8-10-2025.csv")

# --- Config pagina ---
st.set_page_config(page_title="Gioco Export FAOSTAT", page_icon="🌾")

# --- Dizionario prodotti inglese -> italiano ---
traduzioni_prodotti = {
    "Coffee, green": "Caffè",
    "Maize (corn)": "Mais",
    "Rice, paddy (rice milled equivalent)": "Riso",
    "Tomatoes": "Pomodori",
    "Soya beans": "Fagioli di soia",
    "Wheat": "Grano",
    "Cocoa beans": "Cacao",
    "Bananas": "Banane",
}

prodotti_inglese = sorted(df["Item"].unique())
prodotti_italiano = [traduzioni_prodotti.get(p, p) for p in prodotti_inglese]

anni = sorted(df["Year"].unique(), reverse=True)

mappa_paesi = {
    "Afghanistan": "Afghanistan",
    "Albania": "Albania",
    "Algeria": "Algeria",
    "Angola": "Angola",
    "Antigua and Barbuda": "Antigua e Barbuda",
    "Argentina": "Argentina",
    "Armenia": "Armenia",
    "Australia": "Australia",
    "Austria": "Austria",
    "Azerbaijan": "Azerbaigian",
    "Bahamas": "Bahamas",
    "Bahrain": "Bahrein",
    "Bangladesh": "Bangladesh",
    "Barbados": "Barbados",
    "Belarus": "Bielorussia",
    "Belgium": "Belgio",
    "Belize": "Belize",
    "Benin": "Benin",
    "Bhutan": "Bhutan",
    "Bolivia (Plurinational State of)": "Bolivia",
    "Bosnia and Herzegovina": "Bosnia-Erzegovina",
    "Botswana": "Botswana",
    "Brazil": "Brasile",
    "Brunei Darussalam": "Brunei",
    "Bulgaria": "Bulgaria",
    "Burkina Faso": "Burkina Faso",
    "Burundi": "Burundi",
    "Cabo Verde": "Capo Verde",
    "Cambodia": "Cambogia",
    "Cameroon": "Camerun",
    "Canada": "Canada",
    "Central African Republic": "Repubblica Centrafricana",
    "Chile": "Cile",
    "China, Hong Kong SAR": "Honk Kong",
    "China, Macao SAR": "Macao",
    "China, mainland": "Cina",
    "China, Taiwan Province of": "Taiwan",
    "Colombia": "Colombia",
    "Comoros": "Comore",
    "Congo": "Congo",
    "Costa Rica": "Costa Rica",
    "Côte d'Ivoire": "Costa d'Avorio",
    "Croatia": "Croazia",
    "Cuba": "Cuba",
    "Cyprus": "Cipro",
    "Czechia": "Repubblica Ceca",
    "Democratic People's Republic of Korea": "Corea del Nord",
    "Democratic Republic of the Congo": "Repubblica Democratica del Congo",
    "Denmark": "Danimarca",
    "Djibouti": "Gibuti",
    "Dominica": "Dominica",
    "Dominican Republic": "Repubblica Dominicana",
    "Ecuador": "Ecuador",
    "Egypt": "Egitto",
    "El Salvador": "El Salvador",
    "Equatorial Guinea": "Guinea Equatoriale",
    "Eritrea": "Eritrea",
    "Estonia": "Estonia",
    "Eswatini": "Eswatini",
    "Ethiopia": "Etiopia",
    "Fiji": "Fiji",
    "Finland": "Finlandia",
    "France": "Francia",
    "French Polynesia": "Polinesia Francese",
    "Gabon": "Gabon",
    "Gambia": "Gambia",
    "Georgia": "Georgia",
    "Germany": "Germania",
    "Ghana": "Ghana",
    "Greece": "Grecia",
    "Grenada": "Grenada",
    "Guatemala": "Guatemala",
    "Guinea": "Guinea",
    "Guyana": "Guyana",
    "Haiti": "Haiti",
    "Honduras": "Honduras",
    "Hungary": "Ungheria",
    "Iceland": "Islanda",
    "India": "India",
    "Indonesia": "Indonesia",
    "Iran (Islamic Republic of)": "Iran",
    "Iraq": "Iraq",
    "Ireland": "Irlanda",
    "Israel": "Israele",
    "Italy": "Italia",
    "Jamaica": "Giamaica",
    "Japan": "Giapone",
    "Jordan": "Giordania",
    "Kazakhstan": "Kazakistan",
    "Kenya": "Kenya",
    "Kuwait": "Kuwait",
    "Kyrgyzstan": "Kirghizistan",
    "Lao People's Democratic Republic": "Lao",
    "Latvia": "Lettonia",
    "Lebanon": "Libano",
    "Lesotho": "Lesotho",
    "Liberia": "Liberia",
    "Libya": "Libia",
    "Lithuania": "Lituania",
    "Luxembourg": "Lussemburgo",
    "Madagascar": "Madagascar",
    "Malawi": "Malawi",
    "Malaysia": "Malaysia",
    "Mali": "Mali",
    "Malta": "Malta",
    "Mauritius": "Mauritius",
    "Mexico": "Messico",
    "Montenegro": "Montenegro",
    "Morocco": "Marocco",
    "Mozambique": "Mozambico",
    "Myanmar": "Myanmar",
    "Namibia": "Namibia",
    "Nepal": "Nepal",
    "Netherlands (Kingdom of the)": "Paesi Bassi",
    "New Caledonia": "Nuova Caledonia",
    "New Zealand": "Nuova Zelanda",
    "Nicaragua": "Nicaragua",
    "Niger": "Niger",
    "Nigeria": "Nigeria",
    "North Macedonia": "Macedonia del Nord",
    "Norway": "Norvegia",
    "Oman": "Oman",
    "Pakistan": "Pakistan",
    "Palestine": "Palestina",
    "Panama": "Panama",
    "Papua New Guinea": "Papua Nuova Guinea",
    "Paraguay": "Paraguay",
    "Peru": "Perù",
    "Philippines": "Filippine",
    "Poland": "Polonia",
    "Portugal": "Portogallo",
    "Qatar": "Qatar",
    "Republic of Korea": "Corea del Sud",
    "Republic of Moldova": "Moldavia",
    "Romania": "Romania",
    "Russian Federation": "Russia",
    "Rwanda": "Ruanda",
    "Saint Kitts and Nevis": "Saint Kitts and Nevis",
    "Saint Lucia": "Saint Lucia",
    "Saint Vincent and the Grenadines": "Saint Vincent e Grenadines",
    "Samoa": "Samoa",
    "Sao Tome and Principe": "Sao Tomé e Príncipe",
    "Saudi Arabia": "Arabia Saudita",
    "Senegal": "Senegal",
    "Serbia": "Serbia",
    "Seychelles": "Seychelles",
    "Sierra Leone": "Sierra Leone",
    "Singapore": "Singapore",
    "Slovakia": "Slovacchia",
    "Slovenia": "Slovenia",
    "Solomon Islands": "Isole Salomone",
    "South Africa": "Sudafrica",
    "South Sudan": "Sudan del Sud",
    "Spain": "Spagna",
    "Sri Lanka": "Sri Lanka",
    "Sudan": "Sudan",
    "Suriname": "Suriname",
    "Sweden": "Svezia",
    "Switzerland": "Svizzera",
    "Syrian Arab Republic": "Siria",
    "Tajikistan": "Tagikistan",
    "Thailand": "Thailandia",
    "Timor-Leste": "Timor Est",
    "Togo": "Togo",
    "Tonga": "Tonga",
    "Trinidad and Tobago": "Trinidad e Tobago",
    "Tunisia": "Tunisia",
    "Türkiye": "Turchia",
    "Turkmenistan": "Turkmenistan",
    "Uganda": "Uganda",
    "Ukraine": "Ucraina",
    "United Arab Emirates": "Emirati Arabi Uniti",
    "United Kingdom of Great Britain and Northern Ireland": "Regno Unito",
    "United Republic of Tanzania": "Tanzania",
    "United States of America": "Stati Uniti",
    "Uruguay": "Uruguay",
    "Uzbekistan": "Uzbekistan",
    "Vanuatu": "Vanuatu",
    "Venezuela (Bolivarian Republic of)": "Venezuela",
    "Viet Nam": "Vietnam",
    "Yemen": "Yemen",
    "Zambia": "Zambia",
    "Zimbabwe": "Zimbabwe",
}

mappa_paesi_inv = {v: k for k, v in mappa_paesi.items()}
paesi_inglese = sorted(df["Area"].unique())
paesi_italiano = [mappa_paesi.get(p, p) for p in paesi_inglese]

# --- Inizializza session state ---
if 'step' not in st.session_state:
    st.session_state.step = "home"  # home, inserimento, punteggi

if 'num_paesi' not in st.session_state:
    st.session_state.num_paesi = 3

if 'n_partecipanti' not in st.session_state:
    st.session_state.n_partecipanti = 1

if 'partecipanti' not in st.session_state:
    st.session_state.partecipanti = {}

if 'indice_giocatore' not in st.session_state:
    st.session_state.indice_giocatore = 0

if 'prodotto_italiano' not in st.session_state:
    st.session_state.prodotto_italiano = prodotti_italiano[0]

if 'anno' not in st.session_state:
    st.session_state.anno = anni[0]

# --- Funzioni per bottoni ---

def inizia_gioco():
    st.session_state.step = "inserimento"
    st.session_state.partecipanti = {}
    st.session_state.indice_giocatore = 0

def avanti_giocatore(nome, paesi_scelti_italiano):
    if nome and len(paesi_scelti_italiano) == st.session_state.num_paesi:
        # salva partecipante convertendo paesi in inglese
        paesi_scelti_inglese = [mappa_paesi_inv.get(p, p) for p in paesi_scelti_italiano]
        st.session_state.partecipanti[nome] = paesi_scelti_inglese
        st.session_state.indice_giocatore += 1
        if st.session_state.indice_giocatore >= st.session_state.n_partecipanti:
            st.session_state.step = "punteggi"

def calcola_punteggi():
    st.session_state.step = "punteggi"

def torna_home():
    st.session_state.step = "home"
    st.session_state.partecipanti = {}
    st.session_state.indice_giocatore = 0

# --- UI ---

st.title("🌾 Gioco sugli esportatori - FAOSTAT")

if st.session_state.step == "home":
    # Scelte iniziali
    st.session_state.prodotto_italiano = st.selectbox("Scegli prodotto", prodotti_italiano, index=prodotti_italiano.index(st.session_state.prodotto_italiano))
    st.session_state.num_paesi = st.radio("Quanti paesi per giocatore?", [3, 5], index=[3, 5].index(st.session_state.num_paesi))
    st.session_state.n_partecipanti = st.number_input("Numero di partecipanti", min_value=1, step=1, value=st.session_state.n_partecipanti)
    st.session_state.anno = st.selectbox("Scegli anno", anni, index=anni.index(st.session_state.anno))

    if st.button("Inizia"):
        inizia_gioco()

elif st.session_state.step == "inserimento":
    i = st.session_state.indice_giocatore
    nome = st.text_input(f"Nome partecipante {i+1}", key=f"nome_{i}")
    paesi_scelti_italiano = st.multiselect(
        f"Scegli {st.session_state.num_paesi} paesi per {nome}",
        paesi_italiano,
        key=f"paesi_{i}"
    )

    if st.session_state.n_partecipanti == 1:
        # Solo un giocatore → mostra Calcola punteggi
        if st.button("Calcola punteggi"):
            if nome and len(paesi_scelti_italiano) == st.session_state.num_paesi:
                avanti_giocatore(nome, paesi_scelti_italiano)
    else:
        # Più giocatori → bottone "Invia" per ogni giocatore tranne l'ultimo
        if i < st.session_state.n_partecipanti - 1:
            if st.button("Invia"):
                if nome and len(paesi_scelti_italiano) == st.session_state.num_paesi:
                    avanti_giocatore(nome, paesi_scelti_italiano)
        else:
            if st.button("Calcola punteggi"):
                if nome and len(paesi_scelti_italiano) == st.session_state.num_paesi:
                    avanti_giocatore(nome, paesi_scelti_italiano)

elif st.session_state.step == "punteggi":
    prodotto_italiano = st.session_state.prodotto_italiano
    prodotto_idx = prodotti_italiano.index(prodotto_italiano)
    prodotto = prodotti_inglese[prodotto_idx]
    anno = st.session_state.anno

    df_filtrato = df[
        (df["Item"] == prodotto) &
        (df["Year"] == anno) &
        (df["Element"].str.lower().str.contains("export"))
    ].dropna(subset=["Value"]).sort_values(by="Value", ascending=False)

    totale_mondiale = df_filtrato["Value"].sum()

    punteggi = {}
    for nome, paesi in st.session_state.partecipanti.items():
        totale = 0
        for paese in paesi:
            riga = df_filtrato[df_filtrato["Area"].str.lower() == paese.lower()]
            if not riga.empty:
                totale += riga["Value"].values[0]
        punteggi[nome] = totale

    classifica = sorted(punteggi.items(), key=lambda x: x[1], reverse=True)
    st.subheader("🏆 Classifica")
    for pos, (nome, punti) in enumerate(classifica, start=1):
        st.write(f"{pos}. **{nome}** → {punti:,.0f} t ({punti/totale_mondiale*100:.2f}%)")

    top5 = df_filtrato.head(5).copy()
    top5["Percentuale"] = top5["Value"] / totale_mondiale * 100

    st.subheader("🌍 Top 5 reale")
    for _, row in top5.iterrows():
        paese_it = mappa_paesi.get(row["Area"], row["Area"])
        st.write(f"{paese_it}: {row['Value']:,.0f} t ({row['Percentuale']:.2f}%)")

    st.write(f"**Totale cumulato Top 5**: {top5['Value'].sum():,.0f} t ({top5['Percentuale'].sum():.2f}%)")

    # Grafico
    fig, ax = plt.subplots()
    ax.bar(top5["Area"].map(mappa_paesi), top5["Value"])
    ax.set_title(f"Export {prodotto_italiano} nel {anno}")
    ax.set_ylabel("Quantità")
    st.pyplot(fig)

    if st.button("Torna alla Home"):
        torna_home()

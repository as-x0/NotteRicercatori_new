import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Carica il CSV FAOSTAT (metti il percorso giusto)
df = pd.read_csv("FAOSTAT_data_en_8-10-2025.csv")

st.set_page_config(page_title="Gioco Export FAOSTAT", page_icon="🌾")

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

if 'prodotto_italiano' not in st.session_state:
    st.session_state.prodotto_italiano = None
    
prodotto_italiano = st.selectbox("Scegli prodotto", prodotti_italiano)

if prodotto_italiano != st.session_state.prodotto_italiano:
     st.session_state.prodotto_italiano = prodotto_italiano

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
    "China": "Cina",
    "China, Hong Kong SAR": "Honk Kong",
    "China, Macao SAR": "Macao",
    "China, mainland": "",
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

# --- Stato iniziale in session_state ---
if "step" not in st.session_state:
    st.session_state.step = "start"  # start, input_players, results
if "partecipanti" not in st.session_state:
    st.session_state.partecipanti = {}
if "current_player" not in st.session_state:
    st.session_state.current_player = 0

# Funzione reset per tornare all'inizio
def reset():
    st.session_state.step = "start"
    st.session_state.partecipanti = {}
    st.session_state.current_player = 0

# --- Step START ---
if st.session_state.step == "start":
    st.title("🌾 Gioco sugli esportatori - FAOSTAT")

    # Scelta prodotto
    prodotto_italiano = st.selectbox("Scegli prodotto", prodotti_italiano, key="prodotto_italiano")

    # Numero paesi per giocatore
    num_paesi = st.radio("Quanti paesi per giocatore?", [3, 5], key="num_paesi")

    # Numero partecipanti
    n_partecipanti = st.number_input("Numero di partecipanti", min_value=1, step=1, key="n_partecipanti")

    if st.button("Inizia"):
        # Salva valori in session_state
        st.session_state.prodotto_italiano = prodotto_italiano
        st.session_state.num_paesi = num_paesi
        st.session_state.n_partecipanti = n_partecipanti
        st.session_state.anno = anni[0]  # anno di default: il più recente
        st.session_state.step = "input_players"
        st.session_state.current_player = 0
        st.session_state.partecipanti = {}

# --- Step INPUT PLAYERS ---
elif st.session_state.step == "input_players":
    # Mostra titolo con prodotto e anno (fisso a più recente per semplicità)
    st.title(f"🌾 Gioco Export - {st.session_state.prodotto_italiano} ({anni[0]})")

    i = st.session_state.current_player
    n = st.session_state.n_partecipanti
    num_paesi = st.session_state.num_paesi

    st.write(f"Partecipante {i+1} di {n}")

    # Inserisci nome
    nome = st.text_input("Inserisci nome", key=f"nome_{i}")

    # Scegli paesi (multiselect)
    paesi_scelti_italiano = st.multiselect(
        f"Scegli {num_paesi} paesi",
        paesi_italiano,
        key=f"paesi_{i}"
    )

    # Pulsante dinamico
    if i == n - 1:
        btn_text = "Calcola punteggi"
    else:
        btn_text = "Invia"

    if st.button(btn_text):
        # Controlla che nome e paesi siano corretti
        if not nome:
            st.warning("Inserisci un nome valido")
        elif len(paesi_scelti_italiano) != num_paesi:
            st.warning(f"Seleziona esattamente {num_paesi} paesi")
        else:
            # Salva partecipante convertendo i paesi in inglese
            paesi_scelti_inglese = [mappa_paesi_inv.get(p, p) for p in paesi_scelti_italiano]
            st.session_state.partecipanti[nome] = paesi_scelti_inglese

            if i == n - 1:
                st.session_state.step = "results"
            else:
                st.session_state.current_player += 1
            st.experimental_rerun()  # aggiorna pagina per mostrare input del prossimo giocatore o risultati

# --- Step RESULTS ---
elif st.session_state.step == "results":
    st.title("🏆 Risultati Gioco Export FAOSTAT")

    prodotto_italiano = st.session_state.prodotto_italiano
    num_paesi = st.session_state.num_paesi
    partecipanti = st.session_state.partecipanti
    anno = anni[0]

    # Filtro dati come nel tuo codice originale
    prodotto = prodotti_inglese[prodotti_italiano.index(prodotto_italiano)]
    df_filtrato = df[
        (df["Item"] == prodotto) &
        (df["Year"] == anno) &
        (df["Element"].str.lower().str.contains("export"))
    ].dropna(subset=["Value"]).sort_values(by="Value", ascending=False)

    totale_mondiale = df_filtrato["Value"].sum()

    punteggi = {}
    for nome, paesi in partecipanti.items():
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

    fig, ax = plt.subplots()
    top5_paesi_it = [mappa_paesi.get(p, p) for p in top5["Area"]]
    ax.bar(top5_paesi_it, top5["Percentuale"])
    ax.set_ylabel("% sul totale mondiale")
    ax.set_title(f"Top 5 export {prodotto_italiano} ({anno})")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    if st.button("Home"):
        reset()
        st.experimental_rerun()

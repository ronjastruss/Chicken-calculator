
import streamlit as st
import datetime

st.set_page_config(page_title="Chicken Calculator 🐔", layout="centered")

st.title("🐣 Chicken Calculator – Wochenalter-Rechner für Hennen")

einstalldatum = st.date_input("📅 Einstalldatum")
wochen = st.number_input("Wie viele Wochen alt waren die Hennen beim Einstallen?", min_value=0, step=1)
tage = st.number_input("...und wie viele Tage zusätzlich?", min_value=0, max_value=6, step=1)

startdatum = einstalldatum - datetime.timedelta(weeks=wochen, days=tage)

st.markdown("---")
modus = st.radio("Was möchtest du berechnen?", [
    "Wochenalter der Hennen für ein bestimmtes Datum",
    "Wie ist das Wochenalter der Hennen an Datum X"
])

if modus == "Wochenalter der Hennen für ein bestimmtes Datum":
    zieldatum = st.date_input("Wähle ein Datum")
    differenz = (zieldatum - startdatum).days
    result_wochen = differenz // 7
    result_tage = differenz % 7
    st.success(f"Die Hühner sind an diesem Tag **{result_wochen} Wochen und {result_tage} Tage** alt.")
else:
    ziel_wochen = st.number_input("Gib das gewünschte Wochenalter ein", min_value=0, step=1)
    ziel_tage = st.number_input("...und wie viele Tage?", min_value=0, max_value=6, step=1)
    ziel_datum = startdatum + datetime.timedelta(weeks=ziel_wochen, days=ziel_tage)
    st.success(f"Die Hühner sind am **{ziel_datum.strftime('%d.%m.%Y')}** genau {ziel_wochen} Wochen und {ziel_tage} Tage alt.")

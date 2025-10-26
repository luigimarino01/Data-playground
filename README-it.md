# 🎡 Data Playground

[![en](https://img.shields.io/badge/lang-en-blue.svg)](README.md)

## Online dashboard
La dashboard è anche disponibile al seguente link:
**https://data-playground.streamlit.app/**

## Informazioni
**Strumento interattivo per l'esplorazione e la trasformazione dei dati costruito con Streamlit.**

Questa dashboard permette di caricare dataset, esplorarli in modo interattivo e applicare comuni operazioni della libreria Pandas per la pulizia e la trasformazione dei dati.  
⚠️ **Nota:** Questo progetto è in fase di sviluppo attivo — nuove funzionalità vengono aggiunte regolarmente.

---
## Dashboard 
![dashboard](img/dashboard.png)
---
## Funzionalità
> 🕓 Le funzionalità elencate di seguito si riferiscono all'ultimo commit
- Caricamento di dataset in formato **CSV**, **Excel**, o **JSON**.
- Anteprima del dataset:
  - Mostra l'intero dataset
  - Mostra le prime N righe
  - Mostra le ultime N righe
  - Mostra le righe da N a M
- Trasforma i tuoi dati in modo interattivo:
  - Rimuovi i valori nulli
  - Rimuovi le righe duplicate
- Riepilogo del dataset nella barra laterale:
  - Forma, righe, colonne
  - Valori mancanti per colonna
  - Riepilogo delle colonne numeriche
- Esporta il dataset trasformato in `data/processed/exported_data.csv`.

---

## Installazione

1. Clona il repository:
```bash
git clone https://github.com/luigimarino01/Data-playground.git
cd Data-playground
```
2. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

---

## Utilizzo
Avvia l'applicazione Streamlit:
```bash
streamlit run app.py
```
- Apri l'URL fornito da Streamlit nel tuo browser.
- Carica il tuo dataset e inizia a esplorare e trasformare i tuoi dati in modo interattivo.

---

## Contribuire

Questo progetto è un esperimento personale di apprendimento ed è in fase di costruzione.  
Contributi e suggerimenti per nuove funzionalità sono benvenuti!

---

## Autore

**Luigi Marino** - [GitHub](https://github.com/luigimarino01)

---

## Licenza

Questo progetto è open-source e libero di essere utilizzato per scopi di apprendimento e sperimentazione.
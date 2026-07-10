# Modello dati SalonOS

## Principio principale

Ogni salone ha un ambiente separato.

I dati di un salone non possono mai essere visibili ad un altro salone.

---

# Entità principali

## Salone

Contiene:

- nome;
- indirizzo;
- telefono;
- orari;
- impostazioni AI;
- abbonamento.

---

## Utente

Contiene:

- nome;
- email;
- ruolo;
- permessi;
- salone associato.

---

## Cliente

Contiene:

- nome;
- telefono;
- storico appuntamenti;
- preferenze;
- note.

---

## Servizio

Contiene:

- nome servizio;
- prezzo;
- durata;
- categoria.

Esempio:

Taglio uomo
25 €
30 minuti

---

## Appuntamento

Contiene:

- cliente;
- servizio;
- data;
- orario;
- dipendente;
- stato.

---

## Conversazione AI

Contiene:

- cliente;
- messaggi;
- richieste;
- risultato.

---

# Regola AI

Quando un cliente scrive:

"Quanto costa il taglio?"

SalonOS deve prima identificare il salone.

Poi deve leggere solo i dati di quel salone.

---

# Obiettivo

Creare una piattaforma unica capace di gestire migliaia di saloni indipendenti.

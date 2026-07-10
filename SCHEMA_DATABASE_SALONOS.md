# Schema Database SalonOS

## Obiettivo

Creare la struttura della memoria di SalonOS.

Il database deve permettere di gestire migliaia di saloni diversi mantenendo i dati completamente separati.

---

# Tabella Saloni

Contiene le informazioni principali dell'attività.

Campi:

- ID salone
- Nome salone
- Indirizzo
- Telefono
- Email
- Orari apertura
- Giorni apertura
- Stile comunicazione AI
- Piano abbonamento
- Data creazione

---

# Tabella Utenti

Contiene le persone che utilizzano SalonOS.

Campi:

- ID utente
- Nome
- Email
- Password protetta
- Ruolo
- ID salone associato

Ruoli:

- Proprietario
- Dipendente
- Amministratore SalonOS

---

# Tabella Clienti

Contiene i clienti del salone.

Campi:

- ID cliente
- Nome
- Cognome
- Numero telefono
- Email
- Preferenze
- Note
- Data ultima visita
- ID salone associato

---

# Tabella Servizi

Contiene i trattamenti offerti.

Campi:

- ID servizio
- Nome servizio
- Categoria
- Prezzo
- Durata
- ID salone associato

Esempio:

Taglio uomo  
25 €  
30 minuti

---

# Tabella Dipendenti

Contiene il personale del salone.

Campi:

- ID dipendente
- Nome
- Ruolo
- Orari disponibili
- ID salone associato

---

# Tabella Appuntamenti

Contiene tutte le prenotazioni.

Campi:

- ID appuntamento
- Cliente associato
- Servizio richiesto
- Dipendente assegnato
- Data
- Orario
- Stato appuntamento
- ID salone associato

Stati:

- Richiesto
- Confermato
- Completato
- Annullato

---

# Tabella Conversazioni AI

Memorizza le comunicazioni tra cliente e assistente.

Campi:

- ID conversazione
- Cliente
- Messaggi
- Data
- Risultato conversazione
- ID salone associato

---

# Tabella Impostazioni AI

Contiene la personalizzazione dell'assistente.

Campi:

- ID impostazione
- Stile comunicazione
- Formalità
- Uso emoji
- Lingua
- Regole personalizzate
- ID salone associato

---

# Regola fondamentale sicurezza

Ogni dato deve essere collegato al proprio ID salone.

Un salone può vedere solo:

- i propri clienti;
- i propri appuntamenti;
- i propri servizi;
- le proprie conversazioni.

Nessun dato può essere condiviso tra saloni diversi.

---

# Obiettivo finale

Creare una base dati scalabile che permetta a SalonOS di crescere da pochi saloni fino a migliaia di attività.

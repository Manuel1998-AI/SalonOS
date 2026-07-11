# Test Demo SalonOS V1

## Test 1 - Richiesta prezzo

Cliente:

"Quanto costa il taglio uomo?"

Risultato atteso:

SalonOS risponde con:
- nome servizio;
- prezzo;
- durata.

---

## Test 2 - Prenotazione completa

Cliente:

"Vorrei un taglio sabato alle 16"

Risultato atteso:

SalonOS:
- riconosce il servizio;
- riconosce giorno e ora;
- controlla disponibilità;
- prepara prenotazione.

---

## Test 3 - Informazioni mancanti

Cliente:

"Vorrei prenotare un taglio"

Risultato atteso:

SalonOS chiede:
- giorno;
- orario.

---

## Test 4 - Servizio non trovato

Cliente:

"Vorrei fare un trattamento speciale"

Risultato atteso:

SalonOS chiede maggiori informazioni.

---

# Obiettivo finale

Il cliente deve poter iniziare una conversazione naturale e arrivare alla prenotazione.

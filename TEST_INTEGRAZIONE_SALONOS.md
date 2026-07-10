# Test Integrazione SalonOS

## Test 1 - Stato sistema

Azione:

Il frontend richiede lo stato del backend.

Risultato atteso:

Il backend risponde correttamente.

---

## Test 2 - Richiesta cliente

Azione:

Il cliente scrive:

"Quanto costa il taglio uomo?"

Risultato atteso:

Receptionist AI restituisce prezzo e durata.

---

## Test 3 - Prenotazione

Azione:

Il cliente richiede:

"Vorrei un appuntamento sabato alle 16."

Risultato atteso:

- verifica disponibilità;
- creazione appuntamento;
- conferma cliente.

---

## Test 4 - Separazione saloni

Azione:

Un utente accede al proprio salone.

Risultato atteso:

Può vedere solo i propri dati.

---

# Obiettivo

Verificare che i componenti principali di SalonOS comunichino correttamente.

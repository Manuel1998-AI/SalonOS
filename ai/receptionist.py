# Receptionist AI SalonOS


from backend.backend.app.services import lista_servizi
from backend.backend.app.booking_engine import crea_prenotazione
from ai.booking_parser import estrai_dati_prenotazione



def rispondi_cliente(messaggio):

    messaggio = messaggio.lower()


    dati_prenotazione = estrai_dati_prenotazione(
        messaggio
    )


    servizi = lista_servizi()



    for servizio in servizi:

        if servizio["nome"].lower() in messaggio:

            return (
                f"{servizio['nome']} costa "
                f"{servizio['prezzo']} euro "
                f"e dura circa "
                f"{servizio['durata']} minuti."
            )



    if dati_prenotazione["servizio"]:


        if dati_prenotazione["giorno"] and dati_prenotazione["ora"]:


            risultato = crea_prenotazione(
                "Cliente",
                dati_prenotazione["servizio"],
                dati_prenotazione["giorno"],
                dati_prenotazione["ora"]
            )


            if risultato["stato"] == "confermata":

                appuntamento = risultato["appuntamento"]

                return (
                    "Perfetto! Ho preparato la tua prenotazione:\n"
                    f"Servizio: {appuntamento['servizio']}\n"
                    f"Giorno: {appuntamento['data']}\n"
                    f"Ora: {appuntamento['orario']}"
                )


            return "Mi dispiace, questo orario non è disponibile."


        return (
            "Perfetto, posso aiutarti con la prenotazione. "
            "Mi serve solo il giorno e l'orario preferito."
        )



    if "prezzo" in messaggio or "costo" in messaggio:

        return (
            "Dimmi quale servizio ti interessa "
            "e ti comunicherò prezzo e durata."
        )



    if "appuntamento" in messaggio or "prenotare" in messaggio:

        return (
            "Certo, posso aiutarti a prenotare. "
            "Dimmi quale servizio vuoi scegliere."
        )



    return (
        "Ciao! Sono l'assistente SalonOS. "
        "Come posso aiutarti?"
    )

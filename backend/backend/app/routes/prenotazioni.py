from fastapi import APIRouter

router = APIRouter()


@router.get("/prenotazioni")
def lista_prenotazioni():
    return {
        "prenotazioni": [],
        "messaggio": "Nessuna prenotazione presente"
    }


@router.post("/prenotazioni")
def crea_prenotazione():
    return {
        "stato": "Prenotazione ricevuta",
        "messaggio": "La richiesta è stata registrata"
    }

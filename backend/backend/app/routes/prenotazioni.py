from fastapi import APIRouter

from booking_engine import crea_prenotazione


router = APIRouter()



@router.get("/prenotazioni")
def lista_prenotazioni():

    return {
        "stato": "Sistema prenotazioni attivo"
    }



@router.post("/prenotazioni")
def nuova_prenotazione(
    cliente: str,
    servizio: str,
    data: str,
    orario: str
):

    risultato = crea_prenotazione(
        cliente,
        servizio,
        data,
        orario
    )

    return risultato

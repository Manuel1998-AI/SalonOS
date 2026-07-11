from fastapi import APIRouter

from ai import receptionist


router = APIRouter()



@router.post("/chat")
def chat_cliente(messaggio: str):

    risposta = receptionist.rispondi_cliente(
        messaggio
    )

    return {
        "messaggio_cliente": messaggio,
        "risposta_ai": risposta
    }

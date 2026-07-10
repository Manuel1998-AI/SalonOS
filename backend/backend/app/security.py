# Sicurezza accessi SalonOS

def verifica_accesso(utente, salone_id):

    if utente["salone_id"] == salone_id:
        return True

    return False

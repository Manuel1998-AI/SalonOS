# Configurazione database SalonOS

DATABASE_NAME = "SalonOS"

DATABASE_STATUS = "Configurazione iniziale"


def get_database_info():
    return {
        "database": DATABASE_NAME,
        "stato": DATABASE_STATUS
    }

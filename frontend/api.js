const API_URL = "http://localhost:8000";


async function statoSalonOS(){

    const risposta = await fetch(API_URL);

    const dati = await risposta.json();

    console.log(dati);

}

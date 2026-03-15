const API_URL = "http://127.0.0.1:5000/hoteis"


async function getHotels(page = 1, search = ""){

    try{

        let url = `${API_URL}?page=${page}`

        if(search){
            url += `&busca=${search}`
        }

        const response = await fetch(url)

        const data = await response.json()

        return data

    }catch(error){

        console.error("Erro ao buscar hotéis:", error)

    }

}

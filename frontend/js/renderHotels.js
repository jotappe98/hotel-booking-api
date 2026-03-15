//renderização dos hotéis

let allHotels = []
let startIndex = 0
const visibleCards = 5

async function loadHotels(page = 1, search = "") {

    const data = await getHotels(page, search)

    totalPages = data.total_paginas

    // adiciona novos hotéis ao cache
    allHotels = [...allHotels, ...data.hoteis]

    renderHotels()


}

function renderHotels(){

    const cardsContainer = document.getElementById("hotelCards")

    cardsContainer.innerHTML = ""

    const visibleHotels = allHotels.slice(startIndex, startIndex + visibleCards)

    visibleHotels.forEach(hotel => {

        const card = document.createElement("div")
        card.classList.add("hotel-card")

        card.innerHTML = `
        
            <img src="${hotel.imagem_url.trim()}" alt="${hotel.nome}">
            
            
            <div class="hotel-card-content">
            
                <h3>${hotel.nome}</h3>
                
                <p>${hotel.cidade}</p>
                
                <p>⭐ ${hotel.avaliacao}</p>
                
                <p>R$ ${hotel.diaria} / noite</p>
                
            </div>
        
        `

        cardsContainer.appendChild(card)

    })

    updateDots()

}

document.addEventListener("DOMContentLoaded", () => {

    loadHotels()

})
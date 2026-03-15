window.currentPage = 1
window.totalPages = 1

async function loadHotels(page = 1, search = "") {

    const data = await getHotels(page, search)

    totalPages = data.total_paginas

    const hotels = data.hoteis

    const cardsContainer = document.getElementById("hotelCards")

    cardsContainer.innerHTML = ""

    hotels.forEach(hotel => {

        const card = document.createElement("div")
        card.classList.add("hotel-card")

        card.innerHTML = `
        
            <img src="${hotel.imagem_url}" alt="${hotel.nome}">
            
            <div class="hotel-card-content">
            
                <h3>${hotel.nome}</h3>
                
                <p>${hotel.cidade}</p>
                
                <p>⭐ ${hotel.avaliacao}</p>
                
                <p>R$ ${hotel.diaria} / noite</p>
                
            </div>
        
        `

        cardsContainer.appendChild(card)

    })

}

document.addEventListener("DOMContentLoaded", () => {

    loadHotels()

})

updateDots()

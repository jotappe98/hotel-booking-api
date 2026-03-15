// carregar hotéis da API

// variáveis globais do carrossel
window.currentPage = 1
window.totalPages = 1
window.startIndex = 0
window.visibleCards = 4
window.allHotels = []

// carregar hotéis da API
async function loadHotels(page = 1, search = ""){

    const data = await getHotels(page, search)

    if(!data) return

    currentPage = data.page
    totalPages = data.total_paginas

    // adicionar novos hotéis à lista
    allHotels = [...allHotels, ...data.hoteis]

    renderHotels()

}


// renderizar hotéis
function renderHotels(){

    const cardsContainer = document.getElementById("hotelCards")

    cardsContainer.innerHTML = ""

    const visibleHotels = allHotels.slice(startIndex, startIndex + visibleCards)

    visibleHotels.forEach(hotel => {

        const card = document.createElement("div")
        card.classList.add("hotel-card")

        card.innerHTML = `
            <div class="hotel-image">

                <img src="${hotel.imagem_url}" alt="${hotel.nome}">

                <div class="favorite">❤</div>

                <button class="reserve-btn">Reservar</button>

            </div>

            <div class="hotel-card-content">
            
                <h3>${hotel.nome}</h3>
                
                <p>${hotel.cidade}</p>
                
                <p>⭐ ${hotel.avaliacao}</p>
                
                <p>R$ ${hotel.diaria} / noite</p>
                
            </div>
        `

        const favoriteBtn = card.querySelector(".favorite")

        favoriteBtn.onclick = () => {
            favoriteBtn.classList.toggle("active")
        }

        cardsContainer.appendChild(card)

    })

    updateDots()

}


// eventos
document.addEventListener("DOMContentLoaded", () => {

    document.querySelector(".arrow.left").addEventListener("click", () => {
        moveCarousel("prev")
    })

    document.querySelector(".arrow.right").addEventListener("click", () => {
        moveCarousel("next")
    })

    // carregar primeira página
    loadHotels(1)

})
//navegação entre páginas

// navegação entre páginas

window.currentPage = 1
window.totalPages = 1

window.startIndex = 0
window.visibleCards = 4
window.allHotels = []

function moveCarousel(direction){

    if(direction === "next"){

        startIndex++

        if(startIndex + visibleCards > allHotels.length && currentPage < totalPages){

            currentPage++
            loadHotels(currentPage)

        }

    }

    if(direction === "prev"){

        if(startIndex > 0){
            startIndex--
        }

    }

    renderHotels()

}
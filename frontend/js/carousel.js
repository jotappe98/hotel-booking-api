//navegação entre páginas

window.currentPage = 1
window.totalPages = 1

function moveCarousel(direction){

    if(direction === "next"){

        startIndex++

        // se precisar carregar nova página
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

document.addEventListener("DOMContentLoaded", () => {

    document.querySelector(".arrow.left").addEventListener("click", () => {

        moveCarousel("prev")

    })

    document.querySelector(".arrow.right").addEventListener("click", () => {

        moveCarousel("next")

    })

})
let currentPage = 1
let totalPages = 1


function changePage(page){

    if(page < 1 || page > totalPages){
        return
    }

    currentPage = page

    loadHotels(currentPage)

}


document.addEventListener("DOMContentLoaded", () => {

    document.querySelector(".arrow.left").addEventListener("click", () => {

        changePage(currentPage - 1)

    })

    document.querySelector(".arrow.right").addEventListener("click", () => {

        changePage(currentPage + 1)

    })

})


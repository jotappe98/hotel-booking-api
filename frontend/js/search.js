const searchInput = document.getElementById("searchInput")
const searchOverlay = document.getElementById("searchOverlay")

// ativa modo de busca
searchInput.addEventListener("focus", () => {

    document.body.classList.add("search-active")

})

// fecha ao clicar fora
searchOverlay.addEventListener("click", () => {

    document.body.classList.remove("search-active")
    searchInput.blur()

})


// busca ao pressionar ENTER
searchInput.addEventListener("keydown", function(event){

    if(event.key === "Enter"){

        const termo = searchInput.value.trim()

        startIndex = 0
        currentPage = 1
        allHotels = []

        loadHotels(1, termo)

    }

})


// se apagar o texto, mostrar todos novamente
searchInput.addEventListener("input", function(){

    const termo = searchInput.value.trim()

    if(termo === ""){

        startIndex = 0
        currentPage = 1
        allHotels = []

        loadHotels(1)

    }

})


























/*const searchInput = document.getElementById("searchInput")
const searchOverlay = document.getElementById("searchOverlay")

// ativa modo de busca
searchInput.addEventListener("focus", () => {

    document.body.classList.add("search-active")

})

// fecha ao clicar fora
searchOverlay.addEventListener("click", () => {

    document.body.classList.remove("search-active")
    searchInput.blur()

})


// busca ao pressionar ENTER
searchInput.addEventListener("keydown", function(event){

    if(event.key === "Enter"){

        const termo = searchInput.value.trim()

        startIndex = 0
        currentPage = 1
        allHotels = []

        loadHotels(1, termo)

    }

})

*/


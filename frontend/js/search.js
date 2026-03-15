const searchInput = document.getElementById("searchInput")
const searchOverlay = document.getElementById("searchOverlay")

searchInput.addEventListener("focus", () => {

    document.body.classList.add("search-active")

})

searchOverlay.addEventListener("click", () => {

    document.body.classList.remove("search-active")

    searchInput.blur()

})
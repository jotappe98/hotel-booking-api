function updateDots(){

    const dotsContainer = document.getElementById("dots")

    dotsContainer.innerHTML = ""

    for(let i = 1; i <= totalPages; i++){

        const dot = document.createElement("span")

        if(i === currentPage){
            dot.classList.add("active")
        }

        dot.addEventListener("click", () => {

            changePage(i)

        })

        dotsContainer.appendChild(dot)

    }

}

const images = ['population-total', 'co2-emission', 'co2-per-capita', 'gdp-per-capita', 'renewable-energy', 'gdp']

function setCountry(column) {
    const form = document.forms[`columnForm-${column}`]
    const country = form.country.value

    images.map((name) => {
        const url = `http://localhost:5000/${name}?country=${country}`
        document.querySelector(`#${name}-container-${column}`).src = url
    })
}

function toggleImages(endpoint) {
    const images = document.querySelectorAll(`img.${endpoint}`)
    images.forEach((elem) => {
        const currentState = elem.style.display
        if (currentState === 'none') {
            elem.style.display = 'block'
        } else {
            elem.style.display = 'none'
        }
    })
}






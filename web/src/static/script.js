const images = ['population-total','co2-emission','co2-per-capita','gdp-per-capita','renewable-energy','gdp']

const setCountry = (column) => {
    const form = document.forms[`columnForm-${column}`]
    const country = form.country.value

    images.map((name) => {
        const url = `http://localhost:5000/${name}?country=${country}`
        document.querySelector(`#${name}-container-${column}`).src = url
    })
}


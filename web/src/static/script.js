const images = ['population-total','co2-emission']

const setCountry = () => {
    const form = document.forms['mainForm']
    const country = form.country.value

    images.map((name) => {
        const url = `http://localhost:5000/${name}?country=${country}`
        document.querySelector(`#${name}-container`).src = url
    })
    console.log(url)


}




const setCountry = () => {
    const form = document.forms['mainForm']
    const country = form.country.value
    const url = `http://localhost:5000/population-total?country=${country}`
    document.querySelector('#image-container').src = url
    console.log(url)
}


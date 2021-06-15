window.onload = () => {
    const url = "http://localhost:5000/population-total?country=Germany";
    let myImage = new Image();
    myImage.src = url
    document.body.appendChild(myImage);
    // your JS here
}


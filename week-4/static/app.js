const squareBtn = document.getElementById('square-btn')
squareBtn.addEventListener('click', ()=>{
    let number = document.getElementById('num').value
    if (number) {
        squareBtn.setAttribute('href', `/square/${number}`)
    }
})

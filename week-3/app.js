let src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
fetch(src).then((response)=> {
    return response.json();
}).then((result)=> {

    const attractions = result.result.results  // attractions array
    const fragment = document.createDocumentFragment(); 
    let productItemArr = []  // for product-item div
    
    for (let i=0; i<attractions.length; i++){
        const div = document.createElement('div');
        const img = document.createElement('img');
        const h3 = document.createElement('h3');
        img.src = 'http' + attractions[i].file.split('http')[1];
        h3.textContent = attractions[i].stitle;

        if (i<2) { // promotion section
            div.className = 'promotion-item';
            div.appendChild(img);
            div.appendChild(h3);
            fragment.appendChild(div);
            document.querySelector('.promotion').appendChild(fragment);
        } else { // product section
            div.className = 'product-item';
            div.appendChild(img);
            div.appendChild(h3);
            productItemArr.push(div)
            
            // every 4 product-item div append to one wrap div
            if ((i-1) % 4 === 0 && (i-1) > 0) {
                let wrapDiv = div.cloneNode()
                wrapDiv.className = 'wrap'
                productItemArr.forEach(element => wrapDiv.appendChild(element))
                productItemArr = []  // reset arrary
                fragment.appendChild(wrapDiv)
            };
            document.querySelector('.product').appendChild(fragment)
        };
    }

    // load more button event
    let currentWrap = 2;
    loadMoreBtn().onclick = () => {
        let wraps = [... document.getElementsByClassName('wrap')];
        for (let i=currentWrap; i < currentWrap + 2; i++) {
            wraps[i].style.display = 'flex';
        };
        currentWrap += 2
        if (currentWrap >= wraps.length){ // hide the button once reach to the end
            document.getElementById('load-more').style.display = 'none'; // if call loadMoreBtn will create another button so use getElementById
        }
    }
});

// create a load-more button
function loadMoreBtn (){
    const button = document.createElement('div')
    button.id = 'load-more'
    button.textContent = 'Load More'
    return document.querySelector('.container').appendChild(button)
}




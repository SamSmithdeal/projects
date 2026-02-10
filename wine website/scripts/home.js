
document.addEventListener("DOMContentLoaded", async()=>{
    const resp = await fetch("https://api.sampleapis.com/wines/reds");
    const data = await resp.json();
    console.log(data);
    displayWines(data);
});

const clickWines = document.getElementById("wines");
var winesOfTheDay = [];

for(let x = 0; x< clickWines.children.length;x++){
    clickWines.children[x].addEventListener("click", (ev)=>{
        localStorage.setItem("wine", JSON.stringify(winesOfTheDay[x]));
        winesOfTheDay = [];
        window.location.href = 'html/Wine-Information.html';
    });
}

function displayWines(data){
    var wine = document.getElementById("wines").children;
    for(var index of wine){
        var randomWine = Math.floor(Math.random() * (501));
        var image = data[randomWine].image;
        while(!image.includes("png")){
            randomWine = Math.floor(Math.random() * (501));
            image = data[randomWine].image;
        }
        index.querySelector("img").src=image;
        index.querySelector("span").textContent=data[randomWine].wine;
        getImage(data[randomWine].winery, data[randomWine].wine, index);
        winesOfTheDay.push(data[randomWine]);
    }
}

async function getImage(location,defaultReq, wine){
    const resp = await fetch(`https://api.unsplash.com/search/photos?client_id=fwyvNADkZzDAp_uqmHJIS0tel00tROQ5iQ50VOaiKJk&query=${defaultReq}`);
    var data = await resp.json();
    var picture = data.results[0];
    wine.style.backgroundImage=`url(${data.results[0].urls.small})`;
}
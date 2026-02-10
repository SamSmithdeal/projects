window.addEventListener("load", async()=>{
    fetchWines("reds");
});

async function fetchWines(typeOfWine){
    document.getElementById("results").innerHTML="";
    var response = await fetch(`https://api.sampleapis.com/wines/${typeOfWine}`);
    var data = await response.json();
    loadWineData(data);
}

const wineSelect = document.getElementById("type");
var winesOfTheDay = []; //used for click event on every wine

wineSelect.addEventListener("change", (event)=>{
    fetchWines(event.target.value);
});

function loadWineData(data){
    let template = document.getElementById("wine-template");

    for(var x =0;x<data.length;x++){
        let currWine = data[x];
        let temp = template.content.cloneNode(true);
        let wineImage = temp.querySelector("img");
        let wineName = temp.querySelector(".wineName");
        let winery = temp.querySelector(".winery");
        let location = temp.querySelector(".location");
        let rating = temp.querySelector(".rating");

        wineName.textContent = `Name: ${currWine.wine}`;
        winery.textContent = `Winery: ${currWine.winery}`;
        location.textContent = `Location: ${currWine.location}`;
        rating.textContent = `Rating: ${currWine.rating["average"]}`;
        if(currWine.image.includes("jpg") ||currWine.image.includes("svg")){
            continue;
        }else{
            wineImage.src=currWine.image;
            winesOfTheDay.push(data[x]);
        }
        document.getElementById("results").appendChild(temp);
        
    }
    const clickWines = document.getElementById("results");

for(let x = 0; x< clickWines.children.length;x++){
    clickWines.children[x].addEventListener("click", (ev)=>{
        localStorage.setItem("wine", JSON.stringify(winesOfTheDay[x]));
        console.log(winesOfTheDay[x]);
        winesOfTheDay = [];
        window.location.href = 'Wine-Information.html';
    });
}
}

//wine search
var searchBar = document.getElementById("name-input");
searchBar.addEventListener("input", (event)=>{
    var values = event.target.value;
    var lowerCaseValues = values.toLowerCase();
    var results = document.getElementById("results");
    for (let x = results.children.length - 1; x >= 0; x--){
        let curr = results.children[x];
        let secondElement = curr.children[1];
        let thirdElement = secondElement.children[0];
        var lower = secondElement.textContent.toLowerCase();
        if (!lower.includes(lowerCaseValues)) {
            curr.style.display = "none";
          }
          if(curr.style.display = "none" && lower.includes(lowerCaseValues)){
            curr.style.display = "flex";
          }
    }
});
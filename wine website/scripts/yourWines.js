
//used to delete all wine data
document.getElementById("delete").addEventListener("click", function(){
    var table = document.querySelectorAll("table");
    table.forEach(table =>{
        table.remove();
    });
    localStorage.setItem("wines", JSON.stringify([]));
        
});
//used to download your wines
var download = document.getElementById("download");

download.addEventListener("click", function(){
    var items = localStorage.getItem("wines");
    const state = { items: items ? JSON.parse(items) : []};
    let blob = new Blob([JSON.stringify(state)],{
        type: 'application/txt'
    });
    let link = document.createElement("a");
    link.download = "wine-data.txt";
    link.href = URL.createObjectURL(blob);
    link.click();
});

window.addEventListener("load", ()=>{
    var wines = JSON.parse(localStorage.getItem("wines"));
    console.log(wines);
    let template = document.querySelector("#your-wine-template");
    for(let x =0;x<wines.length;x++){
        let wine = wines[x];
        let wineView = template.content.cloneNode(true);

        let del = wineView.querySelector("button");
        del.addEventListener("click", () =>{
            wines.splice(x,1);
            localStorage.setItem("wines",JSON.stringify(wines));
            window.location.reload();
            console.log(localStorage)
        });

        let name = wineView.querySelector(".name");
        let sweetness = wineView.querySelector(".sweetness");
        let location = wineView.querySelector(".location");
        let vintage = wineView.querySelector(".vintage");
        let alc = wineView.querySelector(".alc");
        let rating = wineView.querySelector(".rating");
        let notes = wineView.querySelector(".notes");
    
        name.textContent=wine.name;
        sweetness.textContent=wine.sweetness;
        location.textContent=wine.location;
        vintage.textContent=wine.vintage;
        alc.textContent=wine.alc;
        rating.textContent=wine.rating;
        notes.textContent=wine.notes;

        function updateWine(){
            wine.name = name.textContent;
            wine.sweetness = sweetness.textContent;
            wine.location = location.textContent;
            wine.vintage = vintage.textContent;
            wine.alc = alc.textContent;
            wine.rating = rating.textContent;
            wine.notes = notes.textContent;
            localStorage.setItem("wines",JSON.stringify(wines));
        }

        name.addEventListener("input", updateWine);
        sweetness.addEventListener("input", updateWine);
        location.addEventListener("input", updateWine);
        vintage.addEventListener("input", updateWine);
        alc.addEventListener("input", updateWine);
        rating.addEventListener("input", updateWine);
        notes.addEventListener("input", updateWine);
        
        switch(wine.type){
            case "Red":
                document.querySelector("#reds").appendChild(wineView);
            case "White":
                document.querySelector("#whites").appendChild(wineView);
            case "Dessert":
                document.querySelector("#desserts").appendChild(wineView);
            case "Sparkling":
                document.querySelector("#sparkling").appendChild(wineView);
            case "Port":
                document.querySelector("#ports").appendChild(wineView);
        }
    }

});
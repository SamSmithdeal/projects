function populate() {
    const wineInfoStored = localStorage.getItem("wine");
    const wineInfo = JSON.parse(wineInfoStored);
    console.log("wineInfo: " , wineInfo);
    let name = document.getElementById("nameHeader");
    console.log(name);
    name.textContent = wineInfo.wine;
    let displayImg = document.getElementById("wine-img");
    displayImg.src = wineInfo["image"];
    let wineryDisplay = document.getElementById("winery-display");
    wineryDisplay.textContent = "Winery: " + wineInfo['winery'];
    let whereDisplay = document.getElementById("where-display");
    whereDisplay.textContent = "Where it Was Made: " + wineInfo["location"];
    let ratingDisplay = document.getElementById("pubRating-display");
    ratingDisplay.textContent = "Public Rating of " + wineInfo["rating"]["average"] + " with " + wineInfo["rating"]["reviews"];
}

populate() ;

function addWine(){
    window.location.href = 'New-Wine-Form.html';
}
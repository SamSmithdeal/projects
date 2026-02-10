
window.addEventListener("load", ()=>{
  var wine = localStorage.getItem("wine");
  if(!wine){
    return;
  }
  var data = JSON.parse(wine);
  console.log(data);
  document.getElementById("wine-name").value = data.wine;
  document.getElementById("region").value = data.location;
  document.getElementById("winery").value = data.winery;
});

function saveWine(event) {
    event.preventDefault(); // Prevent form submission

    const name = document.getElementById("wine-name").value;
    const sweetness = document.getElementById("myRange").value;
    const alc = document.getElementById("alc").value;
    const vintage = document.getElementById("vintage").value;
    const region = document.getElementById("region").value;
    const winery = document.getElementById("winery").value;
    const rating = document.querySelector('input[name="rating"]:checked').value;
    const notes = document.getElementById("notes").value;
    const type = document.querySelector('input[name="type-of-wine"]:checked').value;

    if (!name || !alc || !vintage || !region || !winery || !type) {
      alert("Please fill out all fields.");
      return;
    }

    const wine = {name: name, sweetness: sweetness, alc: alc, vintage: vintage, type: type, location: region, rating: rating, notes: notes};

    // Retrieve current wine list from local storage or initialize an empty array
    var wineList = JSON.parse(localStorage.getItem("wines"));
    if(!wineList){
        wineList = [];
    }
    wineList.push(wine);

    localStorage.setItem("wines", JSON.stringify(wineList)); // Save updated wine list to local storage

   console.log(JSON.parse(localStorage.getItem("wines")));
    document.querySelector("form").reset(); // Reset form
}

        // Nav Bar Funcionality - Thanks Sam !
        function toggleMenu() {
            const mobileMenu = document.getElementById("menu-items");
            if(mobileMenu.style.display == "block"){
              mobileMenu.style.display = "none";
            }
            else{
              mobileMenu.style.display = "block";
            }
          }
  
          // Slider Functionality
          var slider = document.getElementById("myRange");
          var output = document.getElementById("sweet-display");
          output.innerHTML = slider.value;
  
        slider.oninput = function() {
        output.innerHTML = this.value;
        }
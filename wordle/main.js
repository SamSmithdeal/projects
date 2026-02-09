var word = randomWord();
//top key div and children
var parent = document.getElementById("topKeys");
var children = parent.children;

//middle key div and children
var parent1 = document.getElementById("middleKeys");
var children1 = parent1.children;

//bottom key div and children
var parent2 = document.getElementById("bottomKeys");
var children2 = parent2.children;
var currentInput = [];      //all of the letters inputted added to array
var wordArray = [];
var checkWinArray = [];
var counter = 0;            // Keeps track of the number of letters entered by the player.
var shake = 30;             // The number of times the input elements shake on invalid input.
var squareCount = 0;
var squareCount1 = 0;
var attempts = 0;
var countTo = 5;            // The number of squares to check when the player presses "ENTER."

listen();

function listen(){
// Add a keydown event listener to the whole document
document.addEventListener("keydown", function(event) {
    var keyPressed = event.key;
    var upperCase = keyPressed.toUpperCase();
    selectedLetter(upperCase); // Call the selectedLetter function with the uppercase key.
});

// Add click event listeners for the first set of keys
for(var x = 0; x < children.length; x++){
    var child = children[x];
    child.addEventListener("click", function(){
        selectedLetter(this.id); // Call the selectedLetter function with the clicked letter's id.
    });
}

// Add click event listeners for the second set of keys
for(var x = 0; x < children1.length; x++){
    var child1 = children1[x];
    child1.addEventListener("click", function(){
        selectedLetter(this.id); // Call the selectedLetter function with the clicked letter's id.
    });
}

// Add click event listeners for the third set of keys
for(var x = 0; x < children2.length; x++){
    var child2 = children2[x];
    child2.addEventListener("click", function(){
        selectedLetter(this.id); // Call the selectedLetter function with the clicked letter's id.
    });
}
}

// Function to handle selected letters
function selectedLetter(letter){

    
    //BACKSPACE or BACK key press to remove the last entered letter
    if (letter === "BACK"  || (letter === "BACKSPACE" && currentInput.length > 0)) {
        currentInput.pop(); // Remove the last letter from the current input.
        var lastEnteredDiv = document.getElementById(counter - 1);
        lastEnteredDiv.innerHTML = ""; // Clear the last entered letter from the display.
        counter--; // Decrement the counter to update the input position.
        if(square % 4 == 0){
            var lastSquare = document.getElementById(squareCount - 1);
            lastSquare.style.background = "lightgray"; // Reset background color for the last square.
        }
        return; 
    }

    // ENTER key press with less than 5 letters entered
    if (letter === "ENTER" && currentInput.length < 5) {
        var shakeCount = 0;
        // Apply a shaking animation to the input elements
        while (shakeCount <= shake) {
            const shakeElement = document.getElementById(shakeCount);
            
            // Add the animation class to initiate the animation
            shakeElement.classList.add("shake-animation");
            
            // Remove the animation class after 0.5 seconds to stop the animation
            setTimeout(() => {
                shakeElement.classList.remove("shake-animation");
            }, 200);
            
            shakeCount += 1;
        }
    }
    
    // Handle valid letter input (A-Z) with a max of letters
    else if(currentInput.length < 5 && letter != "back" && letter != "ENTER" && /^[a-zA-Z]$/.test(letter)){
        currentInput.push(letter); // Add the entered letter to the current input array.
        checkWinArray.push(letter);
        // Place the entered letter in the HTML element corresponding to the counter.
        if(document.getElementById(counter).innerHTML == ""){
            document.getElementById(counter).innerHTML = letter;
            counter++;
        }
        else{
            document.getElementById(counter+1).innerHTML = letter;
        }
    }

    // Check for word completion when 5 letters are entered and ENTER is pressed
        var checkIfWord = currentInput.join("").toLowerCase();
        console.log(checkIfWord);
    if (currentInput.length === 5 && letter === "ENTER" && isInList(checkIfWord)) {
        attempts++;
        for(var j = 0; j < word.length; j++){
            wordArray.push(word[j]);
        }

        var count = 0;
        // Loop through each letter in the input and compare it with the target word.
        while (count < countTo) {
            console.log(checkWin);
            var square = document.getElementById(squareCount);


            for(var i = 0; i < countTo; i++){
                if(wordArray[count] === currentInput[i] && i == count){
                    if (checkWin()) {
                        setTimeout(function () {
                            winLoseScreen("You Lost");
                        }, 1000);
                    }

                    square.classList.add("flip-animation");

                    setTimeout(function() {
                      var elements = document.querySelectorAll(".flip-animation");
                    
                      elements.forEach(function(element) {
                        element.classList.remove("flip-animation");
                      });
                    }, 300);

                    square.style.background = "#6aaa64"; // Set background color to green.
                    square.style.borderColor = "#6aaa64";
                    square.style.color = "white";

                  
                    changeColor("#6aaa64", document.getElementById(currentInput[i]));

                    wordArray[count] = null;
                    currentInput[i] = null;
                    console.log(currentInput);
                }
            }


            if(squareCount === 29){
                setTimeout(function(){
                    winLoseScreen("You Win");
                },1000);

            }
            squareCount++;
            count++;
        }
        
        var count1 = 0
        while(count1 < countTo){
            var square1 = document.getElementById(squareCount1);
            for(var i =0; i <countTo; i++){
                if(wordArray[i] === currentInput[count1] && i != count1 && currentInput[count1] != null){

                    square1.classList.add("flip-animation");

                    setTimeout(function() {
                      var elements = document.querySelectorAll(".flip-animation");
                    
                      elements.forEach(function(element) {
                        element.classList.remove("flip-animation");
                      });
                    }, 300);

                    square1.style.background = "#c9b458"; // Set background color to yellow.
                    square1.style.borderColor = "#c9b458";
                    square1.style.color = "white";

                    changeColor("#c9b458",document.getElementById(currentInput[count1]));

                    
                    wordArray[i] = null;
                    currentInput[count1] = null;
                    break;
                }
                if(!wordArray.includes(currentInput[count1])){
                    square1.classList.add("flip-animation");

                    setTimeout(function() {
                      var elements = document.querySelectorAll(".flip-animation");
                    
                      elements.forEach(function(element) {
                        element.classList.remove("flip-animation");
                      });
                    }, 300);
                    
                    changeColor("#787c7e", document.getElementById(currentInput[count1]));
                    square1.style.background = "#787c7e"; // Set background color to gray for incorrect letters.
                    square1.style.borderColor = "#787c7e";
                    square1.style.color = "white";

                    break;
                }
            }
            count1++;
            squareCount1++
                        // Check if the player has lost (reached the last square without a correct word)
        }

        // Reset the input arrays and counters for the next round.
        currentInput.length = 0;
        wordArray.length = 0;
    }
}


function winLoseScreen(lose){
    var container = document.createElement("div");
    var info = document.createElement("div");
    var h11 = document.createElement("h1");
    var br = document.createElement("br");
    var h21 = document.createElement("h2");
    var button = document.createElement("button");
    button.innerHTML = "Play again";
    button.setAttribute("id", "playAgain");
    h21.innerHTML = "Attempts: " + attempts;
   

    info.setAttribute("id", "info");
    h11.innerHTML = lose;
    info.appendChild(h11);
    info.appendChild(br);
    if(lose != ""){
        var h12 = document.createElement("h1");
        h12.innerHTML = "Word: " + word;
        info.appendChild(h12);
    }
    info.appendChild(h21);
    info.appendChild(button);
    container.appendChild(info);
    container.setAttribute("id", "winLose");
    document.body.appendChild(container);
    button.addEventListener("click", function(){
        resetGame(container);
    });
}


function resetGame(containerToRemove) {
    // Remove the win/lose screen container if it exists
    if (containerToRemove) {
        document.body.removeChild(containerToRemove);
    }

    currentInput = [];
    wordArray = [];
    checkWinArray = [];
    counter = 0;
    squareCount = 0;
    squareCount1 = 0;
    attempts = 0;
    countTo = 5;
    shakeCount = 0;

    // Clear the displayed letters in the input area and reset styles
    for (var i = 0; i < 30; i++) {
        var square = document.getElementById(i);
        if (square) {
            square.innerHTML = "";
            square.style.removeProperty('background'); // Remove the background color style
            square.style.removeProperty('border-color'); // Remove the border color style
            square.style.removeProperty('color'); // Remove the text color style
        }
    }
    var top = document.getElementById("topKeys");
    for(var x = 0; x < top.children.length; x++){
     top.children[x].style.background = "#d3d3d3";
     top.children[x].style.color = "#000000";
     top.children[x].classList.remove("green");
 
    }
    var middle = document.getElementById("middleKeys");
    for(var x = 0; x < middle.children.length; x++){
     middle.children[x].style.background = "#d3d3d3";
     middle.children[x].style.color = "#000000";
     middle.children[x].classList.remove("green");
 
    }
    var bottom = document.getElementById("bottomKeys");
    for(var x = 0; x < bottom.children.length; x++){
     bottom.children[x].style.background = "#d3d3d3";
     bottom.children[x].style.color = "#000000";
     bottom.children[x].classList.remove("green");
 
    }

    // Remove any existing win/lose screen
    var winLoseScreenElement = document.getElementById("winLose");
    if (winLoseScreenElement) {
        document.body.removeChild(winLoseScreenElement);
    }
    word = randomWord();


}
function changeColor(color, div) {
    if (!div.classList.contains("green") && color == "#6aaa64") {
        div.style.background = color;
        div.style.color = "#ffffff";
        div.classList.add("green"); // Add the "green" class to mark it as green
    }
    else if(!div.classList.contains("green") && color == "#c9b458"){
        div.style.background = color;
        div.style.color = "#ffffff";
    }
    else if(!div.classList.contains("green") && color == "#787c7e"){
        div.style.background = color;
        div.style.color = "#ffffff";
    }
}
function checkWin() {
    // Convert the currentInput array into a string for comparison
    const currentInputString = currentInput.join("");
    
    // Check if the currentInput string is equal to the target word (word)
    if (currentInputString === word) {
        return true; // Player has won
    }
    
    return false; // Player has not won yet
}
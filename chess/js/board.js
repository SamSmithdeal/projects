
export function createBoard(){
    var board = document.getElementById("board");
for (let x = 1; x <= 64; x++) {
    var square = document.createElement("div");
    square.setAttribute("id", x);
    square.setAttribute("class", "square");
  
    // Calculate the row and column to determine the square color
    var column = (x - 1) % 8;
    var row = Math.floor((x - 1) / 8);
  
  //applies color based on square
    if ((row + column) % 2 === 0) {
      square.style.backgroundColor = '#212161';
    } else {
      square.style.backgroundColor = '#adadad';
    }
    board.appendChild(square);
  }
}

//object for each square
class location {
    constructor(piece, id, locationNum, color,inCheck){
        this.piece = piece;
        this.id = id;
        this.locationNum = locationNum;
        this.color = color;
        this.inCheck = inCheck;
    }
}

var locationLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
var locationNumbers = [1,2,3,4,5,6,7,8];
var numIndex = 0;
var arrayIndex=0;

export function createLocation(x){
    var piece;
    var locationNum;
    var color;

    if(locationLetters[arrayIndex]=='A'){
        color = "black";
        switch(numIndex){
            case 0: piece = "rook"
            break;
            case 1: piece = "knight"
            break;
            case 2: piece = "bishop"
            break;
            case 3: piece = "king"
            break;
            case 4: piece = "queen"
            break;
            case 5: piece = "bishop"
            break;
            case 6: piece = "knight"
            break;
            case 7: piece = "rook"
            break;
        }
    }
    if(locationLetters[arrayIndex]=='B'){
        piece = "pawn";
        color = "black"
    }
    if(locationLetters[arrayIndex]=='H'){
        color = "white";
        switch(numIndex){
            case 0: piece = "rook"
            break;
            case 1: piece = "knight"
            break;
            case 2: piece = "bishop"
            break;
            case 3: piece = "king";
            break;
            case 4: piece = "queen"
            break;
            case 5: piece = "bishop"
            break;
            case 6: piece = "knight"
            break;
            case 7: piece = "rook"
            break;
        }
    }
    if(locationLetters[arrayIndex]=='G'){
        piece = "pawn";
        color = "white"
    }
    locationNum = locationLetters[arrayIndex] + locationNumbers[numIndex];
    numIndex++;

    if(numIndex==8){
        numIndex=0;
        arrayIndex++;
    }
    return new location(piece, x, locationNum, color,false);
}
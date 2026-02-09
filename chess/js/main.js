
import { createBoard, createLocation} from "./board.js";
import {possibleMoves, arrayOfSquares} from "./validMoves.js";
createBoard();
picsAndLocations();
var currentTurn = "white";
//function to add images and initialize board
function picsAndLocations(){
    //add each square to the location array
    var count = 1;
    for(let x = 0;x<8;x++){
        for(let i = 1;i<9;i++){
            arrayOfSquares[x].push(createLocation(count));
            count++;
        }
    }

    for(var x of arrayOfSquares[0]){
        var picName = `${x.color}_${x.piece}.png`;
        var image = document.createElement("img");
        image.src="../chesspieces/"+picName;
        document.getElementById(x.id).appendChild(image);
    }
    for(var x of arrayOfSquares[1]){
        var picName = `${x.color}_${x.piece}.png`;
        var image = document.createElement("img");
        image.src="../chesspieces/"+picName;
        document.getElementById(x.id).appendChild(image);
    }

    for(var x of arrayOfSquares[7]){
        var picName = `${x.color}_${x.piece}.png`;
        var image = document.createElement("img");
        image.src="../chesspieces/"+picName;
        document.getElementById(x.id).appendChild(image);
    }
    for(var x of arrayOfSquares[6]){
        var picName = `${x.color}_${x.piece}.png`;
        var image = document.createElement("img");
        image.src="../chesspieces/"+picName;
        document.getElementById(x.id).appendChild(image);
    }
}

// ///////////////////////////main code
//var to remove glow on possible spots each click
var removeGlow = [];
var pieceInfo;
var board = document.getElementById("board");

//click event for all the pieces
board.addEventListener("click", e =>{
    //if glowing spot it clicked then move the piece to that square
    if(e.target.classList.contains("glow")||e.target.parentElement.classList.contains("glow")){
        if(e.target.tagName.toLowerCase()==="img"){
            //if image square is clicked
            movePiece(pieceInfo,e.target.parentElement);
        }
        else{
            //if open square is clicked
            movePiece(pieceInfo,e.target);
        }
    }

    else{
        for(var x of removeGlow){
            document.getElementById(x).classList.remove("glow");
        }
var selectedPiece = e.target.parentElement;

// Find piece object
for(var x=0;x<8;x++){
    for(var i=0;i<8;i++){
        if(arrayOfSquares[x][i].id == selectedPiece.id){
            // Only allow selecting pieces of the current turn color
            if(arrayOfSquares[x][i].color !== currentTurn) return;

            pieceInfo = arrayOfSquares[x][i];
            var validMove = possibleMoves(pieceInfo);
            removeGlow = validMove;
            lightUpLocations(validMove);
            incheck(validMove);
        }
    }
}

    }

});
function incheck(validMoves){
    validMoves.forEach(element => {
        if(arrayOfSquares.forEach(obj => obj.id===element)){
            alert("hi")
        }

    });
    console.log(arrayOfSquares)
    console.log(validMoves)
}

//lights up valid spots
function lightUpLocations(spaces){
    for(var x of spaces){
        document.getElementById(x).classList.add("glow");
        console.log(document.getElementById(x))
    }
}

function movePiece(piece, newLocation){
    newLocation.innerHTML='';
    for(var x of removeGlow){
        document.getElementById(x).classList.remove("glow");
    }
    var img = document.getElementById(piece.id).firstChild;
    newLocation.appendChild(img);

    for(var x=0;x<8;x++){
        for(var i=0;i<8;i++){
            //finds selected piece on the board
            if(arrayOfSquares[x][i].id == newLocation.id){
                arrayOfSquares[x][i].color = piece.color;
                arrayOfSquares[x][i].piece = piece.piece;
                document.getElementById("moves").innerHTML+=piece.piece + " "+ arrayOfSquares[x][i].locationNum+"<br>";
            }
        }
       }
       piece.color = null;
       piece.piece = null;
    currentTurn = currentTurn === "white" ? "black" : "white";
}


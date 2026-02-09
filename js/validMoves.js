
var whiteDangerZone =[];
var blackDangerZone =[];
export function possibleMoves(piece){
    switch(piece.piece){
        case "pawn": 
            if(piece.color=="white"){
                return whitePawn(piece);
            }
            else{
                return blackPawn(piece);
            }
        case "knight": return knight(piece);
        case "bishop": return bishopRookQueen(piece);
        case "rook": return bishopRookQueen(piece);
        case "queen": return bishopRookQueen(piece);
        case "king": return king(piece);
    }
}
export var arrayOfSquares = [[],[],[],[],[],[],[],[]];
function blackPawn(piece){
    var possibleSpots = [];
    //move forward two on the first move only
    if(piece.locationNum.includes('B')){
        possibleSpots.push(piece.id+8);
        possibleSpots.push(piece.id+16);
    }
    else{
        possibleSpots.push(piece.id+8);
    }

    //if spot in front of pawn has piece
    for(var x =0;x<8;x++){
        for(var i =0;i<8;i++){
            if(arrayOfSquares[x][i].piece){
                if (possibleSpots.includes(arrayOfSquares[x][i].id)) {
                    const index = possibleSpots.indexOf(arrayOfSquares[x][i].id);
                    if (index !== -1) {
                        possibleSpots.splice(index, 1); // Removes the element at the found index
                    }
                }

                whiteDangerZone.push(piece.id + 7);
                whiteDangerZone.push(piece.id + 9);
                //adds diagonal attacks for the pawns
                if(piece.id + 7 == arrayOfSquares[x][i].id && arrayOfSquares[x][i].color!='black'){
               
                    possibleSpots.push(piece.id + 7);
                }
                if(piece.id + 9 == arrayOfSquares[x][i].id && arrayOfSquares[x][i].color!='black'){
                    
                     possibleSpots.push(piece.id + 9);
                    
                }
            }
        }
    }

    return possibleSpots;
}

function whitePawn(piece){
    var possibleSpots = [];
    //move forward two on the first move only
    if(piece.locationNum.includes('G')){
        possibleSpots.push(piece.id-8);
        possibleSpots.push(piece.id-16);
    }
    else{
        possibleSpots.push(piece.id-8);
    }

    //if spot in front of pawn has piece
    for(var x =0;x<8;x++){
        for(var i =0;i<8;i++){
            if(arrayOfSquares[x][i].piece){
                if (possibleSpots.includes(arrayOfSquares[x][i].id)) {
                    const index = possibleSpots.indexOf(arrayOfSquares[x][i].id);
                    if (index !== -1) {
                        possibleSpots.splice(index, 1); // Removes the element at the found index
                    }
                }

                blackDangerZone.push(piece.id - 7);
                blackDangerZone.push(piece.id - 9);
                //adds diagonal attacks for the pawns
                if(piece.id - 7 == arrayOfSquares[x][i].id &&arrayOfSquares[x][i].color!='white'){
                    possibleSpots.push(piece.id - 7);
                }
                if(piece.id - 9 == arrayOfSquares[x][i].id&&arrayOfSquares[x][i].color!='white'){
                    possibleSpots.push(piece.id - 9);
                }
            }
        }
    }

    return possibleSpots;
}
function knight(piece){
    var possibleSpots = [];
    var letter = piece.locationNum[0];
    var num = piece.locationNum[1];
    for(var x = 0;x<8;x++){
        for(var i = 0;i<8;i++){
            
            //valid spots logic
            if(arrayOfSquares[x][i].locationNum[0]==String.fromCharCode(letter.charCodeAt(0) -2)){
                if(arrayOfSquares[x][i].locationNum[1] == Number(num)+1 || arrayOfSquares[x][i].locationNum[1] == num-1){
                    possibleSpots.push(arrayOfSquares[x][i].id);
                
                }
            }
            if(arrayOfSquares[x][i].locationNum[0]==String.fromCharCode(letter.charCodeAt(0) +2)){
                if(arrayOfSquares[x][i].locationNum[1] == Number(num)+1 || arrayOfSquares[x][i].locationNum[1] == num-1){
                    possibleSpots.push(arrayOfSquares[x][i].id);
                }
            }
            if(arrayOfSquares[x][i].locationNum[0]==String.fromCharCode(letter.charCodeAt(0) -1)){
                if(arrayOfSquares[x][i].locationNum[1] == Number(num)+2 || arrayOfSquares[x][i].locationNum[1] == num-2){
                    possibleSpots.push(arrayOfSquares[x][i].id);
                }
            }
            if(arrayOfSquares[x][i].locationNum[0]==String.fromCharCode(letter.charCodeAt(0) +1)){
                if(arrayOfSquares[x][i].locationNum[1] == Number(num)+2 || arrayOfSquares[x][i].locationNum[1] == num-2){
                    possibleSpots.push(arrayOfSquares[x][i].id);
                }
            }
            
        }
    }
    //removes locations in possible spots that have other pieces of the same color
    for(var x = 0;x<8;x++){
        for(var i = 0;i<8;i++){
            if(arrayOfSquares[x][i].piece){
                if(piece.color==arrayOfSquares[x][i].color && possibleSpots.includes(arrayOfSquares[x][i].id)){
                    const index = possibleSpots.indexOf(arrayOfSquares[x][i].id);
                    if (index !== -1) {
                        possibleSpots.splice(index, 1); // Removes the element at the found index
                    }
                }
            }
        }}
    return possibleSpots;
}


function bishopRookQueen(piece){

    var possibleSpots = [];
    var letterSpots = [];
    var letter = piece.locationNum[0].charCodeAt(0);
    var num = piece.locationNum[1];
    if(piece.piece == "bishop"){
        letterSpots=helperBishop(letter,num,letterSpots, piece);
    }
    if(piece.piece == "rook"){
        letterSpots=helperRook(letter,num,letterSpots, piece);
    }
    if(piece.piece == "queen"){
        var placeHoldArr = helperBishop(letter,num,letterSpots, piece);
        letterSpots = placeHoldArr.concat(helperRook(letter,num,letterSpots, piece));
    }
    console.log(letterSpots)
    for(var x = 0;x<8;x++){
        for(var i= 0;i<8;i++){
            //add possible locations
            if(letterSpots.includes(arrayOfSquares[x][i].locationNum)){
                possibleSpots.push(arrayOfSquares[x][i].id);
                if(arrayOfSquares[x][i].piece){
                    if(piece.color == arrayOfSquares[x][i].color){
                        var index = possibleSpots.indexOf(arrayOfSquares[x][i].id);
                        possibleSpots.splice(index);
                    }
                }
            }


    
        }
    }
    return possibleSpots;
}

function helperBishop(letter, num, spots, piece) {
    var letterCount = letter;
    var numCount = Number(num);

    // Directions: top-left, top-right, bottom-left, bottom-right
    var directions = [
        [-1, -1], // top-left
        [-1, 1],  // top-right
        [1, -1],  // bottom-left
        [1, 1]    // bottom-right
    ];

    // Loop through each direction
    for (var dir of directions) {
        let l = letterCount;
        let n = numCount;
        var stop = false;

        // Move in the current direction until reaching the board limits
        while (l >= 65 && l <= 72 && n >= 1 && n <= 8) {
            l += dir[0]; // Move letter (A-H)
            n += dir[1]; // Move number (1-8)
            for(var x =0;x<8;x++){
                for(var i=0;i<8;i++){
                    if(arrayOfSquares[x][i].locationNum == String.fromCharCode(l)+n){
                        if(arrayOfSquares[x][i].piece){
                            if(arrayOfSquares[x][i].color==piece.color){
                                stop = true;
                                if(arrayOfSquares[x][i].color=="black"){
                                    whiteDangerZone.push(arrayOfSquares[x][i].id);
                                }
                                else{
                                    blackDangerZone.push(arrayOfSquares[x][i].id);
                                }
                            }
                            else if(arrayOfSquares[x][i].color!=piece.color && arrayOfSquares[x][i].piece != "king"){
                                stop = true;
                            }
                        }
                    }
                }
            }
            
            // Check if we are still on the board
            if (l >= 65 && l <= 72 && n >= 1 && n <= 8) {
                spots.push(String.fromCharCode(l) + n);
            }
            if(stop){
                break;
            }
        }
    }

    return spots;
}

function helperRook(letter, num, spots, piece){
    var letterCount = letter;
    var numCount = Number(num);

    // Directions: top-left, top-right, bottom-left, bottom-right
    var directions = [
        [-1, 0], // top-left
        [1, 0],  // top-right
        [0, 1],  // bottom-left
        [0, -1]    // bottom-right
    ];

    // Loop through each direction
    for (var dir of directions) {
        let l = letterCount;
        let n = numCount;
        var stop = false;

        // Move in the current direction until reaching the board limits
        while (l >= 65 && l <= 72 && n >= 1 && n <= 8) {
            l += dir[0]; // Move letter (A-H)
            n += dir[1]; // Move number (1-8)
            for(var x =0;x<8;x++){
                for(var i=0;i<8;i++){
                    if(arrayOfSquares[x][i].locationNum == String.fromCharCode(l)+n){
                        if(arrayOfSquares[x][i].piece){
                            if(arrayOfSquares[x][i].color==piece.color){
                                stop = true;
                                if(arrayOfSquares[x][i].color=="black"){
                                    whiteDangerZone.push(arrayOfSquares[x][i].id);
                                }
                                else{
                                    blackDangerZone.push(arrayOfSquares[x][i].id);
                                }
                            }
                            else if(arrayOfSquares[x][i].color!=piece.color &&arrayOfSquares[x][i].piece != "king"){
                                stop = true;
                            }
                        }
                    }
                }
            }
            
            // Check if we are still on the board
            if (l >= 65 && l <= 72 && n >= 1 && n <= 8) {
                spots.push(String.fromCharCode(l) + n);
            }
            if(stop){
                break;
            }
        }
    }

    return spots;
}

function king(piece){
        whiteDangerZone=[];
    blackDangerZone=[];
    var possibleSpots = [];
    var nonValidSpots = [];
    var letter = piece.locationNum[0].charCodeAt(0);
    var num = Number(piece.locationNum[1]);
    var directions = [
        [1,0],[1,1],[1,-1],[0,1],[0,-1],[-1,-1],[-1,0],[-1,1]
    ];

    for(var x of directions){
        for(var i=0;i<8;i++){
            for(var j =0;j<8;j++){


                if(arrayOfSquares[i][j].locationNum == String.fromCharCode(letter-x[0])+(num-x[1])){
                    if(arrayOfSquares[i][j].color == piece.color){
                        continue;
                    }
                    else{
                        possibleSpots.push(arrayOfSquares[i][j].id)
                    }
                }
            }
        }
    }
    var uniqueArr1;
    for(var i=0;i<8;i++){
        for(var j =0;j<8;j++){
            if(arrayOfSquares[i][j].color != piece.color){

                //king cant go into enemy path
                if(arrayOfSquares[i][j].piece == "bishop"){
                    nonValidSpots.push.apply(nonValidSpots,bishopRookQueen(arrayOfSquares[i][j]));
                }
                if(arrayOfSquares[i][j].piece == "rook"){
                    nonValidSpots.push.apply(nonValidSpots,bishopRookQueen(arrayOfSquares[i][j]));
                }
                if(arrayOfSquares[i][j].piece == "queen"){
                    nonValidSpots.push.apply(nonValidSpots,bishopRookQueen(arrayOfSquares[i][j]));
                }
                if(arrayOfSquares[i][j].piece == "knight"){
                    nonValidSpots.push.apply(nonValidSpots,knight(arrayOfSquares[i][j]));
                }
                if(arrayOfSquares[i][j].piece == "pawn" &&piece.color=='white'){
                    blackPawn(arrayOfSquares[i][j]);
                }
                if(arrayOfSquares[i][j].piece == "pawn" &&piece.color=='black'){
                    whitePawn(arrayOfSquares[i][j]);
                }
                if(piece.color=="white"){
                nonValidSpots.push.apply(nonValidSpots,whiteDangerZone);
            }else{
                nonValidSpots.push.apply(nonValidSpots,blackDangerZone);
            }

                const set2 = new Set(nonValidSpots);

                uniqueArr1 = possibleSpots.filter(item => !set2.has(item));
            }
        }}
    return uniqueArr1

}
'use strict';

var directions = [ 'north', 'northeast', 'east', 'southeast', 'south', 'southwest', 'west', 'northwest' ];
var words = [ 'laraine', 'kindergarten', 'gingerbreadman', 'investigation', 'magnifyingglass', 'flight', 'detective', 'klawn', 'adddetail', 'doyourbestwork', 'choice', 'mysteryreader', 'circletime', 'davinci', 'monalisa', 'postoffice', 'postmaster', 'sandbox', 'garden', 'joeyarea', 'snacktime', 'morningmeeting', 'schedule', 'readingtime', 'clues', 'curiosity', 'resilience', 'pioneer' ];

var puzzle = [
    [ 'c', 'd', 'v', 'i', 'w', 'l', 'v', 'j', 'b', 'w', 'p', 'd', 'c', 'g', 'x', 'g', 'n', 'i', 't', 'e', 'e', 'm', 'g', 'n', 'i', 'n', 'r', 'o', 'm', 'w' ],
    [ 'i', 'a', 'y', 'f', 'y', 'v', 'f', 't', 'q', 'f', 'w', 'y', 'u', 'e', 'm', 'i', 'n', 'a', 'c', 'u', 'i', 'v', 's', 'h', 'n', 'j', 's', 'l', 'y', 'p' ],
    [ 'f', 'v', 'v', 'l', 'u', 'i', 'x', 'q', 'r', 'd', 'e', 'k', 'r', 's', 'r', 'j', 't', 'a', 's', 'p', 'p', 'g', 'i', 'l', 'w', 'h', 'm', 'o', 'z', 'o' ],
    [ 'd', 'i', 'c', 'k', 'g', 'w', 'n', 'u', 't', 'h', 'v', 'q', 'i', 'd', 'z', 'f', 'z', 'z', 'k', 'h', 'w', 'k', 'i', 'l', 'a', 'w', 'o', 'k', 'l', 's' ],
    [ 'z', 'n', 't', 'j', 'm', 'e', 'v', 'm', 'u', 'e', 'p', 'x', 'o', 'g', 'b', 'f', 'o', 's', 'g', 'x', 'u', 'f', 'd', 'j', 'l', 's', 'a', 's', 'g', 't' ],
    [ 't', 'c', 'p', 'g', 'd', 'y', 'c', 'k', 's', 'w', 'b', 'j', 's', 'j', 'f', 'm', 'r', 's', 'z', 'b', 'o', 'i', 's', 'f', 'k', 'y', 'r', 'u', 'r', 'o' ],
    [ 'g', 'i', 'd', 'r', 'v', 'y', 'x', 'e', 'a', 'a', 's', 'a', 'i', 'k', 'r', 'o', 'w', 't', 's', 'e', 'b', 'r', 'u', 'o', 'y', 'o', 'd', 'q', 'n', 'f' ],
    [ 'e', 'r', 'a', 'a', 'p', 'm', 'l', 'u', 'k', 'q', 'd', 'y', 't', 'r', 'p', 'n', 'n', 'n', 'e', 'l', 'u', 'd', 'e', 'h', 'c', 's', 't', 'o', 'g', 'f' ],
    [ 't', 'g', 'a', 'l', 'b', 'a', 'd', 'w', 'x', 'd', 'e', 'h', 'y', 'u', 'n', 'y', 'e', 'n', 't', 'm', 'c', 'n', 'p', 'h', 'u', 'h', 'j', 'k', 'h', 'i' ],
    [ 'y', 't', 'b', 't', 'm', 'i', 'd', 'k', 'd', 'w', 'u', 's', 'h', 'c', 'f', 't', 'c', 'g', 'g', 'q', 'i', 'i', 'x', 'o', 'f', 'o', 't', 'n', 'w', 'c' ],
    [ 'd', 'u', 'h', 'm', 'j', 'w', 'e', 'e', 'j', 'a', 'a', 'z', 'x', 'd', 'r', 't', 'q', 'h', 'y', 's', 'o', 't', 'r', 'l', 'k', 'i', 'w', 'o', 'v', 'e' ],
    [ 'i', 'b', 'y', 'g', 'x', 'k', 't', 'x', 'p', 'b', 'v', 'j', 'b', 'a', 'm', 'r', 'i', 'a', 'r', 'n', 'w', 'i', 'k', 'c', 's', 'e', 'n', 'w', 'a', 'b' ],
    [ 'y', 'e', 'd', 'm', 'i', 'a', 'r', 't', 'c', 'r', 's', 'b', 'g', 'h', 'd', 'o', 'b', 'v', 'e', 'x', 'o', 'x', 'e', 'c', 'l', 'b', 'v', 'a', 'z', 'j' ],
    [ 'i', 'v', 'g', 'b', 'i', 'l', 'z', 'e', 'y', 'g', 'w', 'r', 'z', 'e', 'p', 't', 'n', 'e', 'm', 'l', 'r', 'n', 'g', 'u', 'a', 'e', 'k', 'a', 't', 'm' ],
    [ 'c', 'g', 'h', 'l', 'i', 'a', 'f', 'k', 'q', 'b', 'e', 's', 't', 'd', 'w', 'q', 'r', 'a', 'y', 'z', 'i', 'f', 's', 'f', 'r', 'n', 't', 'o', 'w', 'b' ],
    [ 'o', 'f', 'r', 's', 's', 'e', 'u', 'l', 'c', 'd', 'i', 'e', 'j', 'y', 'v', 'z', 's', 'v', 'l', 'a', 'a', 'y', 'u', 's', 'o', 't', 's', 'i', 'r', 'i' ],
    [ 'n', 'h', 'h', 'e', 'j', 'x', 's', 't', 'n', 'r', 'c', 'g', 'p', 'z', 'l', 'x', 'p', 'a', 'r', 'i', 'b', 'w', 'e', 's', 'q', 'w', 'e', 't', 'm', 'f' ],
    [ 'p', 'a', 'y', 'c', 'm', 'm', 'd', 'i', 'd', 't', 'i', 'i', 'i', 'a', 'y', 'k', 'e', 'a', 'd', 'p', 's', 'x', 'r', 'a', 'n', 'v', 'm', 'm', 'u', 'e' ],
    [ 'o', 'o', 's', 'i', 'j', 'n', 'k', 'r', 'i', 'c', 't', 'j', 'p', 'n', 'e', 'w', 'l', 's', 'x', 'e', 'c', 'a', 'r', 'l', 'f', 'l', 'i', 'q', 'p', 'f' ],
    [ 's', 'f', 'q', 'o', 's', 'k', 'p', 'v', 'r', 'h', 'e', 'p', 'm', 't', 'g', 't', 'h', 'u', 'e', 'n', 'u', 't', 'c', 'g', 'w', 'd', 't', 's', 'u', 'n' ],
    [ 't', 'u', 'n', 'h', 'g', 'b', 'e', 'b', 'c', 'j', 'j', 's', 'c', 'c', 'e', 'e', 'd', 'j', 'x', 'g', 'j', 'j', 'l', 'g', 'k', 't', 'g', 'z', 'k', 'a' ],
    [ 'm', 't', 'i', 'c', 'z', 'v', 'r', 'c', 'w', 'x', 'u', 'q', 'g', 'w', 'm', 't', 'r', 'f', 'h', 'f', 'v', 'y', 'o', 'n', 'o', 'r', 'n', 'i', 'y', 'e' ],
    [ 'a', 'r', 'e', 'd', 'a', 'e', 'r', 'y', 'r', 'e', 't', 's', 'y', 'm', 'r', 'q', 't', 'b', 'o', 'y', 'i', 'w', 'd', 'i', 'i', 't', 'i', 'f', 'g', 'r' ],
    [ 's', 'l', 'a', 'j', 'a', 'g', 'f', 'i', 'l', 'h', 'n', 'z', 'j', 'x', 'n', 'u', 'd', 'q', 'r', 'u', 'c', 'e', 'x', 'y', 'h', 'z', 'd', 'n', 'i', 'a' ],
    [ 't', 'm', 'r', 'f', 'z', 'x', 'z', 'd', 'p', 'q', 'x', 'h', 'u', 'x', 'h', 'e', 'a', 'o', 'x', 'e', 'm', 'i', 'l', 'f', 'm', 'w', 'a', 'n', 'c', 'y' ],
    [ 'e', 'c', 'n', 'e', 'i', 'l', 'i', 's', 'e', 'r', 'i', 'n', 'e', 'l', 'c', 'y', 'x', 'r', 'x', 'b', 'a', 'y', 'z', 'i', 'u', 'w', 'e', 'q', 'v', 'e' ],
    [ 'r', 's', 'b', 'h', 'n', 'o', 'i', 't', 'a', 'g', 'i', 't', 's', 'e', 'v', 'n', 'i', 'm', 'n', 's', 'g', 'd', 'e', 'n', 't', 'i', 'r', 'z', 'w', 'o' ],
    [ 'm', 'q', 'j', 'i', 'y', 'b', 'e', 'k', 's', 'e', 'i', 'n', 'c', 'd', 'i', 'y', 'l', 's', 'h', 'n', 'v', 't', 'm', 'g', 'b', 'z', 'v', 'a', 'z', 'j' ],
    [ 'z', 'o', 'x', 'w', 'a', 'a', 'o', 'f', 'u', 'm', 'h', 'u', 'q', 's', 'a', 'n', 'd', 'b', 'o', 'x', 'h', 'u', 's', 'a', 'f', 'w', 'h', 'i', 's', 'n' ],
    [ 'c', 'q', 'z', 'r', 'm', 'b', 'x', 'r', 'v', 'n', 'q', 'a', 'z', 'c', 'e', 'd', 'q', 's', 'b', 'e', 'r', 's', 'g', 'm', 'n', 'q', 'm', 'i', 'j', 's' ],
];


main(process.argv)


function main(args) {
    for (let word of words) {
        let location = findWord(word);
        if (!location) {
            console.log('The word ' + word + ' is not in the puzzle.');
        } else {
            console.log('The word ' + word + ' is at row: ' + (location[0] + 1) + ', column ' + (location[1] + 1) + ', and direction ' + location[2]);
        }
    }
}


function findWord(word) {
    for (let row = 0; row < 30; row++) {
        for (let column = 0; column < 30; column++) {
            for (let direction of directions) {
                if (search(word, direction, row, column)) {
                    return [ row, column, direction ];
                }
            }
        }
    }

    return null;
}


function search(word, direction, row, column) {
    for (let ch of word) {

        if (row < 0 || column < 0 || row >= 30 || column >= 30 || puzzle[row][column] !== ch) {
            return false;
        }

        switch (direction) {
        case 'north':
            row--;
            break;
        case 'northeast':
            row--;
            column++;
            break;
        case 'east':
            column++;
            break;
        case 'southeast':
            row++;
            column++;
            break;
        case 'south':
            row++;
            break;
        case 'southwest':
            row++;
            column--;
            break;
        case 'west':
            column--;
            break;
        case 'northwest':
            row--;
            column--;
            break;
        }
    }

    return true;
}

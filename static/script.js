const square0Element = document.getElementById('square0')
const square1Element = document.getElementById('square1')
const square2Element = document.getElementById('square2')
const square3Element = document.getElementById('square3')
const square4Element = document.getElementById('square4')
const square5Element = document.getElementById('square5')
const square6Element = document.getElementById('square6')
const square7Element = document.getElementById('square7')
const square8Element = document.getElementById('square8')
const squareElements = [square0Element, square1Element, square2Element, square3Element, square4Element, square5Element, square6Element, square7Element, square8Element]

const currentTurnElement = document.getElementById('current-turn')
const twoPlayerButtonElement = document.getElementById('two-player-button')
const computerButtonElement = document.getElementById('computer-button')
const popupElement = document.getElementById('popup')
const overlayElement = document.getElementById('overlay')

twoPlayerButtonElement.addEventListener('click', startPlayersGame)
computerButtonElement.addEventListener('click', startComputerGame)

for (let squareNumber = 0; squareNumber < squareElements.length; squareNumber++) {
    squareElements[squareNumber].addEventListener('click', () => handleClick(squareNumber))
}

function startPlayersGame() {
    startGame(false)
    currentTurnElement.style.display = 'block'

}

function startComputerGame() {
    startGame(true)
    currentTurnElement.style.display = 'none'
}

async function startGame(isComputerGame) {
    for (let y = 0; y < 3; y++) {
        for (let x = 0; x < 3; x++) {
            squareElements[y * 3 + x].innerHTML = ''
        }
    }
    popupElement.style.display = 'none'
    overlayElement.style.display = 'none'

    const response = await fetch(`/start/${isComputerGame}`).then()
}

async function handleClick(squareNumber) {
    const response = await fetch(`/move/${squareNumber}`).then(response => response.json()).then(data => {
        if (data[0]) {
            for (let y = 0; y < 3; y++) {
                for (let x = 0; x < 3; x++) {
                    squareElements[y * 3 + x].innerHTML = data[2][y][x]
            }
            }
            currentTurnElement.innerHTML = `${data[3]}'s turn`
        }
        if (data[1]) {
            setTimeout(function () {
                alert(`Game over! ${data[4]} has won`)
            }, 500)
            
        }
        if (data[2] !== data[5]) {
            setTimeout(function () {
                for (let y = 0; y < 3; y++) {
                for (let x = 0; x < 3; x++) {
                    squareElements[y * 3 + x].innerHTML = data[5][y][x]
            }
            }
            }, 600)
        }
        if (data[6] && !data[1]) {
            setTimeout(function () {
                alert(`Game over! ${data[4]} has won`)
            }, 1000) }
    })
}
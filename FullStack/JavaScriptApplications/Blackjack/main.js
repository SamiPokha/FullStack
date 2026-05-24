let firstCard = 10
let secondCard = 4
let cards = [firstCard, secondCard]
let sum = firstCard + secondCard
let hasBlackJack = false
let isAlive = true
let message = ""
let messageEl = document.getElementById("message-el")
let messageSum = document.getElementById("sum-el")
let cardsEl = document.getElementById("cards-el")

function start() {
    render()
}

function render() {
    if (sum < 21) {
        message = "Do you want to draw a new card? 🙂"

    } else if (sum === 21) {
        message = "Woohoo! You've got Blackjack! 🥳"
        hasBlackJack = true

    } else {
        message = "You're out of the game! 😭"
        isAlive = false
    }

    messageEl.textContent = message
    messageSum.textContent = "Sum: " + sum
    cardsEl.textContent = "Cards: " + cards[0] + " " + cards[1]

}

function newcard() {
    let thirdCard = 7
    sum += thirdCard
    cards.push(thirdCard)
    start()
}

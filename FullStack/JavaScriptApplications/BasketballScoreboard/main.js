let homeScore = 0
let guestScore = 0

let homeStoreEl = document.getElementById("home-display")
let guestStoreEl = document.getElementById("guest-display")

function addPoints(team, points) {
    if (team === 'home') {
        homeScore += points
        homeStoreEl.textContent = homeScore
    } else {
        guestScore += points
        guestStoreEl.textContent = guestScore
    }
}

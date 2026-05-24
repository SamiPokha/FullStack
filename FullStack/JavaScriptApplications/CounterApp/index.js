let count = 0
let countEL = document.getElementById("count-el")
let saveEL = document.getElementById("save-el")

function increment() {
    count += 1
    countEL.textContent = count
}

function save() {
    let countStr = count + " - "
    saveEL.textContent += countStr
    count = 0
    countEL.textContent = 0
}

function resetall() {
    saveEL.textContent = "Previous entries: "
    count = 0
    countEL.textContent = 0
}
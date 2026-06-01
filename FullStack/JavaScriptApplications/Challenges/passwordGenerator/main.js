let pass1 = document.getElementById("pass1")
let pass2 = document.getElementById("pass2")

const characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
    "U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
    "s","t","u","v","w","x","y","z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9","~","`","!","@"
    ,"#","$","%","^","&","*","(",")","_","-","+","=","{","[","}","]",",","|",":",";","<",">",".","?",
    "/"];

function generate() {
    pass1.textContent = "";
    pass2.textContent = "";
    
    for (let i = 0; i < 15; i++) {
        let randomIndex1 = Math.floor(Math.random() * characters.length);
        pass1.textContent += characters[randomIndex1];
        
        let randomIndex2 = Math.floor(Math.random() * characters.length);
        pass2.textContent += characters[randomIndex2];
    }
}

// Function that handles the copying logic
function copyToClipboard(element) {
    const text = element.textContent;
    
    // Only copy if a password has actually been generated
    if (text !== "") {
        navigator.clipboard.writeText(text).then(() => {

            const originalText = text;
            element.textContent = "Copied!"
            element.style.color = "#white";
            
            // Change it back to the password after 1 second
            setTimeout(() => {
                element.textContent = originalText;
                element.style.color = "#1CD988";
            }, 1000);
        });
    }
}

// Attach the click events to your existing elements
pass1.addEventListener("click", function() { copyToClipboard(pass1); });
pass2.addEventListener("click", function() { copyToClipboard(pass2); });
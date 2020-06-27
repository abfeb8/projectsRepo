var boxes = document.getElementsByClassName("box");
var rgbCode = document.getElementById("rgbCode");
var resultDisplay = document.getElementById("result");
var title = document.getElementById("#title");

// function to generate a random rgb() color code
function getColor() {
    color =
        "rgb(" +
        Math.floor(Math.random() * 225).toString() +
        ", " +
        Math.floor(Math.random() * 225).toString() +
        ", " +
        Math.floor(Math.random() * 225).toString() +
        ")";
    return color;
}

// filling all the boxes with randome colors
for (i = 0; i < 6; i++) {
    boxes[i].style.backgroundColor = getColor();
}

// picking up a right and box and displaying the rgb() code
var ansColor = getColor();
var ans = Math.floor(Math.random() * 5);
boxes[ans].style.backgroundColor = ansColor;
rgbCode.textContent = ansColor.toUpperCase();

function correctAnswer() {
    resultDisplay.textContent = "Right Answer!";
    for (i = 0; i < 6; i++) {
        boxes[i].style.backgroundColor = ansColor;
    }
    rgbCode.textContent = "PLAY AGAIN!";
    rgbCode.style.border = "2px solid white";
    rgbCode.style.borderRadius = "30px";
    rgbCode.style.width = "300px";
    rgbCode.style.backgroundColor = "green";
    rgbCode.style.margin = "0 auto";
    rgbCode.addEventListener("click", resetGame);
}

function wrrongAnswer(i) {
    resultDisplay.textContent = "Try Again!!!";
    boxes[i].style.backgroundColor = "#232323";
}

function resetGame() {
    for (i = 0; i < 6; i++) {
        boxes[i].style.backgroundColor = getColor();
    }
    ans = Math.floor(Math.random() * 5);
    ansColor = getColor();
    boxes[ans].style.backgroundColor = ansColor;
    rgbCode.style.border = "none";
    rgbCode.style.width = "auto";
    rgbCode.style.backgroundColor = "cornflowerblue";
    rgbCode.textContent = ansColor.toUpperCase();
    resultDisplay.textContent = "";
}

// adding event listener for checking right answer
boxes[0].addEventListener("click", function () {
    if (ans == 0) {
        correctAnswer();
        console.log("Right Answer");
    } else {
        wrrongAnswer(0);
        console.log("Try Again!!");
    }
});
boxes[1].addEventListener("click", function () {
    if (ans == 1) {
        correctAnswer();
        console.log("Right Answer");
    } else {
        wrrongAnswer(1);
        console.log("Try Again!!");
    }
});
boxes[2].addEventListener("click", function () {
    if (ans == 2) {
        correctAnswer();
        console.log("Right Answer");
    } else {
        wrrongAnswer(2);
        console.log("Try Again!!");
    }
});
boxes[3].addEventListener("click", function () {
    if (ans == 3) {
        correctAnswer();
        console.log("Right Answer");
    } else {
        wrrongAnswer(3);
        console.log("Try Again!!");
    }
});
boxes[4].addEventListener("click", function () {
    if (ans == 4) {
        correctAnswer();
        console.log("Right Answer");
    } else {
        wrrongAnswer(4);
        console.log("Try Again!!");
    }
});
boxes[5].addEventListener("click", function () {
    if (ans == 5) {
        correctAnswer();
        console.log("Right Answer");
    } else {
        wrrongAnswer(5);
        console.log("Try Again!!");
    }
});

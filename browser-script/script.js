// ==UserScript==
// @name         Solver new
// @namespace    http://tampermonkey.net/
// @version      2024-03-08
// @description  try to take over the world!
// @author       You
// @match        https://wordlegame.org/it
// @icon         https://www.google.com/s2/favicons?sz=64&domain=wordlegame.org
// @grant        none
// ==/UserScript==


function runScript() {
    'use strict';

    let greyLetters = Array.from(document.querySelectorAll(".Row-letter.letter-absent"))
                         .map(el => el.firstChild.textContent)
                         .join('');

    let resultRegex = '';

    const matrix = document.getElementsByClassName("Row Row-locked-in");
    for (let row = 0; row < 5; row++) {
        let greenLetter = '';
        let yellowLetters = '';
        for (let col = 0; col < matrix.length; col++) {
            const className = matrix[col].children[row].className;
            const data = matrix[col].children[row].firstChild.data;

            if (className.includes("correct") && !greenLetter.includes(data)) {
                greenLetter += data;
            }
            if (className.includes("elsewhere") && !yellowLetters.includes(data) && !greyLetters.includes(data) ) {
                yellowLetters += data;
            }
        }
        // end of col loop
        resultRegex += greenLetter.length > 0 ? greenLetter : `[^${yellowLetters}${greyLetters}]`;
    }
    // end of row loop
    let mustInclude = Array.from(document.querySelectorAll(".Game-keyboard-button.letter-elsewhere"))
                         .map(el => el.firstChild.textContent)
                         .join('');

    const obj = {
        "result_regex": resultRegex,
        "must_include": mustInclude,
    }

    fetch("http://127.0.0.1:8000/solver/", {
        method: "post",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },

        body: JSON.stringify(obj)
    })
    .then(response => response.json())
    .then(data => createList(data))
    .catch(error => console.error('Error:', error));
};

function createList(obj) {
    const oldDiv = document.getElementById("solver-results");
    if (oldDiv) document.body.removeChild(oldDiv);

    const div = document.createElement("div");
    div.id = "solver-results";
    div.style = "top:0;left:0;position:absolute;z-index:99999;padding:20px;width:300px;height:100vh;background-color:lightblue;overflow-y:auto;";
    document.body.appendChild(div);

    for (const el of obj) {
        const p = document.createElement('p');
        p.innerText = el.word;
        div.appendChild(p);
    }
}


(function() {
    'use strict';
    const button = document.createElement("Button");
    button.innerHTML = "Run script";
    button.addEventListener("click", runScript);
    button.style = "top:0;right:0;position:absolute;z-index:99999;padding:20px;";
    document.body.appendChild(button);
})();
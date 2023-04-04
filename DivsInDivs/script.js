const middle = document.getElementById("middle")
//const divList = middle.children;

let listH = document.getElementsByClassName("horizontal")
let listV = document.getElementsByClassName("vertical")

let divList = [];

for (let i = 0; i < listH.length; i++) {
    divList.push(listH[i]);
}
for (let i = 0; i < listV.length; i++) {
    divList.push(listV[i]);
}


divList.forEach(el => {
    el.addEventListener("click", () => 
    {
        console.log("bah");
    }, false);
});


var classes = ["horizontal" , "vertical"]
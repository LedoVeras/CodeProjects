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

var classes = ["horizontal" , "vertical"]


addDivEvent = function(element){
    element.addEventListener("click", (event) => 
    {
        event.stopPropagation();
        
        let curClass = element.className;
        let nextClass = classes[Math.abs(1 - classes.indexOf(curClass))];

        let childDiv = document.createElement("div");
        childDiv.className = nextClass

        element.appendChild(childDiv);

        addDivEvent(childDiv);
    }, false);
}


divList.forEach(el => {
    addDivEvent(el);
});


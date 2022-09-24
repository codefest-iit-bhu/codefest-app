const tar="uuddlrlrba"
var code=""
var idleTime=0
window.onload=function(){
    resetTimer()
    code=""
}

idleTime=setInterval(incrIdle, 1000)
document.addEventListener('keyup', e=>{
    resetTimer()
    if(e.code=='ArrowUp') {code+="u"}
    else if(e.code=='ArrowDown') {code+="d"}
    else if(e.code=='ArrowLeft') {code+="l"}
    else if(e.code=='ArrowRight') {code+="r"}
    else if(e.code=='KeyA') {code+="a"}
    else if(e.code=='KeyB') {code+="b"}
    else {code=""}

    if(code==tar) {konamiCode()}
    else if(code.length()>=tar.length()){code=""}
    console.log(e)
})

function incrIdle(){
    idleTime+=1;
    if(idleTime>10) {
        resetTimer()
        code=""
    }
}

function resetTimer(){
    idleTime=0
}

function konamiCode() {
    code=""
    alert("I am Iron Man")
    resetTimer()
}
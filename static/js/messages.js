
setTimeout(clearMessages, 10000);

function clearMessages() {
    const element = document.getElementById("msg");
    element.style.display = "none";
    console.log("cleared");
}
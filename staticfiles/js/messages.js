//clear messages after 10 seconds
setTimeout(clearMessages, 10000);

function clearMessages() {
    const element = document.getElementById("msg");
    element.style.display = "none";
    console.log("cleared");
}
let name = document.getElementById("name")
let clientSocket = new WebSocket("ws://localhost:8888", "protocolOne")
let test = document.getElementById("f")


test.onsubmit = (event) => {
    console.log("Vous avez écrit : " + name.value)
    clientSocket.send(name.value)
    name.value = ""
    return false
}

clientSocket.onmessage = (event) => {
    console.log(event.data)
}

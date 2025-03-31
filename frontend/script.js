function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    let chatbox = document.getElementById("chatbox");

    if (userInput.trim() === "") return;

    // Add user message to chat
    let userMessage = document.createElement("p");
    userMessage.className = "user";
    userMessage.innerText = "You: " + userInput;
    chatbox.appendChild(userMessage);

    // Send user message to backend
    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Add bot response to chat
        let botMessage = document.createElement("p");
        botMessage.className = "bot";
        botMessage.innerText = "Bot: " + data.reply;
        chatbox.appendChild(botMessage);
    });

    document.getElementById("userInput").value = "";
}
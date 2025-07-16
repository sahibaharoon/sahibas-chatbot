let chatHistory = [];

async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class='user'>You: ${message}</div>`;
  chatHistory.push("You: " + message);
  input.value = "";

  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  const data = await res.json();
  const reply = data.reply;

  const botDiv = document.createElement("div");
  botDiv.className = "bot";
  chatBox.appendChild(botDiv);

  let i = 0;
  function typeChar() {
    if (i < reply.length) {
      botDiv.innerHTML += reply.charAt(i);
      i++;
      setTimeout(typeChar, 20);
    } else {
      chatHistory.push("Bot: " + reply);
    }
  }
  typeChar();
}

function downloadChat() {
  const blob = new Blob([chatHistory.join("\n\n")], { type: "text/plain" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "chat-history.txt";
  a.click();
  URL.revokeObjectURL(url);
}

function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
}
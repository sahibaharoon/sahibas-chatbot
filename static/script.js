async function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];
  if (!file) return alert("Please select a PDF file!");

  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch("/upload", { method: "POST", body: formData });
  const data = await res.json();

  if (data.success) {
    document.getElementById("previewText").innerText = "✅ File uploaded! Preview:\n" + data.preview;
  } else {
    alert(data.error);
  }
}

async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class='user'>You: ${message}</div>`;
  input.value = "";

  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  const data = await res.json();
  const reply = data.reply;

  // Typing effect
  const botDiv = document.createElement("div");
  botDiv.className = "bot";
  chatBox.appendChild(botDiv);

  let i = 0;
  function typeChar() {
    if (i < reply.length) {
      botDiv.innerHTML += reply.charAt(i);
      i++;
      setTimeout(typeChar, 20); // typing speed
    }
  }
  typeChar();
}
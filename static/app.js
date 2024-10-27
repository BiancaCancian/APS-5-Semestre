class Chatbox {

    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const { openButton, chatBox, sendButton } = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox));

        sendButton.addEventListener('click', () => this.onSendButton(chatBox));

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", (event) => {
            if (event.key === "Enter") {
                this.onSendButton(chatBox);
            }
        });
    }

    toggleState(chatBox) {
        this.state = !this.state;

        if (this.state) {
            chatBox.classList.add('chatbox--active');
        } else {
            chatBox.classList.remove('chatbox--active');
        }
    }

    onSendButton(chatBox) {
        var textField = chatBox.querySelector('input');
        let text1 = textField.value;
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 };
        this.messages.push(msg1);

        // Endpoint do Flask
        fetch('/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        .then(response => response.json())
        .then(data => {
            let msg2 = { name: "Sam", message: data.answer };
            this.messages.push(msg2);
            this.updateChatText(chatBox);
            textField.value = '';
        })
        .catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatBox);
            textField.value = '';
        });
    }

    updateChatText(chatBox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item) {
            if (item.name === "Sam") {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>';
            } else {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>';
            }
        });

        const chatMessage = chatBox.querySelector('.chatbox__messages');
        chatMessage.innerHTML = html;
    }
}

function sendSuggestion(question) {
    const chatInput = document.getElementById('chat-input'); 
    chatInput.value = question; 
    addMessageToChat(question); 
    hideSuggestions(); 
}

function addMessageToChat(message) {
    const messagesContainer = document.querySelector('.chatbox__messages');
    const messageElement = document.createElement('div');
    messageElement.classList.add('messages__item', 'messages__item--visitor');
    messageElement.textContent = message;
    messagesContainer.prepend(messageElement); 
}

function hideSuggestions() {
    const suggestions = document.querySelector('.suggestions');
    suggestions.style.display = 'none'; 
}


const chatbox = new Chatbox();
chatbox.display();
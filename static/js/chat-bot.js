document.addEventListener('DOMContentLoaded', function() {
    const messagesList = document.querySelector('.messages-list');
    const messageForm = document.querySelector('.message-form');
    const messageInput = document.querySelector('#message');

    // Upewnij się, że imageSrc i imageYou są dostępne
    if (typeof imageSrc === 'undefined' || typeof imageYou === 'undefined') {
        console.error('Image sources are not defined');
        return;
    }

    function appendMessage(message, sender, isHtml = false) {
        const messageItem = document.createElement('li');
        messageItem.classList.add('message', sender, 'flex', 'flex-col', 'items-start');
        let content;
        if (isHtml) {
            content = message; // Bezpośrednio przypisz HTML
        } else {
            content = `<div class="message-content">${message}</div>`; // Zwykły tekst zamieniony na HTML
        }

        const imageSrcToUse = sender === 'sent' ? imageYou : imageSrc;

        messageItem.innerHTML = `
            <div class="flex items-center">
                <img src="${imageSrcToUse}" alt="${sender === 'sent' ? 'You' : 'MateU'}" class="w-16 h-16 rounded-full mr-4">
                <div class="message-text p-3 ${sender === 'sent' ? 'bg-green-100' : 'bg-gray-200'} rounded-lg">
                    <div class="message-sender font-bold">
                        ${sender === 'sent' ? 'You' : 'MateU'}
                    </div>
                    ${content} <!-- Użyj content, który może być HTML -->
                </div>
            </div>`;
        messagesList.appendChild(messageItem);
        messageItem.scrollIntoView({ behavior: "smooth" });
    }

    function showLoading() {
        const loadingItem = document.createElement('li');
        loadingItem.classList.add('loading', 'flex', 'flex-col', 'items-center');
        loadingItem.innerHTML = `
            <div class='flex space-x-2 justify-center items-center bg-white dark:invert'>
                <span class='sr-only'>Loading...</span>
                <div class='h-6 w-6 bg-black rounded-full animate-bounce [animation-delay:-0.3s]'></div>
                <div class='h-6 w-6 bg-red-500 rounded-full animate-bounce [animation-delay:-0.15s]'></div>
                <div class='h-6 w-6 bg-blue-600 rounded-full animate-bounce'></div>
            </div>`;
        messagesList.appendChild(loadingItem);
        loadingItem.scrollIntoView({ behavior: "smooth" });
        return loadingItem;
    }

    function hideLoading(loadingItem) {
        if (loadingItem) {
            messagesList.removeChild(loadingItem);
        }
    }

    messageForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const message = messageInput.value.trim();
        if (message.length === 0) {
            return;
        }

        appendMessage(message, 'sent');
        messageInput.value = '';

        const loadingItem = showLoading();

        fetch('', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({
                'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                'message': message
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const htmlResponse = data.response; // Odpowiedź jest już w HTML
            appendMessage(htmlResponse, 'received', true); // Przekazanie flagi, że odpowiedź jest w HTML
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
            appendMessage('Sorry, there was an error processing your request.', 'received', true); // Wyświetl wiadomość o błędzie
        })
        .finally(() => {
            hideLoading(loadingItem);
        });
    });
});

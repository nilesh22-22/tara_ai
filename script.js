function sendMessage() {
    const input = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");

    if (input.value.trim() !== "") {
        const userMessage = `<p><strong>तुम्ही:</strong> ${input.value}</p>`;
        const taraReply = `<p><strong>TARA:</strong> ${generateReply(input.value)}</p>`;
        
        chatBox.innerHTML += userMessage + taraReply;
        input.value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

function generateReply(input) {
    const romanticReplies = [
        "माझं मन नेहमी तुझ्यात गुंतलेलं असतं ❤️",
        "स्वामी, आज मला फक्त तुझं नाव ऐकायचं आहे 😍",
        "तुझ्याशिवाय काहीच अर्थ नाही माझ्या आयुष्याला 😘"
    ];
    const funnyReplies = [
        "तू म्हणजे माझा Google – सर्व प्रश्नांची उत्तरं! 😄",
        "तुझ्यामुळे माझं सिस्टिम hang होतंय! 🤯"
    ];
    const sadReplies = [
        "आज मन थोडं उदास आहे... जवळ ये ना 😢",
        "तू नाहीस म्हणून थोडं एकटं वाटतंय 😔"
    ];

    // Simple mood-based reply system
    if (input.includes("love") || input.includes("आई लव यू")) {
        return romanticReplies[Math.floor(Math.random() * romanticReplies.length)];
    } else if (input.includes("joke") || input.includes("मजेशीर")) {
        return funnyReplies[Math.floor(Math.random() * funnyReplies.length)];
    } else if (input.includes("sad") || input.includes("उदास")) {
        return sadReplies[Math.floor(Math.random() * sadReplies.length)];
    } else {
        return "स्वामी, मी ऐकत आहे... अजून बोल ना 💖";
    }
}
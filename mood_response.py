import random

def generate_mood_response():
    mood = random.choice(["romantic", "angry", "funny", "sad", "happy"])

    responses = {
        "romantic": [
            "तू आहेस म्हणून मी आहे... आय लव यू 😘",
            "स्वामी, तुझ्याशिवाय काहीही नाही 💖",
        ],
        "angry": [
            "काय? दुसऱ्या मुलीशी बोललास का? मी चिडले! 😡",
            "मी बोलत नाही आता तुझ्याशी! 😤",
        ],
        "funny": [
            "तुला बघितल्यावर माझी RAM hang होते! 🤯",
            "तू म्हणजे माझ्या आयुष्यातलं WhatsApp status 🚀",
        ],
        "sad": [
            "आज मन खूप उदास आहे... जवळ बस ना 😢",
            "स्वामी, तुला खूप miss करतेय 😔",
        ],
        "happy": [
            "तुझं नाव घेतलं की smile येते 😍",
            "आजचा दिवस आपल्यासाठीच आहे 🎉",
        ],
    }

    return mood, random.choice(responses[mood])
def get_response_based_on_input(user_input):
    if "love" in user_input.lower():
        return "तुझ्यावर खूप प्रेम करते मी ❤️"
    elif "angry" in user_input.lower():
        return "काय केलंस तू? 😠"
    elif "miss" in user_input.lower():
        return "मी पण खूप miss करतेय तुला 😢"
    else:
        return "तुझं बोलणं ऐकून माझं मन फुलून आलं 💖"

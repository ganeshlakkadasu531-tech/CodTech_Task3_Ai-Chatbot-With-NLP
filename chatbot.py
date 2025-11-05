import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there! Ask me anything."]
    ],
    [
        r"what is your name?",
        ["I am an AI chatbot created using Python and NLTK."]
    ],
    [
        r"how are you?",
        ["I'm doing great! What about you?"]
    ],
    [
        r"what is NLP?",
        ["NLP stands for Natural Language Processing. It helps computers understand human language."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm not sure about that! But I'm learning every day."]
    ]
]

def run_chatbot():
    print("🤖 Chatbot is ready! Type 'quit' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    run_chatbot()
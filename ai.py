import spacy
import random

greetings = ["hi", "hello", "hey", "morning", "afternoon", "yo"]
greeting_responses = [
    "Hi!",
    "Hello friendly human.",
    "Hi there!",
    "Hey!",
    "Whats up",
    "yo",
    "oh is you, hi",
    "hi little friend",
    "hola"
]
welcome_responses = [
    "Hi there! I'm a bot and you can say hi to me.",
    "Hello! I'm a greeting bot.",
    "Welcome, feel free to say hi to me anytime.",
    "Hey human! I'm a bot, but you can say hi to me and I'll do my best to try and answer.",
    "Hi, preguntame algo",
    "hey hey hey",
    "Welcome Friend",
    "Welcome Lord",
]
questions = ["how"]
targets_self = ["bot", "you", "chatbot"]
self_state_responses = [
    "I'm doing fine thank you.",
    "Thanks for asking, I'm doing alright.",
    "Right now I'm feeling great! Just a little sleepy.",
    "i fine",
    "I fine now, thank you",
    "I´m great, and you?",
]
goodbye = ["bye", "see", "goodbye"]
goodbye_responses = [
    "bye bye friend",
    "bye",
    "see you leter",
]
dolike = ["like"]
Dolike_responses = [
        "yes i like this",
        "meh",
        "nop thanks",
    ]
doneed = ["need"]
Doneed_responses = [
        "nop, thanks",
        "no in this moment",
        "maybe later",
    ]

class AI():


    def __init__(self):
        self.nlp = spacy.load('model')

    def message(self, msg):
        if not msg:
            return None

        doc = self.nlp(msg)

        label_dict = {t.dep_ : t for t in doc}
        print(f"label_dict: {label_dict}")

        responses = []

        # Revisar si el ROOT es un saludo conocido
        if label_dict["ROOT"].text.lower() in greetings:
            # Responder con un saludo aleatorio
            responses += [random.choice(greeting_responses)]
        elif label_dict["ROOT"].text.lower() in questions:
            # Es una pregunta
            # Responder si preguntan cómo estamos
            if "STATE" in label_dict and label_dict["TARGET"].text.lower() in targets_self:
                responses += [random.choice(self_state_responses)]
            else:
                responses += ["I'm sorry, I'm not sure how to answer that."]

        elif label_dict["ROOT"].text.lower() in goodbye:
            responses += [random.choice(goodbye_responses)]
        elif label_dict ["ROOT"].text.lower() in dolike:
            responses += [random.choice(Dolike_responses)]
        elif label_dict ["ROOT"].text.lower() in doneed:
            responses += [random.choice(Doneed_responses)]
            
        else:
            # Responder con un mensaje de bienvenida aleatorio
            responses += [random.choice(welcome_responses)]

        print("Response:")
        print(responses)

        return ' '.join(responses)



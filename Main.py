from ChatBot import ChatBot

context = """who are you?
My name is RoboTec, and I'm here to help you"""

first_message = """Hola, mi nombre es RoboTec y estoy aquí para ayudarte
en lo que necesites saber sobre el Tec. ¿En qué te puedo ayudar?"""

seed = 44
tokenizer = model = 'microsoft/DialoGPT-large'

if __name__ == "__main__":
    ChatBot(context, seed, model, tokenizer, first_message).run()
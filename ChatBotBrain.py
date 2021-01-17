from transformers import pipeline, set_seed
from googletrans import Translator

class ChatBotBrain:
    def __init__(self, context, seed, model, tokenizer):
        self.context = context
        self.generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
        set_seed(seed)
        self.parsed_context = self.generator.tokenizer.eos_token.join(context.split("\n"))
        self.translator = Translator()
        self.temporal_context = []

    def translate(self, text, src, dest):
        try:
            return self.translator.translate(text, src=src, dest=dest).text
        except:
            print('Algó falló ->', text)
            return 'Lo siento, no pude entenderte.'

    def talk(self, question):
        question = self.translate(question, 'es', 'en')
        self.temporal_context.append(question)
        parsed_temp_context = self.generator.tokenizer.eos_token.join(self.temporal_context[-3:])
        context_input = self.generator.tokenizer.eos_token.join([self.parsed_context, parsed_temp_context, ""])
        max_length = len(self.generator.tokenizer.encode(context_input)) + 30
        generated_text = self.generator(context_input, max_length=max_length)
        generated_text = generated_text[0]["generated_text"].split(self.generator.tokenizer.eos_token)[-1]
        self.temporal_context.append(generated_text)
        return self.translate(generated_text, 'en', 'es')
from transformers import MarianMTModel, MarianTokenizer

class HuggingFaceTranslator:
    def __init__(self, model_name="Helsinki-NLP/opus-tatoeba-es-zh"):
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate(self, text):
        try:
            inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
            translated = self.model.generate(**inputs)
            return self.tokenizer.decode(translated[0], skip_special_tokens=True)
        except Exception as e:
            return f"Error de traducción: {e}"
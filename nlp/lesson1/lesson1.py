import re
import json
import numpy as np
import pandas as pd
from typing import List

class TextCleaner:
    def clean(self,text):
        text = text.lower() # Harfleri küçültür
        
        # 1. Tekrar eden harfleri normalleştirme (örn: 'cooooool' -> 'cool')
        text = re.sub(r"(.)\1{2,}", r"\1\1", text) 
        
        # 2. URL'leri kaldırma (http/https ile başlayan linkler)
        text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
        
        # 3. HTML etiketlerini kaldırma (örn: <div>...</div>)
        text = re.sub(r"<.*?>", "", text)

        # 4. Hashtag (#) ve Mention (@) kaldırma
        text = re.sub(r"#\w+", "", text) # #hashtag siler
        text = re.sub(r"@\w+", "", text) # @kullanici siler

        # 5. Sayıları kaldırma
        text = re.sub(r"\d+", "", text) 

        # 6. Noktalama işaretlerini kaldırma (Kelimeler ve boşluklar kalsın)
        text = re.sub(r"[^\w\s]", "", text) 

        # 7. Sadece harfleri tutma (Sayılar ve noktalama gider)
        text = re.sub(r"[^a-z\s]", " ", text)

        # 8. Emojileri ve ASCII olmayan karakterleri kaldırma
        text = re.sub(r"[^\x00-\x7F]+", "", text)

        # 9. Fazla boşlukları temizleme (En sona koymak iyidir)
        text = re.sub(r"\s+", " ", text).strip()
        
        return text
    
    def tokenizer(self,text: str) -> list:
        return re.findall(r"\b[a-z]+\b", text) 

class Tokenizer:
    PAD_TOKEN = "<PAD>"
    UNK_TOKEN = "<UNK>"

    def __init__(self):
        self.word2id = {}
        self.id2word = {}

    def tokenize(self, text: str) -> List[str]:
        return re.findall(r"\b[a-z]+\b", text)

    def build_vocab(self, token_lists: List[List[str]]):
        all_tokens = []
        for tokens in token_lists:
            all_tokens.extend(tokens)

        vocab = sorted(set(all_tokens))
        vocab = [self.PAD_TOKEN, self.UNK_TOKEN] + vocab

        self.word2id = {word: idx for idx, word in enumerate(vocab)}
        self.id2word = {idx: word for word, idx in self.word2id.items()}

    def encode(self, tokens: List[str]) -> List[int]:
        return [
            self.word2id.get(token, self.word2id[self.UNK_TOKEN])
            for token in tokens
        ]

    def decode(self, ids: List[int]) -> List[str]:
        return [
            self.id2word.get(idx, self.UNK_TOKEN)
            for idx in ids
        ]

    def save(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.word2id, f, ensure_ascii=False, indent=2)

    def load(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            self.word2id = json.load(f)

        self.id2word = {int(idx): word for word, idx in self.word2id.items()}

    def __len__(self):
        return len(self.word2id)

class NLPPipeline:
    def __init__(self):
        self.cleaner = TextCleaner()
        self.tokenizer = Tokenizer()

    def fit_transform(self, texts: pd.Series):
        texts = texts.dropna()

        cleaned = [self.cleaner.clean(t) for t in texts]
        tokenized = [self.tokenizer.tokenize(t) for t in cleaned]

        self.tokenizer.build_vocab(tokenized)

        encoded = [self.tokenizer.encode(toks) for toks in tokenized]

        return cleaned, tokenized, encoded


if __name__ == "__main__":

    data = {
        "review_id": list(range(1, 21)),
        "review": [
            "I LOVE NLP!!! It is amazing 😍",
            "NLP is hard... but very powerful.",
            "I hate bugs in code!!!",
            "This course is not bad at all.",
            "I really really love machine learning.",
            "The lecture was boring and too long...",
            "Amazing content, very good explanations!",
            "I do not like this topic 😕",
            "The model works well, no errors so far.",
            "Bad documentation and confusing examples.",
            "I love love LOVE this course!",
            "Not good, not useful, not clear.",
            "The teacher explains things very clearly.",
            "I hate waiting for the code to run.",
            "This is okay, nothing special.",
            "Powerful techniques but hard to understand.",
            "Great examples and practical exercises!",
            "Too many bugs, very bad experience.",
            "I am satisfied with the results 🙂",
            "Terrible performance and bad optimization."
        ]
    }

    df = pd.DataFrame(data)

    pipeline = NLPPipeline()
    cleaned, tokens, encoded = pipeline.fit_transform(df["review"])

    df["cleaned"] = cleaned
    df["tokens"] = tokens
    df["encoded"] = encoded

    print(df.head())
    print("Vocab size:", len(pipeline.tokenizer))

    pipeline.tokenizer.save("vocab.json")

    # 🔁 Decode test
    print("Decode example:", pipeline.tokenizer.decode(encoded[0]))
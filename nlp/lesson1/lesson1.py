import re
import json
import nltk
import numpy as np
import pandas as pd

from typing import List
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# NLTK verilerini indir (ilk çalıştırmada gerekli)
nltk.download('stopwords', quiet=True)


class TextCleaner:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
    
    def clean(self, text):
        text = text.lower()
        text = re.sub(r"(.)\1{2,}", r"\1\1", text)
        text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
        text = re.sub(r"<.*?>", "", text)
        text = re.sub(r"#\w+", "", text)
        text = re.sub(r"@\w+", "", text)
        text = re.sub(r"\d+", "", text)
        text = re.sub(r"[^\w\s]", "", text)
        text = re.sub(r"[^a-z\s]", " ", text)
        text = re.sub(r"[^\x00-\x7F]+", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text
    
    def tokenize(self, text: str) -> list:
        return re.findall(r"\b[a-z]+\b", text)
    
    def remove_stopwords(self, tokens: list) -> list:
        return [word for word in tokens if word not in self.stop_words]
    
    def stem(self, tokens: list) -> list:
        return [self.stemmer.stem(word) for word in tokens]


class Tokenizer:
    PAD_TOKEN = "<PAD>"
    UNK_TOKEN = "<UNK>"

    def __init__(self):
        self.word2id = {}
        self.id2word = {}
    
    def pad_sequence(self, sequence: List[int], max_len: int) -> List[int]:
        pad_id = self.word2id[self.PAD_TOKEN]
        if len(sequence) >= max_len:
            return sequence[:max_len]
        return sequence + [pad_id] * (max_len - len(sequence))

    def pad_batch(self, sequences: List[List[int]], max_len: int) -> List[List[int]]:
        return [self.pad_sequence(seq, max_len) for seq in sequences]

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
        tokenized = [self.cleaner.tokenize(t) for t in cleaned]
        no_stopwords = [self.cleaner.remove_stopwords(t) for t in tokenized]
        stemmed = [self.cleaner.stem(t) for t in no_stopwords]

        self.tokenizer.build_vocab(stemmed)

        encoded = [self.tokenizer.encode(toks) for toks in stemmed]

        return cleaned, stemmed, encoded


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

    pipeline.tokenizer.save("lesson1/vocab.json")

    MAX_LEN = 8

    padded = pipeline.tokenizer.pad_batch(encoded, MAX_LEN)
    df["padded"] = padded

    print(df[["encoded", "padded"]].head())
    print("Decode example:", pipeline.tokenizer.decode(encoded[0]))
    print("Encode example:", pipeline.tokenizer.encode(tokens[0]))

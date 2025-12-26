import re
import json
import pandas as pd
import numpy as np
from lesson1 import TextCleaner, Tokenizer, NLPPipeline


class DataPreprocessor:
    def __init__(self, vocab_path: str):
        self.pipeline = NLPPipeline()
        self.pipeline.tokenizer.load(vocab_path)
        self.cleaner = TextCleaner()  # Tokenize için cleaner kullan


class BoW:
    """
    Bag of Words (Kelime Çantası)
    
    Mantık:
    - Her kelime vocab'da bir sütun (index) ile temsil edilir
    - Her metin bir satır olur
    - Kelime metinde geçiyorsa o hücre 1 (veya kaç kez geçtiyse o kadar)
    - Geçmiyorsa 0
    """
    
    def __init__(self, tokenizer: Tokenizer, cleaner: TextCleaner):
        self.tokenizer = tokenizer
        self.cleaner = cleaner
        self.vocab_size = len(tokenizer)
    
    def transform(self, texts: list) -> np.ndarray:
        matrix = np.zeros((len(texts), self.vocab_size))
        
        for i, text in enumerate(texts):
            # TextCleaner ile tokenize et (Tokenizer'dan tokenize silindi)
            tokens = self.cleaner.tokenize(text.lower())
            encoded = self.tokenizer.encode(tokens)
            
            for token_id in encoded:
                matrix[i, token_id] += 1
        
        return matrix


class TF_IDF:
    """
    TF-IDF: Term Frequency - Inverse Document Frequency
    Nadir kelimeler daha değerli, yaygın kelimeler daha az değerli.
    """
    
    def __init__(self):
        self.idf = None

    def fit(self, bow_matrix):
        doc_count = (bow_matrix > 0).sum(axis=0)
        self.idf = np.log((len(bow_matrix) + 1) / (doc_count + 1)) + 1

    def transform(self, bow_matrix):
        return bow_matrix * self.idf

    def fit_transform(self, bow_matrix):
        self.fit(bow_matrix)
        return self.transform(bow_matrix)


class CosineSimilarity:
    pass


class N_Grams:
    pass


class Word2Vec:
    pass


class GloVe:
    pass


if __name__ == "__main__":
    
    datapre = DataPreprocessor("lesson1/vocab.json")
    print("Vocab Size:", len(datapre.pipeline.tokenizer))
    
    reviews = [
        "I love NLP it is amazing",
        "NLP is hard but very powerful",
        "I hate bugs in code",
        "I love love love this"
    ]
    
    # BoW oluştur (cleaner da ver)
    bow = BoW(datapre.pipeline.tokenizer, datapre.cleaner)
    bow_matrix = bow.transform(reviews)
    
    print("\nBoW Matrix boyutu:", bow_matrix.shape)
    
    # TF-IDF hesapla
    tf_idf = TF_IDF()
    tfidf_matrix = tf_idf.fit_transform(bow_matrix)
    print("\nTF-IDF Matrix boyutu:", tfidf_matrix.shape)
    print("\nİlk metin TF-IDF değerleri (sıfır olmayanlar):")
    non_zero = np.where(tfidf_matrix[0] > 0)[0]
    for idx in non_zero:
        word = datapre.pipeline.tokenizer.id2word.get(idx, "<UNK>")
        print(f"  '{word}': {tfidf_matrix[0, idx]:.2f}")
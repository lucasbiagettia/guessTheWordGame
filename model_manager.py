from sentence_transformers import SentenceTransformer

class Embedder:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Embedder, cls).__new__(cls)
            cls._instance.model = SentenceTransformer('hiiamsid/sentence_similarity_spanish_es')
        return cls._instance

    def encode_sentences(self, sentences):
        return self.model.encode(sentences)


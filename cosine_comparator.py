from sklearn.metrics.pairwise import cosine_similarity
from model_manager import Embedder

# Cargar el modelo SentenceTransformer
model = Embedder()

# Oraciones de ejemplo
sentence1 = 'gato'
sentence2 = 'Hola, ¿cómo te llamas?'

# Generar embeddings para las oraciones
embedding1 = model.encode_sentences([sentence1.lower()])
embedding2 = model.encode_sentences([sentence2])
input_u=""
while input_u != 'fin':
    input_u = input("inp")
    embedding2 = model.encode_sentences([input_u.lower()])

# Calcular la similitud coseno entre los embeddings
    similarity_score = cosine_similarity(embedding1, embedding2)[0][0]

    # Imprimir el resultado
    print(f"Similitud coseno entre las oraciones: {similarity_score}")

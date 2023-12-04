from model import ModelSingleton
import torch.nn.functional as F

def word_similarity(word1, word2):
    model = ModelSingleton()

    tensor1 = model.get_embedding(word1)
    tensor2 = model.get_embedding(word2)
    similarity = tensor_similarity(tensor1,tensor2)
    return similarity

# Tensores de ejemplo
def tensor_similarity(tensor1, tensor2):
    # Normalizar los tensores (opcional pero común para la similitud coseno)
    tensor1_normalized = F.normalize(tensor1, p=2, dim=1)
    tensor2_normalized = F.normalize(tensor2, p=2, dim=1)

    # Calcular la similitud coseno
    similarity = F.cosine_similarity(tensor1_normalized, tensor2_normalized, dim=1)
    return int((similarity.item()+ 1) * 5000)

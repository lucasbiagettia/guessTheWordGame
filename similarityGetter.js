import { HuggingFaceTransformersEmbeddings } from "langchain/embeddings/hf_transformers";


class Embedder {
  static model_path = 'Xenova/all-MiniLM-L6-v2';
  static model = null;

  static async getInstance(progress_callback = null) {
    if (this.model === null) {
      this.model = new HuggingFaceTransformersEmbeddings({
        modelName: this.model_path,
      });
    }
    
    return this.model;
  }
}


Embedder.getInstance();

export async function getEmbedding(text) {
  const model = await Embedder.getInstance();
  const res = await model.embedQuery(text);
  return res;
}


function cosineSimilarity(vec1, vec2) {
    if (vec1.length !== vec2.length) {
        throw new Error('Vectors must have the same lenght');
    }

    let dotProduct = 0;
    for (let i = 0; i < vec1.length; i++) {
        dotProduct += vec1[i] * vec2[i];
    }

    const magnitudeVec1 = Math.sqrt(vec1.reduce((sum, value) => sum + value ** 2, 0));
    const magnitudeVec2 = Math.sqrt(vec2.reduce((sum, value) => sum + value ** 2, 0));

    const similarity = dotProduct / (magnitudeVec1 * magnitudeVec2);

    return similarity;
}

export async function getSimilarity(text) {
  const vector = await getEmbedding(text);
  const vector2 = await getEmbedding("I like pizza")
  const similarity = cosineSimilarity(vector, vector2)
  console.log(similarity)
  return similarity
}




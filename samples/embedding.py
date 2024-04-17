from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

embedding_data = embedding.embed_documents(
    ["Cat", "Dog", "Blue", "Yellow", "Elephant", "Tiger", "Rose", "Jasmine"]
)

print(embedding_data[0][:1])

from langchain.evaluation import load_evaluator, EmbeddingDistance

evaluator = load_evaluator("embedding_distance")


print(
    evaluator.evaluate_strings(
        prediction="cat", reference="Cricket", embedding=embedding
    )
)
print(
    evaluator.evaluate_strings(
        prediction="cat",
        reference="kitty",
        embedding=embedding,
        distance_metric=EmbeddingDistance.EUCLIDEAN,
    )
)

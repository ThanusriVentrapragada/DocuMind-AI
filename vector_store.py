import numpy as np


class VectorStore:

    def __init__(self):
        self.chunks = []
        self.embeddings = []

    def add(self, chunks, embeddings):
        self.chunks.extend(chunks)
        self.embeddings.extend(embeddings)

    def search(self, query_embedding, top_k=3):
        if not self.embeddings:
            return []

        query = np.array(query_embedding)

        scores = []

        for i, embedding in enumerate(self.embeddings):
            vector = np.array(embedding)

            similarity = np.dot(query, vector) / (
                np.linalg.norm(query) * np.linalg.norm(vector)
            )

            scores.append((similarity, i))

        scores.sort(reverse=True)

        results = []

        for score, index in scores[:top_k]:
            results.append({
                "chunk": self.chunks[index],
                "score": float(score)
            })

        return results
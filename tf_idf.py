def bert(a, b):
    'From https://towardsdatascience.com/bert-for-measuring-text-similarity-eec91c6bf9e1'
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer('paraphrase-MiniLM-L3-v2')
    sentence_embeddings = model.encode([a, b])

    from sklearn.metrics.pairwise import cosine_similarity

    return cosine_similarity([sentence_embeddings[0]],
                             sentence_embeddings[1:]).item(0)

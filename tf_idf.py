def bert(a, b):
    'From https://towardsdatascience.com/bert-for-measuring-text-similarity-eec91c6bf9e1'
    from sentence_transformers import SentenceTransformer
   
    model = SentenceTransformer('paraphrase-MiniLM-L3-v2')
    sentence_embeddings = model.encode([a, b])

    from sklearn.metrics.pairwise import cosine_similarity

    result = cosine_similarity([sentence_embeddings[0]],
                             sentence_embeddings[1:]).item(0)
    if (result < 0) :
        return 0
    return result
  
X = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible."
Y = "Bees are flying insects closely related to wasps and ants, known for their role in pollination and, in the case of the best-known bee species, the western honey bee, for producinghoney. Bees are a monophyletic lineage within the superfamily Apoidea. They are presently considered a clade, called Anthophila. There are over 16,000 known species of bees in seven recognized biological families. Some species – including honey bees, bumblebees, and stingless bees – live socially in colonies while some species – including mason bees, carpenter bees, leafcutter bees, and sweat bees – are solitary."
#print(bert(X,Y))
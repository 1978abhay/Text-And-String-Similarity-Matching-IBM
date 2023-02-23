
# Should function as list comprehension version below,
# but will test to see which is more performant.
def longMongeElkan(m, textA, textB, simFunc):
    total = 0
    arrayA = textA.split(" ")
    arrayB = textB.split(" ")
    for a in arrayA:
        maxSimilarity = -10**8
        for b in arrayB:
            similarity = simFunc(a,b)
            if similarity > maxSimilarity:
                maxSimilarity = similarity
        total += maxSimilarity ** m

    return (total / len(arrayA)) ** (1 / m)
        
def simMongeElkan(m, textA, textB, simFunc):
    arrayB = textB.split(" ")
    arrayA = textA.split(" ")
    return (sum([max([simFunc(a,b) for b in arrayB])**m for a in arrayA])/len(arrayA))**(1/m)

def quadSimilarityME(textA, textB, simFunc):
    return simMongeElkan(2, textA, textB, simFunc)

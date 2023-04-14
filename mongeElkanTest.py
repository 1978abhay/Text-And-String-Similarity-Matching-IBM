import mongeElkan as me

from nltk.corpus import wordnet as wn


def main(textA, textB):
    while "  " in textA:
        textA = textA.replace("  ", " ")
    while "  " in textB:
        textB = textB.replace("  ", " ")

    # levenshtein score
    print(" ---- Levenshtein ---- ")
    print(f"   ", me.levenshtein_monge_elkan(textA, textB))

    # binary synonym score
    print(" ---- Synonym ---- ")
    ##    print("   ", me.longMongeElkan(1, textA, textB, lambda a, b: int(checkSyn.is_synonym(a, b))))
    ##    print("   ", me.quadSimilarityME(textA, textB, lambda a, b: int(checkSyn.is_synonym(a, b))))
    print(f"   ", me.synonym_monge_elkan(textA, textB))



if __name__ == "__main__":
    # textB = dr.getStory("clean_bbc_news_list_uk.json", 32)
    # textA = dr.getStory("clean_bbc_news_list_uk.json", 70)
    ##    textA = "According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too " \
    ##            "small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't " \
    ##            "care what humans think is impossible."
    ##    textB = "Bees are flying insects closely related to wasps and ants, known for their role in pollination and, " \
    ##            "in the case of the best-known bee species, the western honey bee, for producinghoney. Bees are a " \
    ##            "monophyletic lineage within the superfamily Apoidea. They are presently considered a clade, " \
    ##            "called Anthophila. There are over 16,000 known species of bees in seven recognized biological families. " \
    ##            "Some species – including honey bees, bumblebees, and stingless bees – live socially in colonies while " \
    ##            "some species – including mason bees, carpenter bees, leafcutter bees, and sweat bees – are solitary."

    textA = '''There are three dachshund coat varieties: smooth coat (short hair), long-haired, and wire-haired.[14] Longhaired dachshunds have a silky coat and short featherings on legs and ears. Wire-haired dachshunds are the least common coat variety in the United States (although it is the most common in Germany) and the most recent coat to appear in breeding standards.[14] Dachshunds have a wide variety of colors and patterns, the most common one being red. Their base coloration can be single-colored (either red or cream), tan pointed (black and tan, chocolate and tan, blue and tan, or isabella and tan), and in wire-haired dogs, a color referred to as wildboar. Patterns such as dapple (merle), sable, brindle and piebald also can occur on any of the base colors. Dachshunds in the same litter may be born in different coat colors depending on the genetic makeup of the parents.

The dominant color in the breed is red, followed by black and tan. Tan pointed dogs have tan (or cream) markings over the eyes, ears, paws, and tail. The reds range from coppers to deep rusts, with or without somewhat common black hairs peppered along the back, face and ear edges, lending much character and an almost burnished appearance; this is referred to among breeders and enthusiasts as an "overlay" or "sabling". Sabling should not be confused with a more unusual coat color referred to as sable. At a distance, a sable dachshund looks somewhat like a black and tan dog. Upon closer examination, however, one can observe that along the top of the dog's body, each hair is actually banded with red at the base near the skin transitioning to mostly black along the length of the strand. An additional striking coat marking is the brindle pattern. "Brindle" refers to dark stripes over a solid background—usually red. If a dachshund is brindled on a dark coat and has tan points, it will have brindling on the tan points only. Even one single, lone stripe of brindle is a brindle. If a dachshund has one single spot of dapple, it is a dapple.

The Dachshund Club of America (DCA) and the American Kennel Club (AKC) consider Double Dapple to be out of standard and a disqualifying color in the show ring. Piebald is now a recognized color in the Dachshund Club of America (DCA) breed standard.

Dogs that are double-dappled have the merle pattern of a dapple, but with distinct white patches that occur when the dapple gene expresses itself twice in the same area of the coat. The DCA excluded the wording "double-dapple" from the standard in 2007 and now strictly uses the wording "dapple" as the double dapple gene is commonly responsible for blindness and deafness.'''

    textB = '''Mount Everest is a peak in the Himalaya mountain range. It is located between Nepal and Tibet, an autonomous region of China. At 8,849 meters (29,032 feet), it is considered the tallest point on Earth. In the nineteenth century, the mountain was named after George Everest, a former Surveyor General of India. The Tibetan name is Chomolungma, which means “Mother Goddess of the World.” The Nepali name is Sagarmatha, which has various meanings.

The first ever recorded people to climb Everest were Edmund Hillary (a mountaineer from New Zealand) and his Tibetan guide Tenzing Norgay. They climbed the mountain in 1953 and hold the record together. The first records of Everest’s height came much earlier, in 1856. British surveyors recorded that Everest was the tallest peak in the world in their Great Trigonometrical Survey of the Indian subcontinent.

The Himalayan mountains have long been home to indigenous groups living in the valleys. The most famous of these are the Sherpa people. The word “Sherpa” is often used to mean mountain guide, though it actually refers to an ethnic group. The Sherpa have valuable experience in mountain climbing, which they can provide to other climbers. Most climbs of Everest would be impossible without the Sherpas’ logistical help and knowledge. However, their way of life extends beyond helping Everest climbers. Traditionally, their lifestyle has consisted of farming, herding, and trade. And, because they live at such a high altitude year round, they are accustomed to the low oxygen levels.

Climbing Mount Everest has become a popular expedition for mountain climbers. However, it is a dangerous undertaking. Climbing Everest requires a lot of experience mountaineering elsewhere, as well as a certificate of good health, equipment, and a trained Nepalese guide. The snow and ice on the mountain create deadly hazards like avalanches, and there is only a limited climbing season due to bad weather conditions. But perhaps the biggest danger is the altitude. Most climbers are not accustomed to the high altitude and low oxygen levels and rely on bottled oxygen they bring along. This is why the area above 8,000 meters (26,000 feet) elevation on Everest is called the “death zone.” Climbers who spend long periods in this region can develop altitude sickness and even brain swelling.

Mount Everest’s climbing industry has become controversial. As popularity of the climb has increased, there have been more “traffic jams” as climbers spend too much time in the death zone waiting for their chance to go to the summit. With more people has also come more pollution up near the summit as climbers often discard unwanted items all along the mountain. Additionally, the Sherpa people have been exploited by climbers, and their traditional way of life has been disrupted by foreign climbers. Sherpa guides are faced with some of the highest death rates of any field of employment, for comparatively little pay. Most disturbingly, because many climbers have died along the way, and their bodies are impossible to retrieve, climbers must frequently travel past corpses as they make their way up the mountain.'''

    textC = '''K2, Chinese Qogir Feng, also called Mount Godwin Austen, called locally Dapsang or Chogori, the world’s second highest peak (28,251 feet [8,611 metres]), second only to Mount Everest. K2 is located in the Karakoram Range and lies partly in a Chinese-administered enclave of the Kashmir region within the Uygur Autonomous Region of Xinjiang, China, and partly in the Gilgit-Baltistan portion of Kashmir under the administration of Pakistan.

The glacier- and snow-covered mountain rises from its base at about 15,000 feet (4,570 metres) on the Godwin Austen Glacier, a tributary of the Baltoro Glacier. The mountain was discovered in 1856 by Col. T.G. Montgomerie of the Survey of India, and it was given the symbol K2 because it was the second peak measured in the Karakoram Range. The name Mount Godwin Austen is for the peak’s first surveyor, Col. H.H. Godwin Austen, a 19th-century English geographer.

Blue Ridge Mountains. Blue Ridge Parkway. Autumn in the Appalachian Mountains in North Carolina, United States. Appalachian Highlands, Ridge and Valley, The Appalachian Mountain system
Britannica Quiz
All About Mountains Quiz

The first attempt to reach the summit was made by an Anglo-Swiss expedition in 1902 that ascended to 18,600 feet (5,670 metres) on the peak’s northeastern crest. Other unsuccessful attempts included an Italian expedition in 1909, led by Luigi Amedeo, duke d’Abruzzi, via the southeastern ridge (later called the Abruzzi Ridge) that reached approximately 20,000 feet (6,100 metres). In 1938 an American expedition led by Charles Houston via the Abruzzi Ridge reached about 26,000 feet (7,925 metres); in 1939 another American-led expedition following the same route reached about 27,500 feet (8,380 metres); and in 1953 another expedition led by Houston reached 25,900 feet (7,900 metres) on the Abruzzi Ridge. Finally, in 1954, an Italian expedition consisting of five scientists (including the geologist Ardito Desio as leader), a doctor, a photographer, and 12 others, including a Pakistani, managed to conquer the Abruzzi Ridge despite the severe weather conditions. The summit was reached at 6 PM on July 31, 1954, by Achille Compagnoni and Lino Lacedelli. In the course of the ascent, Mario Puchoz, one of the guides, died of pneumonia.

Because K2 is prone to frequent and severe storms that make the already treacherous climbing conditions on its slopes even more challenging—and humans find functioning at such high elevations difficult—it is one of the world’s most difficult mountains to climb. The number of people to have reached the top constitutes only a small fraction compared with how many have successfully climbed Mount Everest. In addition, although there have been fewer deaths on K2 compared with those on Mount Everest, the proportion of those killed to the number of people who have attempted climbing K2 is significantly higher.'''

    textD = '''Mount Everest—known in Nepali as Sagarmatha and Tibetan as Chomolungma—straddles the border between Nepal and Tibet at the crest of the Himalayan mountain chain. Although reaching the top of the world is an arduous and potentially deadly undertaking due to the extreme altitude, avalanches, icefalls, and other hazards, the mountain lies quite close to the equator, at a latitude of approximately 28 degrees, the same as Tampa, Florida.

Earth scientists estimate that Everest is 50 to 60 million years old, a youngster by geological standards. The mountain was formed by the upward force generated when the Indian and Eurasian tectonic plates collided, pushing up the rocks that formed the highest mountain on Earth. That force is still at work today, pushing Everest’s summit about a quarter of an inch higher each year. (Learn more about how mountains are formed.)

What are the hazards of climbing Everest?
At 29,032 feet, Everest’s summit has approximately one-third the air pressure that exists at sea level, which significantly reduces a climber's ability to breathe in enough oxygen. Because of this, scientists have determined that the human body is not capable of remaining indefinitely above 19,000 feet.'''
    print("Dachshund \n")
    main(textA, textB)
    print("Similar mountains \n")
    main(textC, textB)
    print("Same mountain \n")
    main(textD, textB)

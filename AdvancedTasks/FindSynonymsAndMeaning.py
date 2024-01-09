from nltk.corpus import wordnet
def dict_and_thesaurus(word):
    try:
        synsets = wordnet.synsets(word)

        if synsets:
            print(f'Definition of word {word} : ')
            for value in synsets:
                print(f'- {value.definition()}')

            synonyms = set()
            for value in synsets:
                for lemma in value.lemmas():
                    synonyms.add(lemma.name())

            if synonyms:
                print(f'\nSynonyms of {word}: {synonyms}')
            else:
                print(f'\nNo synonyms found for "{word}"')
        else:
            print(f'No definitions found for "{word}"')

    except Exception as ex:
        print(f"An error occured: {ex}")

dict_and_thesaurus(input('Enter a word: '))
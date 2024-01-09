def textAnalyzer(path):
    with open(path, "r") as file:
        text = file.read()
        words_count = len(text.split())
        sentence_count = text.count('.')
        words = text.split()
        word_length = [len(word) for word in words]
        average_word_length = sum(word_length)/len(word_length)

        print(f' Word_count: {words_count}\n '
              f'sentence_count: {sentence_count}\n'
              f' average_word_length: {average_word_length}')

file_path = 'sample_text'
textAnalyzer(file_path)

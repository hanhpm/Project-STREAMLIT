import streamlit as st

def initialize_distances(len_token1, len_token2):
    distances = [[0] * (len_token2 + 1) for _ in range(len_token1 + 1)]
    for t1 in range(len_token1 + 1):
        distances[t1][0] = t1
    for t2 in range(len_token2 + 1):
        distances[0][t2] = t2
    return distances

def calculate_min_distance(distances, t1, t2):
    a = distances[t1][t2 - 1]
    b = distances[t1 - 1][t2]
    c = distances[t1 - 1][t2 - 1]
    return min(a, b, c) + 1

def levenshtein_distance(token1, token2):
    len_token1, len_token2 = len(token1), len(token2)
    distances = initialize_distances(len_token1, len_token2)

    for t1 in range(1, len_token1 + 1):
        for t2 in range(1, len_token2 + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                distances[t1][t2] = calculate_min_distance(distances, t1, t2)

    return distances[len_token1][len_token2]

def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words

vocabs = load_vocab(file_path=r'C:\Users\Admin\OneDrive - Swinburne University\Documents\AIO-Exercise-2024\module-1\week-4\streamlit\data\vocab.txt')

def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):
        # compute levenshtein distance
        leven_distances = {vocab: levenshtein_distance(word, vocab) for vocab in vocabs}
        
        # sorted by distance
        sorted_distances = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)
        
        col2.write('Distances:')
        col2.write(sorted_distances)

if __name__ == "__main__":
    main()
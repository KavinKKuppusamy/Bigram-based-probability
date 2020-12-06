import sys
from collections import Counter

f = open(sys.argv[1], "r")
all_lines = f.readlines()
corpus_words_count = 0
corpus_list = []

for line in all_lines:
    line = line.strip()
    words_in_lines = line.lower().split(' ')
    for i in range(len(words_in_lines)):
        words_in_lines[i] = words_in_lines[i].split('_')[0]
    corpus_words_count += len(words_in_lines)
    corpus_list.append(words_in_lines)

unigram_count = dict(Counter([item for sub_list in corpus_list for item in sub_list]))
unique_words_in_corpus = len(unigram_count)
unigram_prob = {key: val / corpus_words_count for key, val in unigram_count.items()}

bigram_count = {}

for each_sentence in corpus_list:
    for index in range(1, len(each_sentence)):
        bigram_count[each_sentence[index - 1] + ' ' + each_sentence[index]] = bigram_count.get(
            each_sentence[index - 1] + ' ' + each_sentence[index], 0) + 1

bigram_prob = {}
for each_sentence in corpus_list:
    for index in range(1, len(each_sentence)):
        bigram_prob[each_sentence[index] + '|' + each_sentence[index - 1]] = bigram_count.get(
            each_sentence[index - 1] + ' ' + each_sentence[index]) / unigram_count[each_sentence[index - 1]]

print("\n\n*******Model Training**********")

print("\nUnigram Count", len(unigram_count))
# print("\nUnigram Probability", unigram_prob)
print("\nBigram Count", len(bigram_count))


# print("\nBigram Probability", bigram_prob)


def no_smoothing(input_words_list):
    no_smoothing_prob = 1
    for word in range(1, len(input_words_list)):
        if unigram_count.get(input_words_list[word - 1], -1) != -1:
            no_smoothing_prob *= (bigram_count.get(input_words_list[word - 1] + ' ' + input_words_list[word],
                                                   0)) / unigram_count.get(input_words_list[word - 1], 1)
        else:
            print(f"\nModel didn't find the word '{input_words_list[word - 1]}' during Training. Please apply smoothing. ")
    print("\n\nNo Smoothing Probability ", no_smoothing_prob)


def add_one_smoothing(input_words_list):
    no_smoothing_prob = 1
    for word in range(1, len(input_words_list)):
        no_smoothing_prob *= ((bigram_count.get(input_words_list[word - 1] + ' ' + input_words_list[word],
                                                0)) + 1) / (
                                     unigram_count.get(input_words_list[word - 1], 0) + unique_words_in_corpus)
    print("\n\nAdd-One Smoothing Probability ", no_smoothing_prob)


def good_turing_discount_smoothing(input_words_list):
    total_bigram_count = sum([val for val in bigram_count.values()])
    good_turing_prob = 1
    p_value = {}
    count_value = {}
    buckets = {}
    for key in bigram_count:
        if bigram_count[key] in buckets:
            buckets[bigram_count[key]].append(key)
        else:
            buckets[bigram_count[key]] = [key]
    p_value[0] = len(buckets[1]) / total_bigram_count

    for key in buckets:
        if key + 1 in buckets:
            count_value[key] = (key + 1) * len(buckets[key + 1]) / len(buckets[key])
        else:
            count_value[key] = 0
        p_value[key] = count_value[key] / total_bigram_count

    for index in range(1, len(input_words_list)):
        if (input_words_list[index - 1] + ' ' + input_words_list[index]) in bigram_count:
            good_turing_prob *= p_value[bigram_count[(input_words_list[index - 1] + ' ' + input_words_list[index])]]
        else:
            good_turing_prob *= p_value[0]
    print("\n\nGood Turing Smoothing Probability ", good_turing_prob)


input_word = sys.argv[2]
smoothing = int(sys.argv[3])
input_sentence_list = input_word.lower().split(' ')
if smoothing == 1:
    no_smoothing(input_sentence_list)
elif smoothing == 2:
    add_one_smoothing(input_sentence_list)
elif smoothing == 3:
    good_turing_discount_smoothing(input_sentence_list)

import nltk
source_data = open('source-data.txt', 'r')
delim = ' '
numbers_file = open('data/numbers', 'w')
noun_clause_file = open('data/noun-clause', 'w')
adj_clause_file = open('data/adj-clause', 'w')

# each headline should contain:
#   - number            (13)
#   - noun clause       (Great Ways)
#   - adjective clause  (You Can Use the NLTK Library)

for line in source_data:
    # convert to lowercase for part of speech classification
    line = line.rstrip('\n').lower()
    words = line.split(delim)
    pos_words = nltk.pos_tag(words)

    # validate input
    assert len(pos_words) >= 3

    # get the number
    num = pos_words.pop(0)[0]

    noun_clause = []
    adj_clause = []
    end_noun_clause = False

    # get the noun clause
    for pos_word in pos_words:
        word = pos_word[0]
        pos = pos_word[1]

        if not end_noun_clause:
            noun_clause.append(word)
            if pos == 'NNS' or pos == 'NNPS':
                end_noun_clause = True
        else:
            adj_clause.append(word)

    # only write out results where we have all 3 parts.
    if len(adj_clause) > 0:
        numbers_file.write(num + '\n')
        noun_clause_file.write(delim.join(noun_clause) + '\n')
        adj_clause_file.write(delim.join(adj_clause) + '\n')
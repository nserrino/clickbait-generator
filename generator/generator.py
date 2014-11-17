import random
import sys

# Helper functions

def print_usage():
    print 'usage: generator.py path_to_data_dir num_headlines_to_generate'
    sys.exit(1)

def read_data_file(file_name):
    path = '%s/%s' % (data_dir, file_name)
    f = open(path, 'r')
    data = [line.strip() for line in f.readlines()]
    f.close()
    return data

def to_title_case(phrase):
    return ' '.join([word.capitalize() for word in phrase.split()])

# Main

if len(sys.argv) != 3:
    print_usage()

data_dir = sys.argv[1]
count = int(sys.argv[2])

numbers = read_data_file('numbers')
noun_clauses = read_data_file('noun-clause')
adj_clauses = read_data_file('adj-clause')

for i in range(count):
    number = numbers[random.randrange(len(numbers))]
    noun_clause = noun_clauses[random.randrange(len(noun_clauses))]
    adj_clause = adj_clauses[random.randrange(len(adj_clauses))]

    print '%s %s %s' % (number, to_title_case(noun_clause),
        to_title_case(adj_clause))


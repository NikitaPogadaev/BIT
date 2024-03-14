#!/usr/bin/env python3

import sys
import re
import io

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
output_stream = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

p = re.compile('[^\w\s]')


for line in sys.stdin:
    lcopy = line
    try:
        lcopy.lower()
        lcopy.strip()
        id, lcopy = lcopy.split('\t', 1)
    except ValueError:
        continue
    lcopy = re.sub("[^A-Za-z\\s]", "", lcopy)
    words = re.split(r'[ \t\n\r\f\v]+', lcopy)
    bigrams = set((words[i].lower(), words[i+1].lower()) for i in range(len(words)-1))
    #print(bigrams)
    for bigram in bigrams:
        print('%s#%s' % (' '.join(bigram), 1))


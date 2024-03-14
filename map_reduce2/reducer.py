#!/usr/bin/env python3

import sys
import re
import io

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
output_stream = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

current_bigram = None
current_count = 0
bigram = None
inf = 1000000000
for line in sys.stdin:
    line = line.strip()
    words = re.split(r"#*", line)

    count = 0
    if len(words) < 2:
        continue
    bigram = words[0]
    try:
        count = int(words[1])
    except ValueError:
        continue
    if not re.match(r"^\w+\s\w+$", bigram):
        continue

    if current_bigram == None:
        current_bigram = bigram
        current_count = count
    elif current_bigram == bigram:
        current_count += count
    else:
        print('%s#%s' % (inf - current_count, current_bigram))
        current_bigram = bigram
        current_count = count

if current_bigram == bigram:
    print('%s#%s' % (inf - current_count, current_bigram))


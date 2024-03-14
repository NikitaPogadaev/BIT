#!/usr/bin/env python3

import sys
import re
import io

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
output_stream = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

inf = 1000000000
for line in sys.stdin:
    line = line.strip()
    words = re.split(r"#*", line)
    count = 0
    if len(words) < 2:
        continue

    try:
        count = inf - int(words[0])
    except ValueError:
        continue

    print('%s\t%s' % (words[1], count))


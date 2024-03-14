#!/usr/bin/env python3
import sys
import random
ids=[]
for line in sys.stdin:
    x = line.strip()
    if x:
        ids.append(x)

for line in ids[:51]:
    num_ids = random.randint(1, 5)

    random.shuffle(ids)
    print(','.join(ids[:num_ids]))

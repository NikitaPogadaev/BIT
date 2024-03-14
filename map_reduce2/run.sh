#!/usr/bin/env bash
OUT_DIR="output1"
OUT_DIR2="output2"
IN_DIR="/data/wiki/en_articles"

NUM_REDUCERS=8
hadoop fs -rm -r -skipTrash $OUT_DIR* > /dev/null
yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.name="job1" \
    -D mapreduce.job.reduces=${NUM_REDUCERS} \
    -files mapper.py,reducer.py \
    -input $IN_DIR \
    -mapper mapper.py \
    -reducer reducer.py \
    -output $OUT_DIR > /dev/null


hadoop fs -rm -r -skipTrash $OUT_DIR2* > /dev/null
yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.name="job2" \
    -D mapreduce.job.reduces=1 \
    -files mapper_sort.py,reducer_sort.py \
    -input $OUT_DIR \
    -mapper mapper_sort.py \
    -reducer reducer_sort.py \
    -output $OUT_DIR2 > /dev/null

hdfs dfs -cat ${OUT_DIR2}/part-00000 | head


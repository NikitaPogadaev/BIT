#!/usr/bin/env bash
OUT_DIR="output1"
NUM_REDUCERS=8
hadoop fs -rm -r -skipTrash $OUT_DIR* > /dev/null
yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.name="job1" \
    -D mapreduce.job.reduces=${NUM_REDUCERS} \
    -files mapper.py,reducer.py \
    -input /data/ids \
    -mapper mapper.py \
    -reducer reducer.py \
    -output $OUT_DIR > /dev/null

hdfs dfs -cat ${OUT_DIR}/part-00000 | head -n 50

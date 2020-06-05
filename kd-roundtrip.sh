#!/bin/sh
TRAIN_OFFSET=0
COUNT_TRAIN=72000
TEST_OFFSET=72000
COUNT_TEST=10000

echo "generating training data..."
bin/generate_data --data-path=ingr-model4-gen.csv --count=$COUNT_TRAIN --offset=$TRAIN_OFFSET > tmp/train4_file || exit 1

echo "generating test data..."
bin/generate_data --data-path=ingr-model4-gen.csv --count=$COUNT_TEST --offset=$TEST_OFFSET > tmp/test4_file || exit 1

echo "training..."
crf_learn -c 1 template_file tmp/train4_file ingr-model4.crfmodel || exit 1

echo "testing..."
crf_test -m ingr-model4.crfmodel tmp/test4_file > tmp/test4_output || exit 1

echo "visualizing..."
ruby visualize.rb tmp/test4_output > tmp/output4.html || exit 1

echo "evaluating..."
FN=log/`date +%s`.txt
python bin/evaluate.py tmp/test4_output > $FN || exit 1
cat $FN

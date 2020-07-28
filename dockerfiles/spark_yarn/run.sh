#!/bin/sh


set -o errexit
set -o nounset


spark-submit --master yarn --deploy-mode cluster --verbose test_spark.py
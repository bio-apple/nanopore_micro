import os,sys,re
import subprocess
import argparse


def run():
    NanoPlot - -fastq
    "$sample/reads.fastq" \
    - -summary
    "$sample/sequencing_summary.txt" \
    - -loglength - -tsv_stats \
    - o
    "batch_qc/${name}_NanoPlot"
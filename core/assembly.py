import os,sys,re
import subprocess,argparse

docker="nanopore_micro:latest"

def run(fa,outdir,prefix):

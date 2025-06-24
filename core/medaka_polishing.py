import os,sys,re
import argparse
import subprocess

docker="nanopore_micro:latest"

def run(basecalls,DRAFT,outdir):
    basecalls=os.path.abspath(basecalls)
    DRAFT=os.path.abspath(DRAFT)
    os.makedirs(outdir)
    cmd=(f'docker run --rm -v {DRAFT}:/raw_data/{DRAFT.split("/")[-1]} '
         f'-v {basecalls}:/raw_data/{basecalls.split("/")[-1]} '
         f'-v {os.path.abspath(outdir)}:/outdir/ '
         f'{docker} sh -c \'export PATH=/opt/conda/envs/medaka/bin:$PATH && '
         f'medaka_consensus -i /raw_data/{basecalls.split("/")[-1]}'
         f' -d /raw_data/{DRAFT.split("/")[-1]} -o /outdir/ -t 24\'')
    subprocess.check_call(cmd,shell=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser("\nUse medaka to create consensus sequences and variant calls from nanopore sequencing data.\n")
    parser.add_argument("-b",'--basecalls',help='nanopore base calls fasta or fastq',required=True)
    parser.add_argument("-d",'--draft',help="assembly draft genome sequence",required=True)
    parser.add_argument("-o", "--outdir", help="directory of output", default=os.getcwd())
    args=parser.parse_args()
    run(args.basecalls,args.draft,args.outdir)
import os,sys,re
import subprocess
import argparse

docker='nanopore_micro:latest'
def run(fastq,outdir,prefix,min_len=1000,percent=90,R1=None,R2=None):
    os.makedirs(outdir,exist_ok=True)
    fastq=os.path.abspath(fastq)
    cmd=f'docker run --rm -v {fastq}:/raw_data/{fastq.split("/")[-1]} -v {os.path.abspath(outdir)}:/outdir '
    if R1 and R2:
        R1 = os.path.abspath(R1)
        R2 = os.path.abspath(R2)
        cmd+=f'-v {R1}:/raw_data/{R1.split("/")[-1]} -v {R2}:/raw_data/{R2.split("/")[-1]} '
        cmd+=(f'{docker} sh -c \'export PATH=/opt/conda/bin/:$PATH && '
              f'filtlong -1 /raw_data/{R1.split("/")[-1]} -2 /raw_data/{R2.split("/")[-1]} --min_length {min_len} --keep_percent {percent} /raw_data/{fastq.split("/")[-1]} | gzip > /outdir/{prefix}.Filtlong.output.fastq.gz\'')
    else:
        cmd+=(f'{docker} sh -c \'export PATH=/opt/conda/bin/:$PATH && '
              f'filtlong --min_length {min_len} --keep_percent {percent} /raw_data/{fastq.split("/")[-1]} | gzip > /outdir/{prefix}.Filtlong.output.fastq.gz')
    subprocess.check_call(cmd,shell=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser("\nFiltlong is a tool for filtering long reads by quality.\n")
    parser.add_argument("-p1","--pe1",help="illumina R1 fastq",default=None)
    parser.add_argument("-p2", "--pe2", help="illumina R2 fastq", default=None)
    parser.add_argument("-o","--outdir",help="directory of output",default=os.getcwd())
    parser.add_argument("-p","--prefix",help="prefix of output",required=True)
    parser.add_argument("-n",'--nano',help="nanopore fastq file",required=True)
    parser.add_argument("-l", '--min_len', help="minimum length threshold", default=1000,type=int)
    parser.add_argument("-k", '--keep_percent', help="keep only this percentage of the best reads (measured by bases)", default=90,type=int)
    args=parser.parse_args()
    run(args.nano,args.outdir,args.prefix,args.min_len,args.keep_percent,args.pe1,args.pe2)

import os,sys,re
import subprocess,argparse

docker="nanopore_micro:latest"

def run(fq,kind,outdir,prefix):
    fq=os.path.abspath(fq)
    os.makedirs(outdir,exist_ok=True)
    cmd = (f'docker run --rm -v {fq}:/raw_data/{fq.split("/")[-1]} -v {os.path.abspath(outdir)}:/outdir {docker} '
           f'sh -c \'export PATH=/opt/conda/bin:$PATH && flye --out-dir /outdir/ --threads 24 ')
    if kind=="R10":
        cmd+=f'--nano-hq /raw_data/{fq.split("/")[-1]} '
    elif kind=="R9":
        cmd += f'--nano-hq /raw_data/{fq.split("/")[-1]} --read-error 0.05 '
    else:
        cmd+=f'--nano-raw /raw_data/{fq.split("/")[-1]} '
    cmd+="\'"
    print(cmd)
    subprocess.check_call(cmd,shell=True)



if __name__=="__main__":
    parser=argparse.ArgumentParser("De novo assembler for single molecule sequencing reads using repeat graphs.")
    parser.add_argument("-i",'--input',help="Input reads can be in FASTA or FASTQ format, uncompressed or compressed with gz",required=True)
    parser.add_argument("-o", "--outdir", help="directory of output", default=os.getcwd())
    parser.add_argument("-p", "--prefix", help="prefix of output", required=True)
    parser.add_argument("-k",'--kind',help="which type Oxford Nanopore",type=str,choice=['R10','R9','older'],required=True)
    args=parser.parse_args()
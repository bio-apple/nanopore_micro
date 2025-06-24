import h5py
from pathlib import Path

fast5_dir = Path("/staging/fanyucai/nanopore_micro/flowcell_20/1.9/downloads/multi_reads")
with open("output.fastq", "w") as out:
    for file in fast5_dir.glob("*.fast5"):
        try:
            with h5py.File(file, "r") as f:
                for read in f.keys():
                    try:
                        fq = f[read]["Analyses"]["Basecall_1D_000"]["BaseCalled_template"]["Fastq"][()]
                        out.write(fq.decode() + "\n")
                    except Exception:
                        print(f"FASTQ not found in {file.name}")
        except:
            print(f"Can't open {file.name}")
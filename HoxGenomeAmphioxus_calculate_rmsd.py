import os
from chimera import runCommand as rc
from chimera import replyobj
os.chdir("/home/bioinfo/workspace/genome/data/IrxA_final_output_1.2_-0.3_8000/")
rc("open IrxA1725.py")
rc("open IrxA36671.py")
rc("match #134-267 #0-133")

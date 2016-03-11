import os
from chimera import runCommand as rc
from chimera import replyobj
os.chdir("/home/bioinfo/workspace/genome/data/wnt_final_output_0.2_-0.2_25000/")
rc("open wnt2026.py")
rc("open wnt4803.py")
rc("match #166-331 #0-165")

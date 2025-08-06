# merge_code_dump.py  –  run from project root

from pathlib import Path
from PyPDF2 import PdfMerger           # ships with Anaconda; pip install PyPDF2 if missing

pdf_dir   = Path("code_dump")          # folder holding the individual PDFs
out_file  = Path("code_dump.pdf")      # single combined PDF at project root

# order of notebooks in the final document
pdf_order = [
    "ex1_1_detect.pdf",
    "ex1_2_count.pdf",
    "ex2_audio_codec.pdf",
    "ex3_video_qc.pdf",
]

merger = PdfMerger()
for name in pdf_order:
    merger.append(pdf_dir / name)

merger.write(out_file)
merger.close()
print("Merged →", out_file.resolve())

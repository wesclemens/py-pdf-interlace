import sys
import argparse
import itertools
from pdfrw import PdfWriter, PdfReader

parser = argparse.ArgumentParser(description='Interlaces two pdf to make one complete pdf.')
parser.add_argument('front_pdf_loc', type=str, help="PDF of fronts of pages")
parser.add_argument('back_pdf_loc', type=str, help="PDF of backs of pages")
parser.add_argument('output_loc', type=str, nargs='?', default="output.pdf",
        help="Output location for interlaced PDF")

args = parser.parse_args()

output = PdfWriter()
front_pdf = PdfReader(args.front_pdf_loc)
back_pdf = PdfReader(args.back_pdf_loc)

if len(front_pdf.pages) != len(back_pdf.pages):
    print("PDFs must have the same number of pages")
    sys.exit(1)

output.addpages(itertools.chain.from_iterable(zip(front_pdf.pages, back_pdf.pages[::-1])))
output.write(args.output_loc)

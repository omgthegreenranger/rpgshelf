from xmptools import XMPMetadata, XMPParser, XMPSerializer
import pdfminer
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import pdfminer.pdfinterp
from fs.osfs import OSFS
import os

def pdfsearch():
    file_dir = OSFS("../testfiles/originals")
    print(file_dir.listdir('/'))
    num_file = []

    print("Select title to search for:\n-----------------\n")

    for i,n in enumerate(file_dir.listdir('/')):
        print(i, n)
        num_file.append([i, n])
            #Parse internal metadata
            # pdf_info = PDFParser(pdfread_doc)
            # pdf_set = PDFDocument(pdf_info)
        
            # pdf_meta = XMPParser.parse(pdfread_doc)
            # print(pdf_meta)

            # Grab title for search
            # pdfread_doc.

    select = input("Make selection now:")
    num_file_selected = num_file[int(select)]



    # print(num_file)
    file_name = os.path.splitext(num_file_selected[1])
    print(file_name[0])

    import string
 
    file_stripped = file_name[0].translate(str.maketrans('','',string.punctuation))
    print(file_stripped)
    global qsearchterms
    qsearchterms = file_stripped

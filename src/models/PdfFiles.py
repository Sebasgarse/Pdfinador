from shutil import rmtree
from os import listdir, mkdir
from os.path import join, exists

from .FilesSorter import FilesSorter

class PdfFiles:
    def __init__(self, parent):
        self.parent = parent
        self.sort = FilesSorter(self)

        self.get_all_files()
        self.create_pdf_directory()

    def get_all_files(self):
        self.files =  [
            file for file 
            in listdir(self.parent.dir) 
            if file.lower().endswith('.jpg') 
            or file.lower().endswith('.png') 
            or file.lower().endswith('.jpeg')
            or file.lower().endswith('.webp')
        ]
    
    def create_pdf_directory(self):
        self.pdf_dir = join(self.parent.dir, "pdf")

        if exists(self.pdf_dir):
            rmtree(self.pdf_dir)

        mkdir(self.pdf_dir)

    def sort_by_number(self):
        self.files = self.sort.by_number(self.files)

    def get(self):
        return self.files

    def get_pdf_dir(self):
        return self.pdf_dir
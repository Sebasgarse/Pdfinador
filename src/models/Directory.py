from os.path import basename
from os.path import join

from .PdfFiles import PdfFiles 

class Directory:
    def __init__(self, dir, directory = None) -> None:
        self.dir = dir

        if directory == None:
            self.directory = dir
        else:
            self.directory = directory

        self.files = PdfFiles(self)
        self.files.sort_by_number()

        self.name = basename(dir)
        self.full_directory_path = join(self.directory, self.name)

    def has_no_files(self):
        return len( self.files.get() ) == 0

    def get_path(self):
        return self.dir

    def get_full_path(self):
        return self.full_directory_path
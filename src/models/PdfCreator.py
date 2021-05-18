from PyPDF2 import PdfFileReader
from PIL import Image
from os.path import join

class PdfCreator:
    def __init__(self, parent, image_file, directory):
        self.parent = parent
        self.files = []
        self.image_file = image_file
        self.directory = directory
        
    def get_pages(self):
        self.initialize_variables()
        self.save_image()
        self.set_reader()
        return self.get_pages_from_reader()

    def initialize_variables(self):
        self.archive_name = join( self.directory.files.get_pdf_dir(), self.image_file )
        self.archive_name = self.archive_name + '.pdf'

        image_path = join(self.directory.get_path(), self.image_file)
        self.image = Image.open( image_path )

    def save_image(self):
        try:
            self.image.save(self.archive_name, 'PDF', resoultion = 100.0)
        except ValueError as _:
            self.convert_rgb()

    def convert_rgb(self):
        rgb_im = self.image.convert("RGB")
        rgb_im.save(self.archive_name, 'PDF', resoultion = 100.0)
        self.parent.add_error('El archivo: %s, poseía alpha, removido para añadir a pdf' % self.image_file)

    def set_reader(self):
        pdf = open(self.archive_name, 'rb')
        self.parent.add_file(pdf)
        self.reader = PdfFileReader(pdf)
        
    def get_pages_from_reader(self):
        pages = []
        for page in range(self.reader.numPages):
            page_ = self.reader.getPage(page)
            pages.append(page_)
        return pages



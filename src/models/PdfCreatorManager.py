from .Directory import Directory
from .PdfCreator import PdfCreator
from PyPDF2 import PdfFileWriter

class PdfCreatorManager:
    def __init__(self):
        self.directories = []

    def add_directory(self, dir, directory = None):
        directory = Directory(dir, directory)
        self.directories.append(directory)
    
    def execute(self):
        for directory in self.directories:
            self.set_directory = directory
            self.create_pdf()

    def create_pdf(self):
        if self.set_directory.has_no_files():
            return

        self.initialize_variables()
        self.process_images()
        self.create_pdf_file_result()
        self.close_files()
        self.print_last_message()

    def initialize_variables(self):
        self.archive_count = 0

        self.errors = []
        self.files = []

        self.writer = PdfFileWriter()

    def process_images(self):
        for image_file in self.set_directory.files.get():
            pages = self.get_pdf_pages(image_file)
            self.set_pages_to_writer(pages)
            self.archive_count += 1
            self.print_complete_text()

    def get_pdf_pages(self, image_file):
        pdfCreator = PdfCreator( self, image_file, self.set_directory )
        return pdfCreator.get_pages()

    def set_pages_to_writer(self, pages):
        for page in pages:
            self.writer.addPage(page)


    def print_complete_text(self):
        archive_max_count = len(self.set_directory.files.get())
        percent = 100 * ( self.archive_count / archive_max_count )
        percent = int(percent)
        complete_text = '\rCompletado ' + str(percent) + '%'
        print(complete_text, end='', flush=True)

    def create_pdf_file_result(self):
        final = open(self.set_directory.get_full_path() + '.pdf', 'wb')
        self.writer.write(final)
        final.close()

    def print_last_message(self):
        if len(self.errors) == 0:
            print("\nPdf creado sin problemas")
        else:
            print('\nSe presentaron los siguientes errores:')
            [
                print(error) 
                for error 
                in self.errors
            ]

    def close_files(self):
        for file in self.files:
            file.close()
        self.set_directory.files.remove_pdf_directory()

    def add_error(self, error):
        self.errors.append(error)

    def add_file(self, file):
        self.files.append(file)
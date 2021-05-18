import os, codecs, sys

from os.path import join

from src.models import PdfCreatorManager

def one():
    print("Escriba la direccion de la carpeta:")
    directory = input()
    if os.path.exists(directory) and os.path.isdir(directory):
        pdfCreatorManager.add_directory(directory)
    else:
        print('Carpeta no existe')
        return one()
        
def many():
    print("Escriba la direccion de la carpeta:")
    directory = input()
    if os.path.exists(directory) and os.path.isdir(directory):
        directories = [n for n in os.listdir(directory) if os.path.isdir(join(directory, n))]
    else:
        print('Carpeta no existe') 
        return many()
    for dir in [join(directory, n) for n in directories if n + ".pdf" not in os.listdir(directory)]:
        pdfCreatorManager.add_directory(dir, directory)
        
    
if __name__ == '__main__':
    # Esto cambia el enconding de print a utf-8
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    if sys.stderr.encoding != 'utf-8':
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    # Empieza el programa
    pdfCreatorManager = PdfCreatorManager()
    print("1)One archive \n2)Many")
    mode = input("Choose mode:")
    if mode == "1":
        one()
    if mode == "2":
        many()
    pdfCreatorManager.execute()
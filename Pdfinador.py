import os, PyPDF2, re, codecs, sys
from shutil import rmtree
from PIL import Image
from os.path import join

def one():
    print("Escriba la direccion de la carpeta:")
    directory = input()
    if os.path.exists(directory) and os.path.isdir(directory):
        pdfing(directory)
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
        pdfing(dir, directory)
        
def pdfing(dir, directory = None):
    archives = [n for n in os.listdir(dir) if n.endswith('.jpg') 
                                                or n.endswith('.png') 
                                                or n.endswith('.jpeg')
                                                or n.endswith('.webp')]
    
    archives = integer_converter(archives)
                                                
    i = 0
    if directory == None:
        directory = dir
    pdfDir = join(dir, "pdf")
    if os.path.exists(pdfDir):
        rmtree(pdfDir)
    os.mkdir(pdfDir)
    
    writer = PyPDF2.PdfFileWriter()
    
    files = []
    if len(archives) == 0:
        return
    nombre = os.path.basename(dir)
    fullDir = join(directory, nombre)
    errors = []
    print (nombre)
    for imagen in archives:
        archive = join(pdfDir, imagen) + '.pdf'
        im = Image.open(join(dir, imagen))
        try:
            im.save(archive, 'PDF', resoultion = 100.0)
        except ValueError as ve:
            rgb_im = im.convert("RGB")
            rgb_im.save(archive, 'PDF', resoultion = 100.0)
            errors.append('El arhivo: %s, poseia alpha, removido para añadir a pdf' % imagen)
        pdf = open(archive, 'rb')
        files.append(pdf)
        reader = PyPDF2.PdfFileReader(pdf)
        for pagina in range(reader.numPages):
            page = reader.getPage(pagina)
            writer.addPage(page)
        i += 1
        print('\rCompletado ' + str(int(100 * (i / len(archives)))) + '%',end='',flush=True)
    final = open(fullDir + '.pdf', 'wb')
    writer.write(final)
    final.close()
    for file in files:
        file.close()
    rmtree(pdfDir)
    if len(errors) == 0:
        print("\nPdf creado sin problemas")
    else:
        print('\nSe presentaron los siguientes errores:')
        [print(n) for n in errors]
        
        
def integer_converter(values):
    mapa = {}
    numeros = re.compile(r'\d+')
    for value in values:
        numbers = numeros.findall(value)
        if len(numbers) == 0:
            mapa[value] = value
        elif len(numbers) == 1:
            mapa[numbers[0]] = value
        elif len(numbers) == 2:
            mapa[numbers[1]] = value
        else:
            mapa[numbers[len(numbers) - 1]] = value
    list = []
    for number in sorted(mapa):
        list.append(mapa[number])
    return list
    
if __name__ == '__main__':
    # Esto cambia el enconding de print a utf-8
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    if sys.stderr.encoding != 'utf-8':
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    # Empieza el programa
    print("1)One archive \n2)Many")
    mode = input("Choose mode:")
    if mode == "1":
        one()
    if mode == "2":
        many()
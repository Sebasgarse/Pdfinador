import os, PyPDF2, re, shutil
from PIL import Image

def inicio():
    print("Escriba la direccion de la carpeta")
    carpeta = input()
    if os.path.exists(carpeta) and os.path.isdir(carpeta):
        archivos = [n for n in os.listdir(carpeta) if n.endswith('.jpg') 
                                                    or n.endswith('.png') 
                                                    or n.endswith('.jpeg')]
        archivos.sort()
                                                    
        os.chdir(carpeta)
        i = 0
        os.mkdir("pdf")
        
        writer = PyPDF2.PdfFileWriter()
        
        formato = re.compile(r'.jpg|.png|.jpeg')
        
        files = []
        for imagen in archivos:
            archivo = 'pdf\\' + formato.sub('', imagen) + '.pdf'
            im = Image.open(imagen)
            im.save(archivo, 'PDF', resoultion = 100.0)
            pdf = open(archivo, 'rb')
            files.append(pdf)
            reader = PyPDF2.PdfFileReader(pdf)
            for pagina in range(reader.numPages):
                page = reader.getPage(pagina)
                writer.addPage(page)
            i += 1
            print('Completado ' + str(int(100 * (i / len(archivos)))) + '% \r',end='',flush=True)
        final = open(os.path.basename(carpeta) + '.pdf', 'wb')
        writer.write(final)
        final.close()
        for file in files:
            file.close()
        shutil.rmtree("pdf")
        
    else:
        print('Carpeta no existe')
        inicio()
        

if __name__ == '__main__':
    inicio()
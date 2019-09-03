import os, PyPDF2, re
from PIL import Image

def inicio():
    print("Escriba la direccion de la carpeta")
    carpeta = input()
    if os.path.exists(carpeta) and os.path.isdir(carpeta):
        archivos = [n for n in os.listdir(carpeta) if n.endswith('.jpg') 
                                                    or n.endswith('.png') 
                                                    or n.endswith('.jpeg')]
                                                    
        os.chdir(carpeta)
        i = 0
        os.mkdir("pdf")
        formato = re.compile(r'.jpg|.png|.jpeg')
        for imagen in archivos:
            im = Image.open(imagen)
            im.save('pdf\\' + formato.sub('', imagen) + '.pdf', 'PDF', resoultion = 100.0)
            i += 1
            print('Completado ' + str(int(100 * (i / len(archivos)))) + '% \r',end='',flush=True)
        
        
    else:
        print('Carpeta no existe')
        inicio()
        

if __name__ == '__main__':
    inicio()
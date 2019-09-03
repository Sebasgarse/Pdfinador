import os, PyPDF2, docx
from PIL import Image
from lxml import etree

def inicio():
    print("Escriba la direccion de la carpeta")
    carpeta = input()
    if os.path.exists(carpeta) and os.path.isdir(carpeta):
        archivos = [n for n in os.listdir(carpeta) if n.endswith('.jpg') 
                                                    or n.endswith('.png') 
                                                    or n.endswith('.jpeg')]
                                                    
        os.chdir(carpeta)
        doc = docx.Document()
        i = 0
        for imagen in archivos:
            width, height = Image.open(imagen).size
            doc.add_picture(imagen, width=docx.shared.Inches(8.5), height=docx.shared.Inches(11))
            i += 1
            print('Completado ' + str(int(100 * (i / len(archivos)))) + '% \r',end='',flush=True)
        
        sections = doc.sections
        for section in sections:
            section.bottom_margin = 0
            section.left_margin = 0
            section.right_margin = 0
            section.top_margin = 0

        doc.save(os.path.basename(carpeta) + '.docx')
        
    else:
        print('Carpeta no existe')
        inicio()
        

if __name__ == '__main__':
    inicio()
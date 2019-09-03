import os, PyPDF2, docx

def inicio():
    print("Escriba la direccion de la carpeta")
    carpeta = input()
    if os.path.exists(carpeta) and os.path.isdir(carpeta):
        archivos = [n for n in os.listdir(carpeta) if n.endswith('.jpg') 
                                                    or n.endswith('.png') 
                                                    or n.endswith('.jpeg')]
                                                    
        #archivo = open(carpeta + '\\' + os.path.basename(carpeta) + '.docx', 'w')
        #archivo.close()
        os.chdir(carpeta)
        doc = docx.Document()
        doc.add_paragraph('hola')
        doc.add_page_break()
        doc.add_picture(archivos[0])
        doc.save(os.path.basename(carpeta) + '.docx')
        print(archivos)
        
    else:
        print('Carpeta no existe')
        inicio()
        
        
if __name__ == '__main__':
    inicio()
import os, PyPDF2, docx

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
            doc.add_picture(imagen)
            doc.add_page_break()
            i += 1
            print('Completado ' + str(int(100 * (i / len(archivos)))) + '% \r',end='',flush=True)
            
        doc.save(os.path.basename(carpeta) + '.docx')
        
    else:
        print('Carpeta no existe')
        inicio()
        
        
if __name__ == '__main__':
    inicio()
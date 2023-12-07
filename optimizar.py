from PIL import Image
from pathlib import Path
import os
import shutil

def optimizar_Pillow(image,name,rootdir):
    #image=Image.open('C:/Users/eadel/OneDrive/Desktop/media/Europa.jpg')
    
    quality= 50
    print(f'el tamaño es {image.size} ')
    #print("File Size In Bytes:- "+str(len(image.fp.read())))
    largo=image.size[0]
    ancho=image.size[1]
    #print(f'el tipo de dato de ancho es {type(ancho)}')
    reducida = image.resize((largo, ancho))
    reducida.save(f"{rootdir}\\{name}", optimize=True, quality=quality)
   
    #image.save(f'{rootdir}\\{name}', optimize=True, quality=quality)

"""
print(f'os.system\n {os.system("dir")}') #listar archivos y carpetas del directorio actual
print(f'DIRECTORIO ACTUAL os.getcwd\n {os.getcwd()}') #mostrar el directorio actual
directorioActual=os.listdir(".")
print(f'ELEMENTOS DIRECTORIO ACTUAL os.listdir\n {directorioActual}') #listar archivos y carpetas del directorio actual
for archivo in directorioActual:
    is_dir=os.path.isdir(archivo)
    print(f'{archivo} : {is_dir}')"""
# print(f'os.chdir\n{os.chdir("/home/user/documents")}') #cambiar
# print(f'os.path.dirname\n {os.path.dirname(__file__)}') #
#os.makedirs('mantenimiento/avances') #para crar directorios, solo se deben crear en caso de no existir, si exiten marca error

 
def navegarDirectorio(rootdir):
    for rootdir, dirs, files in os.walk(rootdir):
        for subdir in dirs:
            print(os.path.join(rootdir, subdir))
        for subfile in files:
            path=os.path.join(rootdir, subfile)
            peso=os.path.getsize(path)
            print(path)
            print(f'peso del archivo {peso} bits')

            #print(len(subfile))
            #if len(subfile)>4:
            #    ext=subfile[4:]
                #   print(ext)
            print(subfile)
            if ('.jpg' in subfile) or ('.jpeg' in subfile):
                try:
                    imagen = Image.open(os.path.join(rootdir, subfile))
                    
                    print(f'se aplica optimizacion a: {subfile}')
                    print(rootdir)
                    #print(NewRootdir)#aca debo ingresar el directorio de la imagen en la nueva ruta raiz
                                    #verifico si existe la nueva ruta o en dado caso la creo
                    optimizar_Pillow(imagen,subfile,rootdir)
                except:
                    print(f'no fue posible optimizar archivo: {subfile}')
                
            else:
                print(f'no es una imagen: {subfile}')

pathCarpetaOrigen="media_backup"
pathCarpetaDestino="media_optimizado"
media_backup=os.path.exists(pathCarpetaDestino)
print(media_backup)#comprueba si existe un archivo
if media_backup== False:
    shutil.copytree(pathCarpetaOrigen,pathCarpetaDestino) #copia directorios completos con archivos y todo
    
#rootdir = 'C:/Users/eadel/OneDrive/Documents/VISUAL_STUDIO_PROJECTS/LEARNING_PROJECTS/OPTIMIZE_IMAGE'
#NewRootdir= 'C:\\Users\\eadel\\OneDrive\\Desktop\\media_results'
directorio_Actual=os.getcwd()
RutaDestino=directorio_Actual+"\\"+pathCarpetaDestino
#print(f'os.path.dirname\n {os.getcwd()}')
#print(RutaDestino)
#NewRootdir= 'C:\\Users\\eadel\\OneDrive\\Documents\\VISUAL_STUDIO_PROJECTS\\LEARNING_PROJECTS\\OPTIMIZE_IMAGE\\media_backup'
#listdirs(rootdir)
#print(NewRootdir)
navegarDirectorio(RutaDestino)
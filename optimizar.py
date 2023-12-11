from PIL import Image
from pathlib import Path
import os
import shutil
import platform

def optimizar_Pillow(image,name,rootdir,peso):
    #image=Image.open('C:/Users/eadel/OneDrive/Desktop/media/Europa.jpg')
    
    quality= 50
    #print(f'El tamaño de {name} es {image.size} y el peso {peso} [bytes]')
    
    #print("File Size In Bytes:- "+str(len(image.fp.read())))
    largo=image.size[0]
    ancho=image.size[1]
    
    if largo > 1080:
        nuevolargo = 1080
        ratio=(nuevolargo/largo)
        print(f'Para {name}La tasa de reduccion es {ratio} largo:{nuevolargo} ancho:{int(ancho*ratio)}\n')
        reducida = image.resize((nuevolargo, int(ancho*ratio)))
        #reducida.save(f"{rootdir}\\{name}")
        reducida.save(f"{rootdir}\\{name}", optimize=True, quality=quality)
    elif ancho > 1080:
        nuevoAncho = 1080
        ratio=(nuevoAncho/ancho)
        print(f'Para {name}La tasa de reduccion es {ratio} largo:{int(largo*ratio)} ancho:{nuevoAncho}\n')
        reducida = image.resize((int(largo*ratio), nuevoAncho))
        #reducida.save(f"{rootdir}\\{name}")
        reducida.save(f"{rootdir}\\{name}", optimize=True, quality=quality)
    else:
        #print(f'el tipo de dato de ancho es {type(ancho)}')
        print(f'Para {name}no se aplica reduccion {largo} ancho:{ancho}\n')
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
    for rootdir, dirs, files in os.walk(rootdir,onerror=None):
        for subdir in dirs:
            path=os.path.join(rootdir, subdir)
            #print(path)
        for subfile in files:
            path=os.path.join(rootdir, subfile)
            peso=os.path.getsize(path)
            #print(path)
            #print(f'peso del archivo {peso} bytes')

            #print(len(subfile))
            #if len(subfile)>4:
            #    ext=subfile[4:]
                #   print(ext)
            print(subfile)
            if ('.jpg' in subfile) or ('.jpeg' in subfile) or ('.jfif' in subfile) or ('.png' in subfile):
                try:
                    imagen = Image.open(os.path.join(rootdir, subfile))
                    
                    #print(f'se aplica optimizacion a: {subfile}')
                    #print(rootdir)
                    #print(NewRootdir)#aca debo ingresar el directorio de la imagen en la nueva ruta raiz
                                    #verifico si existe la nueva ruta o en dado caso la creo
                    optimizar_Pillow(imagen,subfile,rootdir,peso)
                except:
                    print(f'no fue posible optimizar archivo: {subfile}')
                
            else:
                print(f'No es una imagen: {subfile}\n')


def limpiar_pantalla():
    so=platform.system() #sistema operativo
    if so=="Windows": #si es windows
        os.system("cls")
    elif os== 'linux': #si es linux
        os.system("clear") 


def directorio_verificado(path):
            intentos=0
            existe_directorio=os.path.exists(path)
            while existe_directorio==False:
                intentos +=1 
                if existe_directorio == True:
                    print(f"se procede a copiar {path}")
                    path= path#salimos del bucle
                    break
                if intentos==3:
                    print(f'Supera el maximo de intentos {intentos}')
                    path= 'NOEXISTE'
                    break
                else:
                    print(f"No existe, el directorio ingresado: ")
                    path=input("Ingresar nombre de directorio: ")
                    existe_directorio=os.path.exists(path)
                print()
            
            return path
### ### ### MAIN ### ### ### ### ### ### ### ### ### ###
if __name__ == '__main__':
    limpiar_pantalla()
    print("############# INICIANDO PROGRAMA ############################### \n")
    print("############# 1. CREAR UN BACK UP ##############################  ")
    crearCopia=input("Desea cear un backup de algún directorio?\n yes or not :")
    if crearCopia=='yes' or crearCopia.lower()=='yes':
        print('\n1.1. Debe ingresar la ruta del directorio de origen:')
        print('Ej. Dir externo: ruta. C:\\Users\\eadel\\OneDrive\\Desktop\\PILDORAS_DJANGO')
        print('Ej. Dir actual: media_backup')
        pathCarpetaOrigen=input("Ingresar nombre de directorio origen: ")
        #pathCarpetaOrigen="media_backup"
        
        directorioOrigen_Verificado=directorio_verificado(pathCarpetaOrigen)
        if directorioOrigen_Verificado== 'NOEXISTE':
            print(f'\nError!: No fue posible crear backup a Directorio\n{pathCarpetaOrigen}')
        else:
            pathCarpetaOrigen=directorioOrigen_Verificado
            print(f'\nok: El nombre del directorio origen es:\n{pathCarpetaOrigen}')
            pathCarpetaDestino=input("Ingresar nombre de directorio destino: ")
            #existe_directorio=exite_dir(path=pathCarpetaDestino)
            #if existe_directorio== True:
            try:
                shutil.copytree(pathCarpetaOrigen,pathCarpetaDestino)
                print(f"ok: El directorio se encuentra la ruta actual folder :\n{pathCarpetaDestino} ")
            except:
                print(f'Error!: No fue posible crear backup a {pathCarpetaOrigen}')
    print("\n\n############# 2. OPTIMIZAR IMAGENES DE DIRECTORIO ############### ")
    optimizarDirectorio=input("Desea optimizar imagenes de algun directorio?\n yes or not :")
    if optimizarDirectorio=='yes' or optimizarDirectorio.lower()=='yes':
        print('\n2.1. Debe ingresar la ruta del directorio de origen:')
        print('Ej. Dir externo: ruta. C:\\Users\\eadel\\OneDrive\\Desktop\\PILDORAS_DJANGO')
        print('Ej. Dir actual: media_optimizado')
        pathCarpetaOrigen=input("Ingresar nombre de directorio origen: ")
        directorioOrigen_Verificado=directorio_verificado(pathCarpetaOrigen)
        if directorioOrigen_Verificado== 'NOEXISTE':
            print('EL DIRECTORIO NO EXISTE')
        elif directorioOrigen_Verificado== 'media_backup':
            print('CARPETA media_backup REFERENCIA')
        elif directorioOrigen_Verificado== 'optimizar':
            print('CARPETA ENTORNO VIRTUAL')
        else:
            pathCarpetaOrigen=directorioOrigen_Verificado
            directorio_Actual=os.getcwd()
            RutaDestino=directorio_Actual+"\\"+pathCarpetaOrigen
            navegarDirectorio(RutaDestino)
            #pseo_dir_origen=os.path.getsize(pathCarpetaOrigen)
            #pseo_dir_destino=os.path.getsize(RutaDestino)
            #print(f'El tamaño del directorio origen es {pseo_dir_origen} dir destino {pseo_dir_destino}')
    #pathCarpetaDestino="media_optimizado"a
"""
existe_directorio=os.path.exists(pathCarpetaDestino)
#print(media_backup)#comprueba si existe un archivo
if existe_directorio== False:
    shutil.copytree(pathCarpetaOrigen,pathCarpetaDestino) #copia directorios completos con archivos y todo
    
#rootdir = 'C:/Users/eadel/OneDrive/Documents/VISUAL_STUDIO_PROJECTS/LEARNING_PROJECTS/OPTIMIZE_IMAGE'
#NewRootdir= 'C:\\Users\\eadel\\OneDrive\\Desktop\\PILDORAS_DJANGO'
directorio_Actual=os.getcwd()
RutaDestino=directorio_Actual+"\\"+pathCarpetaDestino
#print(f'os.path.dirname\n {os.getcwd()}')
#print(RutaDestino)
#NewRootdir= 'C:\\Users\\eadel\\OneDrive\\Documents\\VISUAL_STUDIO_PROJECTS\\LEARNING_PROJECTS\\OPTIMIZE_IMAGE\\media_backup'
#listdirs(rootdir)
#print(NewRootdir)
navegarDirectorio(RutaDestino)"""
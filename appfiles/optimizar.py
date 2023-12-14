from PIL import Image
import os
import shutil
import platform
so=platform.system() #sistema operativo
    

def optimizar_Pillow(image,name,rootdir,path):
    quality= 90
    limite_pixeles=1280
    largo=image.size[0]
    ancho=image.size[1]
    peso=os.path.getsize(path)
    if peso >400000:
        if largo > limite_pixeles:
            nuevolargo = limite_pixeles
            ratio=(nuevolargo/largo)
            x = round(ratio, 4)
            print(f'Para {name} peso:{peso}[Bytes]\nLargo. Reduccion: {x*100}[%] - largo:{nuevolargo}[px] - ancho:{int(ancho*ratio)}[px]\n')
            reducida = image.resize((nuevolargo, int(ancho*ratio)))
            if so=="Windows": #si es windows
                print(f'salida1 {name} peso {os.path.getsize(path)}')
                reducida.save(f"{rootdir}/{name}", optimize=True, quality=quality)
                if os.path.getsize(path) >peso:
                    print('#### NO SE GUARDA')
                
            elif os== 'Linux': 
                reducida.save(f"{rootdir}/{name}", optimize=True, quality=quality)
        elif ancho > limite_pixeles:
            nuevoAncho = limite_pixeles
            ratio=(nuevoAncho/ancho)
            x = round(ratio, 4)
            print(f'Para {name} peso:{peso}[Bytes]\nAncho. Reduccion: {x*100}[%] - largo:{(int(largo*ratio))}[px] - ancho:{int(ancho*ratio)}[px]\n')
            reducida = image.resize((int(largo*ratio), nuevoAncho))
            if so=="Windows": #si es windows
                reducida.save(f"{rootdir}\\{name}", optimize=True, quality=quality)
                print(f'salida1 {name} peso {os.path.getsize(path)}')
                if os.path.getsize(path) >peso:
                    print('#### NO SE GUARDA')
               
            elif so== 'Linux': 
                reducida.save(f"{rootdir}/{name}", optimize=True, quality=quality)
        else:
            print(f'Para {name} peso:{peso}[Bytes]\nPeso. Se optimiza peso al  90% \nConservan largo:{largo}[px] ancho:{ancho}[px]\n')
            #reducida = image.resize((largo, ancho))
            if so=="Windows": #si es windows
                #reducida.save(f"{rootdir}\\{name}", optimize=True, quality=quality)
                print(f'salida1 {name} peso {os.path.getsize(path)}')
                if os.path.getsize(path) >peso:
                    print('#### NO SE GUARDA')
                
            elif so== 'Linux': 
                print('ok')
                #reducida.save(f"{rootdir}/{name}", optimize=True, quality=quality)
            
        print(f'salida2 {name} peso {os.path.getsize(path)}')
        """if peso >400000:
        #else:
            print(f'Para {name} peso:{peso}[Bytes]\nPeso. Se optimiza peso al  50% \nConservan largo:{largo}[px] ancho:{ancho}[px]\n')
            reducida = image.resize((largo, ancho))
            reducida.save(f"{rootdir}\\{name}", optimize=True, quality=quality)"""
   
 
def navegarDirectorio(rootdir):
    print(f'\n############# 2.2 INICIANDO OPTIMIZACION ###############################') 
    for rootdir, dirs, files in os.walk(rootdir,onerror=None):
        for subdir in dirs:
            path=os.path.join(rootdir, subdir)
        for subfile in files:
            path=os.path.join(rootdir, subfile)
            #peso=os.path.getsize(path)
            print(subfile)
            if ('.jpg' in subfile) or ('.jpeg' in subfile) or ('.jfif' in subfile) or ('.png' in subfile):
                try:
                    imagen = Image.open(os.path.join(rootdir, subfile))
                    optimizar_Pillow(imagen,subfile,rootdir,path)
                except:
                    print(f'No fue posible optimizar archivo: {subfile}')                
            else:
                print(f'{subfile} No es una imagen\n')
    


def limpiar_pantalla():
    #so=platform.system() #sistema operativo
    if so=="Windows": #si es windows
        os.system("cls")
    elif so== 'Linux': #si es linux
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
    if crearCopia!='yes' and crearCopia.lower()!='yes' and crearCopia!='not' and crearCopia.lower()!='not' :
        print('error!: Respuesta incorrecta ultimo intento ')
        crearCopia=input("Desea cear un backup de algún directorio?\n yes or not :")
        
    if crearCopia=='yes' or crearCopia.lower()=='yes':
        so=platform.system() #sistema operativo
        print(f'\n1.1. Debe ingresar la ruta del directorio de origen:{so}') 
        if so=="Windows": #si es windows
            print(f'Ej. path  : {os.getcwd()}\\mi_directorio_origen')
        elif so== 'Linux': #si es linux
            print(f'Ej. path  : {os.getcwd()}/mi_directorio_origen')   
        
        print(f'Ej. Relative path : mi_directorio_origen')
        pathCarpetaOrigen=input("Ingresar nombre de directorio origen: ")        
        directorioOrigen_Verificado=directorio_verificado(pathCarpetaOrigen)

        if directorioOrigen_Verificado== 'NOEXISTE':
            print(f'\nError!: No fue posible crear backup a Directorio\n{pathCarpetaOrigen}')
        else:
            pathCarpetaOrigen=directorioOrigen_Verificado
            print(f'\nok: El nombre del directorio origen es:\n{pathCarpetaOrigen}')
            pathCarpetaDestino=input("Ingresar nombre de directorio destino: ")
            try:
                shutil.copytree(pathCarpetaOrigen,pathCarpetaDestino)
                if so=="Windows": #si es windows
                    print(f"\nOk: El directorio destino se encuentra la ruta:\n {os.getcwd()}\\{pathCarpetaDestino} ")
                elif so== 'Linux': #si es linux
                    print(f"\nOk: El directorio destino se encuentra la ruta:\n {os.getcwd()}/{pathCarpetaDestino} ")
            except:
                print(f'Error!: No fue posible crear backup a {pathCarpetaOrigen}')
    
    

    print("\n\n############# 2. OPTIMIZAR IMAGENES DE DIRECTORIO ############### ")
    optimizarDirectorio=input("Desea optimizar imagenes de algun directorio?\n yes or not :")
    if optimizarDirectorio!='yes' and optimizarDirectorio.lower()!='yes' and optimizarDirectorio!='not' and optimizarDirectorio.lower()!='not' :
        print('error!: Respuesta incorrecta ultimo intento ')
        optimizarDirectorio=input("Desea cear un backup de algún directorio?\n yes or not :")
        
    if optimizarDirectorio=='yes' or optimizarDirectorio.lower()=='yes':
        if so=="Windows": #si es windows
            print(f'Ej. path  : {os.getcwd()}\\mi_directorio_origen')
        elif so== 'Linux': #si es linux
            print(f'Ej. path  : {os.getcwd()}/mi_directorio_origen')

        print(f'Ej. Relative path : mi_directorio_origen')
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
            #directorio_Actual=os.getcwd()
            #RutaDestino=directorio_Actual+"\\"+pathCarpetaOrigen
            #navegarDirectorio(RutaDestino)
            navegarDirectorio(pathCarpetaOrigen)
            print(f'\n############# 2.3 FINALIZA OPTIMIZACION ###############################')
            print(f'Revisar directorio: {pathCarpetaOrigen}')
            
from PIL import Image
import os
import shutil
import platform
so=platform.system() 
    
def optimizarImagenPillow(image,name,rootdir,path):
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
            reducida = image.resize((nuevolargo, int(ancho*ratio)))
            if so=="Windows": 
                reducida.save(f"{rootdir}/{name}", optimize=True, quality=quality)
            elif so== 'Linux': 
                reducida.save(f"{rootdir}/{name}", optimize=True, quality=quality)
        elif ancho > limite_pixeles:
            nuevoAncho = limite_pixeles
            ratio=(nuevoAncho/ancho)
            x = round(ratio, 4)
            reducida = image.resize((int(largo*ratio), nuevoAncho))
            if so=="Windows": 
                reducida.save(f"{rootdir}\\{name}", optimize=True, quality=quality)
            elif so== 'Linux': 
                reducida.save(f"{rootdir}/{name}", optimize=True, quality=quality)
        else:
            x=0
            reducida = image.resize((largo, ancho))
            if so=="Windows": 
                reducida.save(f"{rootdir}\\{name}", optimize=True, quality=quality)                
            elif so== 'Linux': 
                reducida.save(f"{rootdir}/{name}", optimize=True, quality=quality)
        reduccion=(os.path.getsize(path)/peso)*100
        reduccion=round(reduccion, 2)
        print(f'**\t{name}: peso incial: {peso}[Bytes] - peso final: {os.path.getsize(path)}[Bytes]\n\t{reduccion} [%] : % Ocupacion Final - Reduccion dimensional: {x*100}[%]')
            
def funOptimizarDirectorio(rootdir):
    print(f'\n############# 2.2 INICIANDO OPTIMIZACION #########') 
    for rootdir, dirs, files in os.walk(rootdir,onerror=None):
        for subdir in dirs:
            path=os.path.join(rootdir, subdir)
        for subfile in files:
            path=os.path.join(rootdir, subfile)
            if ('.jpg' in subfile) or ('.jpeg' in subfile) or ('.jfif' in subfile) or ('.png' in subfile):
                try:
                    imagen = Image.open(os.path.join(rootdir, subfile))
                    optimizarImagenPillow(imagen,subfile,rootdir,path)
                except:
                    print(f'No fue posible optimizar archivo: {subfile}')                
            else:
                print(f'--\t{subfile}: No es una imagen')
    
def limpiar_pantalla():
    if so=="Windows": 
        os.system("cls")
    elif so== 'Linux': 
        os.system("clear") 

def directorio_verificado(path):
    intentos=0
    existe_directorio=os.path.exists(path)
    while existe_directorio==False:
        intentos +=1 
        print()
        if existe_directorio == True:
            print(f"#\tOk path seleccionado: {path}")
            path= path#salimos del bucle
            break
        if intentos>3:
            print(f'#\tSupera el maximo de intentos {intentos}')
            path= 'NOEXISTE'
            break
        else:
            print(f"#\tNo existe, el directorio ingresado: ")
            path=input("#\tIngresar nombre de directorio: ")
            existe_directorio=os.path.exists(path)
    return path

def crear_backup():
    print("############# 1. CREAR UN BACK UP ################")
    crearCopia=input("#\tDesea crear un backup de algún directorio?\n#\tyes or not :")
    if crearCopia!='yes' and crearCopia.lower()!='yes' and crearCopia!='not' and crearCopia.lower()!='not' :
        print('\nError!: Respuesta incorrecta ultimo intento ')
        crearCopia=input("#\tDesea crear un backup de algún directorio?\n#\tyes or not :")
        
    if crearCopia=='yes' or crearCopia.lower()=='yes':
        so=platform.system() 
        print(f'\n#\t1.1. Debes ingresar la ruta del directorio de origen so: {so}') 
        if so=="Windows": 
            print(f'#\tEj. path  : {os.getcwd()}\\mi_directorio_origen')
        elif so== 'Linux': 
            print(f'#\tEj. path  : {os.getcwd()}/mi_directorio_origen')   
        
        print(f'#\tEj. Relative path : mi_directorio_origen')
        pathCarpetaOrigen=input("#\tIngresar ruta de directorio que desea Copiar: ")        
        directorioOrigen_Verificado=directorio_verificado(pathCarpetaOrigen)

        if directorioOrigen_Verificado== 'NOEXISTE':
            print(f'\nError!: No fue posible crear backup a Directorio\n{pathCarpetaOrigen}')
        else:
            pathCarpetaOrigen=directorioOrigen_Verificado
            print(f'\nOk: El nombre del directorio origen es:\n{pathCarpetaOrigen}')
            print('\n#\tDebes ingresar un nombre o ruta para tu Directorio copia Ej. mi_directorio_backup')
            pathCarpetaDestino=input("#\tIngresar nombre o ruta del nuevo directorio: ")
            while pathCarpetaDestino==directorioOrigen_Verificado:
                print('El nuevo directorio debe ser diferente al inicial')
                pathCarpetaDestino=input("#\tIngresar nombre o ruta del nuevo directorio: ")
            try:
                shutil.copytree(pathCarpetaOrigen,pathCarpetaDestino)
                if so=="Windows":
                    print('\n############# 1.2 FINALIZA BACKUP ################')
                    print(f"Ok: El directorio destino se encuentra la ruta:\n {os.getcwd()}\\{pathCarpetaDestino} ")
                elif so== 'Linux':
                    print('\n############# 1.2 FINALIZA BACKUP ################')
                    print(f"Ok: El directorio destino se encuentra la ruta:\n {os.getcwd()}/{pathCarpetaDestino} ")
            except:
                print(f'Error!: No fue posible crear backup a {pathCarpetaOrigen}')

def optimizar():
    print("\n\n###### 2. OPTIMIZAR IMAGENES DE DIRECTORIO #######")
    optimizarDirectorio=input("#\tDesea optimizar imagenes de algun directorio?\n#\tyes or not :")
    if optimizarDirectorio!='yes' and optimizarDirectorio.lower()!='yes' and optimizarDirectorio!='not' and optimizarDirectorio.lower()!='not' :
        print('\nError!: Respuesta incorrecta ultimo intento ')
        optimizarDirectorio=input("#\tDesea optimizar imagenes de algun directorio?\n#\tyes or not :")
        
    if optimizarDirectorio=='yes' or optimizarDirectorio.lower()=='yes':
        print(f'\n#\t2.1. Debes ingresar la ruta del directorio de origen so: {so}')
        if so=="Windows":
            print(f'#\tEj. path  : {os.getcwd()}\\mi_directorio_origen')
        elif so== 'Linux':
            print(f'#\tEj. path  : {os.getcwd()}/mi_directorio_origen')

        print(f'#\tEj. Relative path : mi_directorio_origen')
        pathCarpetaOrigen=input("#\tIngresar nombre de directorio origen: ")
        directorioOrigen_Verificado=directorio_verificado(pathCarpetaOrigen)
        if directorioOrigen_Verificado== 'NOEXISTE':
            print('EL DIRECTORIO NO EXISTE')
        
        else:
            pathCarpetaOrigen=directorioOrigen_Verificado
            funOptimizarDirectorio(pathCarpetaOrigen)
            print(f'\n###### 2.3 FINALIZA OPTIMIZACION #################')
            print(f'Revisar directorio: {pathCarpetaOrigen}')

### ### ### MAIN ### ### ### ### ### ### ### ### ### ###
if __name__ == '__main__':
    
    limpiar_pantalla()
    print("############# INICIANDO PROGRAMA #################\n")
    print('\n###################### MENU ######################')
    print('#\t[1] Explorar Directorio                  #')
    print('#\t[2] Crear BackUp                         #')
    print('#\t[3] Optimizar Imágenes en un Directorio  #')
    print('#\t[4] Salir                                #')
    print('##################################################\n')
    opcion= input("Seleccione una opcion : ")
    try:
        opcion =int(opcion)
    except:
        opcion =0
    intentos=0
    while opcion<0 or opcion>4:
        intentos +=1
        print('\nOpción no válida!\n')
        opcion= input("Seleccione una opcion : ")
        try:
            opcion =int(opcion)
        except:
            opcion =0
        if intentos>=5:
            print("has agotado el numero de intentos")
            break

    while opcion!=4:        
        if opcion==1:
            limpiar_pantalla()
            print("explorar directorio ")
        elif opcion==2:
            limpiar_pantalla()
            crear_backup()
        elif opcion==3:
            limpiar_pantalla()
            print("Optimizar Imágenes en un Directorio")
            optimizar()
        elif opcion==4:
            break
        else:
            print("\nOpción no válida!\n")

        print('\n###################### MENU ######################')
        print('#\t[1] Explorar Directorio                  #')
        print('#\t[2] Crear BackUp                         #')
        print('#\t[3] Optimizar Imágenes en un Directorio  #')
        print('#\t[4] Salir                                #')
        print('##################################################\n')
        opcion= input("Seleccione una opcion : ")
        try:
            opcion =int(opcion)
        except:
            opcion =0
            
    

    
    
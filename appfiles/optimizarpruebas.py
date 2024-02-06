from PIL import Image
import os
import shutil
import platform
so=platform.system() 

def procesoOptimizacion(path):
        
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
                    reducida.save(f"{rootdir}\\{name}", optimize=True, quality=quality)
                elif so== 'Linux': 
                    reducida.save(f"{rootdir}/{name}", optimize=True, quality=quality)
            elif ancho > limite_pixeles:
                nuevoAncho = limite_pixeles
                ratio=(nuevoAncho/ancho)
                x = round(ratio, 2)
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
            pesoinicialmegabytes=peso/1000000
            pesoinicial = round(pesoinicialmegabytes, 3)
            fpeso=os.path.getsize(path)
            pesofinalmegabytes=fpeso/1000000
            pesofinal = round(pesofinalmegabytes, 3)
            print(f'**\tnombre: {name}, incial: {pesoinicial} , final: {pesofinal} , %Ocupacion: {reduccion}')

    def explorarDirectorio(rootdir):
        
        pesoTotal=0
        contadorImagenes=0
        todosDirectorios={}    
        for rootdir, dirs, files in os.walk(rootdir,onerror=None):        
            for subdir in dirs:
                pass          
            for subfile in files:
                if ('.jpg' in subfile.casefold()) or ('.jpeg' in subfile.casefold()) or ('.jfif' in subfile.casefold()) or ('.png' in subfile.casefold()):
                    path1=os.path.join(rootdir, subfile)
                    peso=os.path.getsize(path1)
                    imagen={}
                    if peso >400000:
                        dirname=os.path.dirname(path1)
                        imagen['dirname']=dirname
                        imagen['nombre']=subfile
                        imagen['peso']=peso
                        try:
                            todosDirectorios[f'{dirname}'].append(imagen)
                        except:
                            todosDirectorios[f'{dirname}']=[imagen]
                        pesoTotal+=peso
                        contadorImagenes+=1

        megabytes=pesoTotal/1000000
        gigabytes=megabytes/1000
        xM = round(megabytes, 2)
        xG=round(gigabytes, 2)
        print(f'\n############# 1.1 RESULTADOS EXPLORACIÓN #########\n') 
        for directorio in todosDirectorios:
            listaImagenes=todosDirectorios[f'{directorio}']
            totalpeso=0
            for objeto in listaImagenes:
                totalpeso+=(objeto['peso'])/1000000
            totalpeso=round(totalpeso, 3)
            print(f'Imagenes: {len(listaImagenes)} - Peso: {totalpeso}[MB] - Subdirectorio: {directorio}')
        print(f'\nImagenes sup 400KB: {contadorImagenes} - Peso Total: {xM}[MB] - {xG}[GB]\n')

    def funOptimizarDirectorio(rootdir):
        print(f'\n############# 3.2 INICIANDO OPTIMIZACION #########') 
        for rootdir, dirs, files in os.walk(rootdir,onerror=None):
            for subdir in dirs:
                pass
            for subfile in files:
                path1=os.path.join(rootdir, subfile)
                if ('.jpg' in subfile.casefold()) or ('.jpeg' in subfile.casefold()) or ('.jfif' in subfile.casefold()) or ('.png' in subfile.casefold()):
                    try:
                        imagen = Image.open(os.path.join(rootdir, subfile))
                        optimizarImagenPillow(imagen,subfile,rootdir,path1)
                    except:
                        print(f'No fue posible optimizar archivo: {subfile}')                
                else:
                    pass
        
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
                path= path
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

    def explorar(directorio_Exploracion):
        print("############# 1. EXPLORAR UN DIRECTORIO ################")
        explora='yes'
        if explora!='yes' and explora.lower()!='yes' and explora!='not' and explora.lower()!='not' :
            print('\nError!: Respuesta incorrecta ultimo intento ')
            explora=input("#\tDesea explorar algún directorio?\n#\tyes or not :")
            
        if explora=='yes' or explora.lower()=='yes':
            so=platform.system() 
            print(f'\n#\t1.1. Debes ingresar la ruta del directorio de origen so: {so}') 
            if so=="Windows": 
                print(f'#\tEj. path  : {os.getcwd()}\\mi_directorio_origen')
            elif so== 'Linux': 
                print(f'#\tEj. path  : {os.getcwd()}/mi_directorio_origen')   
            
            print(f'#\tEj. Relative path : mi_directorio_origen')
            #pathCarpetaOrigen=input("#\tIngresar ruta de directorio que desea explorar: ")        
            directorioOrigen_Verificado=directorio_verificado(directorio_Exploracion)

            if directorioOrigen_Verificado== 'NOEXISTE':
                print(f'\nError!: No fue posible explorar Directorio\n{pathCarpetaOrigen}')
            else:
                pathCarpetaOrigen=directorioOrigen_Verificado
                print(f'\nOk: El nombre del directorio origen es:\n{pathCarpetaOrigen}')
                explorarDirectorio(pathCarpetaOrigen)

    def ignore_files(folder, files):
        ignored_items = []
        for f in files :
            path1=os.path.join(folder, f)
            peso=os.path.getsize(path1)
            if not os.path.isdir(path1):
                if not peso >400000 :
                    ignored_items.append(f)
                if not(('.jpg' in path1.casefold()) or ('.jpeg' in path1.casefold()) or ('.jfif' in path1.casefold()) or ('.png' in path1.casefold())):           
                    ignored_items.append(f)
        return ignored_items              

    
    def crear_backup_imagenes(path_origen,path_destino):
        print("############# 2. CREAR UN BACK UP ################")
        #crearCopia=input("#\tDesea crear un backup de algún directorio?\n#\tyes or not :")
        crearCopia='yes'
        if crearCopia!='yes' and crearCopia.lower()!='yes' and crearCopia!='not' and crearCopia.lower()!='not' :
            print('\nError!: Respuesta incorrecta ultimo intento ')
            crearCopia=input("#\tDesea crear un backup de algún directorio?\n#\tyes or not :")
            
        if crearCopia=='yes' or crearCopia.lower()=='yes':
            so=platform.system() 
            print(f'\n#\t2.1. Debes ingresar la ruta del directorio de origen so: {so}') 
            if so=="Windows": 
                print(f'#\tEj. path  : {os.getcwd()}\\mi_directorio_origen')
            elif so== 'Linux': 
                print(f'#\tEj. path  : {os.getcwd()}/mi_directorio_origen')   
            
            print(f'#\tEj. Relative path : mi_directorio_origen')
            #pathCarpetaOrigen=input("#\tIngresar ruta de directorio que desea Copiar: ")        
            #directorioOrigen_Verificado=directorio_verificado(pathCarpetaOrigen)
            directorioOrigen_Verificado=directorio_verificado(path_origen)
            if directorioOrigen_Verificado== 'NOEXISTE':
                print(f'\nError!: No fue posible crear backup a Directorio\n{pathCarpetaOrigen}')
            else:
                pathCarpetaOrigen=directorioOrigen_Verificado
                print(f'\nOk: El nombre del directorio origen es:\n{pathCarpetaOrigen}')
                print('\n#\tDebes ingresar un nombre o ruta para tu Directorio copia Ej. mi_directorio_backup')
                #pathCarpetaDestino=input("#\tIngresar nombre o ruta del nuevo directorio: ")
                pathCarpetaDestino=path_destino
                while pathCarpetaDestino==directorioOrigen_Verificado:
                    print('El nuevo directorio debe ser diferente al inicial')
                    pathCarpetaDestino=input("#\tIngresar nombre o ruta del nuevo directorio: ")
                try:
                    shutil.copytree(pathCarpetaOrigen,pathCarpetaDestino,symlinks=False,ignore=ignore_files)
                    if so=="Windows":
                        print('\n############# 2.2 FINALIZA BACKUP ################')
                        print(f"Ok: El directorio destino se encuentra la ruta:\n {os.getcwd()}\\{pathCarpetaDestino} ")
                    elif so== 'Linux':
                        print('\n############# 2.2 FINALIZA BACKUP ################')
                        print(f"Ok: El directorio destino se encuentra la ruta:\n {os.getcwd()}/{pathCarpetaDestino} ")
                except:
                    print(f'Error!: No fue posible crear backup a {pathCarpetaOrigen}')
    def optimizar(directorio_a_optimizar):
        print("\n\n###### 3. OPTIMIZAR IMAGENES DE DIRECTORIO #######")
        #optimizarDirectorio=input("#\tDesea optimizar imagenes de algun directorio?\n#\tyes or not :")
        optimizarDirectorio='yes'
        if optimizarDirectorio!='yes' and optimizarDirectorio.lower()!='yes' and optimizarDirectorio!='not' and optimizarDirectorio.lower()!='not' :
            print('\nError!: Respuesta incorrecta ultimo intento ')
            optimizarDirectorio=input("#\tDesea optimizar imagenes de algun directorio?\n#\tyes or not :")
            
        if optimizarDirectorio=='yes' or optimizarDirectorio.lower()=='yes':
            print(f'\n#\t3.1. Debes ingresar la ruta del directorio de origen so: {so}')
            if so=="Windows":
                print(f'#\tEj. path  : {os.getcwd()}\\mi_directorio_origen')
            elif so== 'Linux':
                print(f'#\tEj. path  : {os.getcwd()}/mi_directorio_origen')

            print(f'#\tEj. Relative path : mi_directorio_origen')
            #pathCarpetaOrigen=input("#\tIngresar nombre de directorio origen: ")
            #directorioOrigen_Verificado=directorio_verificado(pathCarpetaOrigen)
            directorioOrigen_Verificado=directorio_verificado(directorio_a_optimizar)
            if directorioOrigen_Verificado== 'NOEXISTE':
                print('EL DIRECTORIO NO EXISTE')
            
            else:
                pathCarpetaOrigen=directorioOrigen_Verificado
                funOptimizarDirectorio(pathCarpetaOrigen)
                print(f'\n###### 3.3 FINALIZA OPTIMIZACION #################')
                print(f'Revisar directorio: {pathCarpetaOrigen}')

    ### ### ### MAIN ### ### ### ### ### ### ### ### ### ###        
    limpiar_pantalla()
    print("############# INICIANDO PROGRAMA #################")
    print('#\t[1] Explorar Directorio                  #')
    print('##################################################\n')  
    explorar(path)
    print('##################################################')  
    print('#\t[2] Optimizar Directorio                  #')
    print('##################################################\n')  
    optimizar(path)
    print('##################################################')  
    print('#\t[3] Explorar Directorio                  #')
    print('##################################################') 
    explorar(path)
    #print('##################################################')  
    #print('#\t[4] Optimizar Imágenes en un Directorio  #')
    #print('##################################################') 
    #path_destino=path+'_backup'
    #crear_backup_imagenes(path,path_destino)
path='C:/Users/eadel/OneDrive/Documents/VISUAL_STUDIO_PROJECTS/LEARNING_PROJECTS/OPTIMIZE_IMAGE/appfiles/instalaciones'
#path='integraciones'
procesoOptimizacion(path=path)
       
import subprocess


comando = ['python', 'optimizar.py']
ruta_log = 'C:/Users/eadel/OneDrive/Documents/app/optimacion_instalaciones.log'

inputs = ["1", "yes", "instalaciones"]
#time.sleep(2)
#process.communicate(input=1)[0]
"""for entrada in inputs:
    salida, error = proceso.communicate(input=entrada)
    print("Salida del proceso:", salida)
    print("Error del proceso:", error)"""
with open(ruta_log, 'x') as log_file:
    try:
        path='C:/Users/eadel/OneDrive/Documents/VISUAL_STUDIO_PROJECTS/LEARNING_PROJECTS/OPTIMIZE_IMAGE/appfiles/instalaciones'
        #path='integraciones'
        #salida=procesoOptimizacion(path=path)
        #subprocess.run(rsync_command1, check=True)
        #proceso=subprocess.run('python C:/Users/eadel/OneDrive/Documents/WIGILABS/optimizar.py',shell=True,  stdout=log_file, stderr=subprocess.STDOUT)
        #proceso=subprocess.run('python C:/Users/eadel/OneDrive/Documents/WIGILABS/optimizar.py',shell=True,  stdout=log_file, stderr=subprocess.STDOUT)
        #proceso = subprocess.run(comando, shell=True, stdout=log_file, stderr=subprocess.STDOUT, text=True)
        proceso = subprocess.Popen(comando, shell=True, stdout=log_file, stdin=subprocess.PIPE,stderr=subprocess.STDOUT, text=True)
        #subprocess.run(rsync_command2)
        #inputs = ["1", "yes", "C:/Users/eadel/OneDrive/Documents/VISUAL_STUDIO_PROJECTS/LEARNING_PROJECTS/OPTIMIZE_IMAGE/appfiles/instalaciones","4"]
        #proceso.communicate(input=entrada[0].encode())
        # Enviar cada input al proceso
        proceso.stdin.write("1\n")
        proceso.stdin.write("yes\n")
        proceso.stdin.write("instalaciones\n")
        proceso.stdin.write("3\n")
        proceso.stdin.write("yes\n")
        proceso.stdin.write("instalaciones\n")
        proceso.stdin.write("1\n")
        proceso.stdin.write("yes\n")
        proceso.stdin.write("instalaciones\n")
        proceso.stdin.write("4\n")
        #stdout_data = proceso.communicate(input='1')[0]
        
        #stdout_data = proceso.communicate(input=path)[0]
        #stdout_data = proceso.communicate(input=4)[0]
        
        #path='C:/Users/eadel/OneDrive/Documents/VISUAL_STUDIO_PROJECTS/LEARNING_PROJECTS/OPTIMIZE_IMAGE/appfiles/instalaciones'
        #procesoOptimizacion(path=path)
        """for entrada in inputs:
            salida, error = proceso.communicate(input=entrada)
            print("Salida del proceso:", salida)
            print("Error del proceso:", error)"""
    except subprocess.CalledProcessError as e:
    # logger.error(f'Error while running rsync: {e}')
        print('no se optimiza')

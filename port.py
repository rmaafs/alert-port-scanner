import os, time
cooldown = 5#Tiempo que tardará escuchando los paquetes en los puertos
recordsFileName = "records.pcap"#Archivo donde se guardarán los paquetes temporalmente

while True:
    #Empezaremos a capturar los paquetes de los siguientes rangos de puertos.
    #Los paquetes se guardarán en un archivo temporal
    os.system('(tcpdump -i any \'portrange 100-150 or portrange 1000-1050 or portrange 10000-11000\' -w ' + recordsFileName + ' & pid=$! ; sleep ' + str(cooldown) + ' ; kill -1 $pid) 2> /dev/null')
    time.sleep(1)#Este timer se usa en caso de que quieras cancelar el ciclo, pulsar CTRL + C, 2 rápido veces seguidas
    size = os.stat(recordsFileName).st_size#Obtenemos el size del archivo temporal

    #Normalmente, si no se recibe ningún paquete en el rango de puertos, el size del archivo temporal es de 24 bytes
    print("Size: " + str(size))
    if size > 24:#En caso de que tenga algún paquete capturado
        print("Se esta haciendo port scanner, guardado en el archivo log" + str(int(time.time())) + ".pcap")
        #Creamos una copia del archivo temporal para analizarlo en un futuro
        os.system('mkdir -p logs && cp ' + recordsFileName + ' logs/log' + str(int(time.time())) + '.pcap')
        #Enviar correo o notificación push al administrador para analizar el log creado con el timestamp en unix.

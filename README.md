# alert-port-scanner
Script que alerta al administrador cuando se detecte un escaneo en un rango de puertos, normalmente utilizando nmap

### Testeado únicamente en servidores Linux

![Consola](https://i.imgur.com/vA3JyVB.png)

![WireShark](https://i.imgur.com/pJIoIwl.png)

---

### Instalación
- Unicamente descargar el archivo port.py

---

### Configuración
En el código, podrá cambiar las condiciones de ``portrange`` para usar los rangos que usted guste.
En mi caso, en el código tengo los siguientes rangos:
- 100 - 150
- 1000 - 1050
- 10000 - 11000

Puede agregar los que usted guste, añadiendo sus rangos o sus nuevos ``or``.

---

### Ejecución
Al ejecutar el script y se capture mínimo un paquete en el rango que usted especificó, se guardará una copia
de los paquetes capturados en el archivo ``log/log<unix_time_stamp>.pcap``, y así poder descargarlo
y visualizarlo de forma visual en WireShark, o desde consola utilizando

```
$ tcpdump -qns 0 -X -r archivo.pcap
```

![Ejemplo](https://i.imgur.com/ETEummV.png)

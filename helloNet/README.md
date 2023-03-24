# REQUIREMENTS

- Docker instalado en tu sistema operativo. Si aún no tienes Docker instalado, puedes ver como descargarlo e instalarlo en este [video](https://youtu.be/YpBoqXK_3wE).

- Git

# STEPS

0) Abre una terminal y clona este repositorio en tu sistema:

   ```bash
   git clone https://github.com/kamilinuxoficial/hello-apps
   cd hello-apps/helloNet 
   ```
   
1) Tenemos que generar el cuerpo de la aplicación web, para ello utilizamos el QuickStart de dotnet:
``` code
#Si no tenemos instalado el comando dotnet, entramos al contenedor
docker run -it mcr.microsoft.com/dotnet/sdk:6.0 
#generamos la plantilla
dotnet new webapp -n myWebApp -o src --no-https
```
2) Copiamos la el codigo generado a local
``` code
docker cp <container_id>:/tmp/src .
```
3) Buildeamos la imagen de contenedor
``` code
docker build -t hellonet .
```
4) Ejecutamos nuestra app 

``` code
docker run -p 5000:80 hellonet
```
5) Ahora puedes acceder a la aplicación a través de tu navegador web en la siguiente [URL](http://localhost:5000).

 Eso es todo lo que necesitas para ejecutar la aplicación utilizando Docker. Si necesitas detener la ejecución de la aplicación, puedes presionar CTRL+C en la terminal donde está ejecutándose el contenedor. 

## AVISO
 
Cuando el programa termina su ejecución el contendor muere.

Todo lo que tengas en el contenedor como configuraciones, logs... se perdederán si se apaga el contenedor.

En este caso el programa, al ser un servicio web el contenedor no muere porque tiene un proceso en segundo plano (la ejecución del servidor web).

El contenedor seguirá vivo hasta que nosotros lo paremos, o hasta que haya un fallo y el motor de contenedores decida matar el contenedor.

## BACKGROUND MODE

Tambien puedes dejar el contenedor en segundo plano (deattach)

  ```bash
   docker run -d nombre-de-la-imagen
   ```


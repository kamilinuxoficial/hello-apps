1) Tenemos que generar el cuerpo de la aplicación web, para ello utilizamos el QuickStart de dotnet:
``` code
#entramos en un contenedor dotnet, si no tenemos instalado el comando dotnet
docker run -it mcr.microsoft.com/dotnet/sdk:6.0 
#generamos la plantilla
dotnet new webapp -n myWebApp -o src --no-https
```
2)COPIAMOS LA PLANTILLA AL LOCAL
``` code
docker cp <container_id>:/tmp/src .
```
3) Buildeamos
``` code
docker build -t hellonet .
```
4) Ejecutamos nuestra app 

``` code
docker run -p 5000:80 hellonet
```

1) Tenemos que generar el cuerpo de la aplicación web,
para ello ejecutamos: 
docker run -it mcr.microsoft.com/dotnet/sdk:6.0 
#generamos la plantilla
dotnet new webapp -n myWebApp -o src --no-https
2)COPIAMOS LA PLANTILLA AL LOCAL
3) Buildeamos
docker build -t hellonet .
3) docker run 
docker run -p 5000:80 hellonet

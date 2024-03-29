# REQUIREMENTS

- Docker instalado en tu sistema operativo. Si aún no tienes Docker instalado, puedes ver como descargarlo e instalarlo en este [video](https://youtu.be/YpBoqXK_3wE).

- Git

# STEPS

1. Abre una terminal y clona este repositorio en tu sistema:

   ```bash
   git clone https://github.com/kamilinuxoficial/hello-apps 
   cd hello-apps/helloNodeJS
   ```
2. Construye la imagen del contenedor utilizando el siguiente comando:
   ```bash
   docker build -t nombre-de-la-imagen .
   ```

3. Una vez que se haya construido la imagen, puedes ejecutar la aplicación dentro de un contenedor utilizando el siguiente comando:
   ```bash
   docker run -p 8080:8080 nombre-de-la-imagen
   ```
4. Ahora puedes acceder a la aplicación a través de tu navegador web en la siguiente [URL](http://localhost:8080).


 Eso es todo lo que necesitas para ejecutar la aplicación utilizando Docker. Si necesitas detener la ejecución de la aplicación, puedes presionar CTRL+C en la terminal donde está ejecutándose el contenedor. 

## AVISO
 
Cuando el programa termina su ejecución el contendor muere.

Todo lo que tengas en el contenedor como configuraciones, logs... se perdederán si se apaga el contenedor.

En este caso el programa, al ser un servicio web el contenedor no muere porque tiene un proceso en segundo plano (la ejecución del servidor web).

El contenedor seguirá vivo hasta que nosotros lo paremos (CONTROL + C), o hasta que haya un fallo y el motor de contenedores decida matar el contenedor.

## BACKGROUND MODE

Tambien puedes dejar el contenedor en segundo plano (deattach)

  ```bash
   docker run -d nombre-de-la-imagen
   ```

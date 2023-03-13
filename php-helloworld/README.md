# REQUIREMENTS

- Docker instalado en tu sistema operativo. Si aún no tienes Docker instalado, puedes ver como descargarlo e instalarlo en este [video](https://youtu.be/YpBoqXK_3wE).

- Git

# STEPS

1. Abre una terminal y clona este repositorio en tu sistema:

   ```bash
   git clone https://github.com/kamilinuxoficial/hello-apps 
   cd hello-apps/php-helloworld
   ```
2. Construye la imagen del contenedor utilizando el siguiente comando:
   ```bash
   docker build -t nombre-de-la-imagen .
   ```

3. Una vez que se haya construido la imagen, puedes ejecutar la aplicación dentro de un contenedor utilizando el siguiente comando:
   ```bash
   docker run -p 80:80 nombre-de-la-imagen
   ```
4. Ahora puedes acceder a la aplicación a través de tu navegador web en la siguiente [URL](http://localhost).


 Eso es todo lo que necesitas para ejecutar la aplicación utilizando Docker. Si necesitas detener la ejecución de la aplicación, puedes presionar CTRL+C en la terminal donde está ejecutándose el contenedor.

Tambien puedes dejar el contenedor en segundo plano (deattach)

  ```bash
   docker run -d -p 80:80 nombre-de-la-imagen
   ```

¡Gracias por utilizar nuestra aplicación! Si tienes alguna pregunta o problema al ejecutar la aplicación, no dudes en contactarnos.

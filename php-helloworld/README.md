# REQUIREMENTS

- Docker instalado en tu sistema operativo. Si aún no tienes Docker instalado, puedes ver como descargarlo e instalarlo en este video https://www.docker.com/get-started.

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

docker run -p 8000:8000 nombre-de-la-imagen

```
4. Ahora puedes acceder a la aplicación a través de tu navegador web en la siguiente URL:


Eso es todo lo que necesitas para ejecutar la aplicación utilizando Docker. Si necesitas detener la ejecución de la aplicación, puedes presionar CTRL+C en la terminal donde está ejecutándose el contenedor.

¡Gracias por utilizar nuestra aplicación! Si tienes alguna pregunta o problema al ejecutar la aplicación, no dudes en contactarnos.

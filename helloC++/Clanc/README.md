# REQUIREMENTS

- Docker instalado en tu sistema operativo. Si aún no tienes Docker instalado, puedes ver como descargarlo e instalarlo en este [video](https://youtu.be/YpBoqXK_3wE).

- Git

# STEPS

1. Abre una terminal y clona este repositorio en tu sistema:

   ```bash
   git clone https://github.com/kamilinuxoficial/hello-apps
   cd hello-apps/helloC++/Clanc
   ```
   
2. Construye la imagen del contenedor utilizando el siguiente comando:

   ```bash
   docker build -t nombre-de-la-imagen .
   ```

3. Una vez que se haya construido la imagen, puedes ejecutar la aplicación dentro de un contenedor utilizando el siguiente comando:

   ```bash
   docker run nombre-de-la-imagen
   ```
 
 
## AVISO
Cuando el programa termina su ejecución el contendor muere.

Todo lo que tengas en el contenedor como configuraciones, logs... se perdederán si se apaga el contenedor.

En este caso el programa es muy sencillo y su ejecución es muy rápida, por tanto el contenedor muere muy rápido.


## BACKGROUND MODE

Tambien puedes dejar el contenedor en segundo plano (deattach)

Cuando se ejecuta el programa de C++, el contenedor muere, por lo tanto el siguiente comando no funcionaría:

  ```bash
   docker run -d nombre-de-la-imagen
   ```

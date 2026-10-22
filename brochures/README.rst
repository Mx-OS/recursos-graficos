============================
Folletos y Trípticos de MxOS
============================

Este directorio contiene los materiales informativos y folletos vectoriales de MxOS, diseñados con un enfoque ligero, cercano y directo para escuelas, universidades, congresos y entusiastas del software libre.

Todos los archivos maestros están estructurados por capas nativas de Inkscape y utilizan exclusivamente la tipografía **Liberation Mono** en nodos de texto editables, sin convertir tipografías a curvas, facilitando su actualización y adaptación directa.

Archivos Vectoriales Disponibles
================================

Folleto de Una Página
---------------------

* ``folleto-ejecutivo.svg``: Hoja informativa vertical en tamaño Carta de 215.9 por 279.4 mm, equivalente a 816 por 1056 px a 96 ppp. Presenta qué es MxOS, sus casos de uso cotidianos, desde jugar en Steam y estudiar hasta levantar servidores o aprender a empaquetar software, y el directorio completo de ligas oficiales con códigos QR vectoriales.

Tríptico Impreso de Doble Cara
------------------------------

* ``triptico-exterior.svg``: Cara exterior en tamaño Carta horizontal de 279.4 por 215.9 mm, equivalente a 1056 por 816 px a 96 ppp, dividida en tres paneles de 352 px con guías de pliegue en ``x=352`` y ``x=704``:

  * **Panel izquierdo o solapa interior:** Por qué aprender a construir la tecnología nosotros mismos en México y cómo sumarse al proyecto.
  * **Panel central o contraportada:** Directorio de ligas de interés con códigos QR vectoriales y datos de contacto de la comunidad.
  * **Panel derecho o portada:** Isotipo oficial del águila, título principal, lema y resumen de características para escritorio, videojuegos y servidores.

* ``triptico-interior.svg``: Cara interior en tamaño Carta horizontal de 1056 por 816 px, dividida en tres paneles de 352 px:

  * **Panel izquierdo:** Qué es MxOS, para qué se puede usar en el día a día y cómo parte de una base sencilla adaptable mediante ediciones.
  * **Panel central:** Esquema visual en cuatro bloques de cómo se adapta el sistema y qué hace diferente a MxOS.
  * **Panel derecho:** Recorrido por las plataformas abiertas bajo ``mx-os.mx``, ejemplo en terminal con IPFS e invitación a la comunidad en Telegram.

Ligas Oficiales Incluidas
=========================

.. list-table::
   :widths: 25 35 40
   :header-rows: 1

   * - Plataforma
     - Enlace
     - Propósito
   * - Sitio web
     - ``https://mx-os.mx``
     - Noticias, descargas y blog del proyecto
   * - Documentación
     - ``https://docs.mx-os.mx``
     - Guías paso a paso y manuales en español
   * - Forja Git
     - ``https://git.mx-os.mx``
     - Código fuente, recetas de paquetes, scripts y diseño
   * - Espejos
     - ``https://mirrors.mx-os.mx``
     - Imágenes ISO y paquetes distribuidos por HTTP e IPFS
   * - Telegram
     - ``https://t.me/mx_os_mx``
     - Canal comunitario para resolver dudas, aprender y colaborar

Estructura de Capas en Inkscape
===============================

Cada archivo SVG está organizado en capas independientes para agilizar su edición en Inkscape:

#. ``01 - Fondo y Contenedores``: Tarjetas, fondos, líneas divisorias y franjas de color.
#. ``02 - Guias de Pliegue``: Líneas punteadas de referencia para el doblado del tríptico; puede ocultarse antes de exportar a imprenta.
#. ``03 - Logotipo, Iconos y QR``: Trazos vectoriales del isotipo oficial de ``logo/isotipo.svg``, iconografía y códigos QR.
#. ``04 - Textos Editables en Liberation Mono``: Todos los títulos, párrafos, comandos y enlaces en elementos ``<text>`` nativos.

Exportación a PNG
=================

Para generar las vistas previas rasterizadas en ``output/``:

.. code-block:: bash

   make

Para limpiar los archivos generados:

.. code-block:: bash

   make clean

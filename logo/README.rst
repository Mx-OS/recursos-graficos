==============================
Logotipo Oficial de MxOS
==============================

Este directorio contiene los archivos vectoriales maestros del logotipo e identidad gráfica oficial de la Fundación MxOS, basados en la propuesta ganadora del concurso comunitario (**propuesta a2** de `@fitorec <https://gitlab.com/fitorec>`_).

Archivos Vectoriales Disponibles
================================

Isotipo Oficial
---------------

* ``isotipo.svg`` / ``a2.svg``: Cabeza de águila estilizada en trazo vectorial limpio con colores oficiales verde, terracota y dorado. Adecuada para avatares, favicons, iconos de aplicación y elementos identitarios compactos.

Imagotipo (Isotipo + Nombre)
----------------------------

* ``logo_horizontal.svg``: Versión horizontal con el isotipo a la izquierda y el identificador tipográfico "MxOS" a la derecha. Ideal para barras de navegación, cabeceras de sitios web, documentos y firmas institucionales.
* ``logo_sub_horizontal.svg``: Versión horizontal que incorpora la bajada institucional o subtítulo de la fundación.
* ``logo_vertical.svg``: Versión vertical centrada con el isotipo sobre la palabra "MxOS". Adecuada para portadas de manuales, carteles y pantallas de bloqueo o inicio de sesión.
* ``logo_sub_vertical.svg``: Versión vertical con subtítulo institucional inferior.

Variantes de Contraste y Fondo
------------------------------

* ``logo_fondo_blanco.svg``: Isotipo integrado sobre contenedor circular blanco, garantizando legibilidad sobre fondos oscuros o fotográficos.
* ``logo_fondo_negro.svg``: Isotipo integrado sobre contenedor circular oscuro, para uso en interfaces nocturnas y fondos monocromáticos.

Elementos de Identidad Complementarios
--------------------------------------

* ``pattern.svg``: Patrón geométrico decorativo derivado de las formas angulares del plumaje del águila. Apto para fondos sutiles, cintillos y material editorial.

Paleta de Color Oficial
=======================

.. list-table::
   :widths: 25 20 30 25
   :header-rows: 1

   * - Nombre del Tono
     - Hexadecimal
     - RGB
     - Uso
   * - Verde Bandera
     - ``#00815b``
     - rgb(0, 129, 91)
     - Color primario institucional, tipografía y plumas superiores
   * - Terracota / Ámbar
     - ``#a76350``
     - rgb(167, 99, 80)
     - Acento cálido en plumaje inferior
   * - Ocre Claro
     - ``#f5dc94``
     - rgb(245, 220, 148)
     - Tono de luminosidad y contraste
   * - Gris Carbón
     - ``#333333``
     - rgb(51, 51, 51)
     - Textos neutros y contrastes oscuros
   * - Blanco Nieve
     - ``#ffffff``
     - rgb(255, 255, 255)
     - Fondos y contenedor de contraste

Tipografía de Marca
===================

El logotipo compuesto utiliza la tipografía **Nimbus Sans** (Bold) para la palabra "MxOS". Para aplicaciones técnicas y código fuente se utiliza **Hack**, y para textos continuos **Fira Sans** o **Roboto**.

Exportación a PNG
=================

Para generar versiones rasterizadas (PNG) de todos los logotipos:

.. code-block:: bash

   make

Los archivos generados se ubicarán en la carpeta ``output/``.

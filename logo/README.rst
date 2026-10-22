==============================
Logotipo Oficial de MxOS
==============================

Este directorio contiene los archivos vectoriales maestros del logotipo e identidad gráfica oficial de la Fundación MxOS, derivados directamente de la propuesta ganadora del concurso comunitario (**propuesta a2** de `@fitorec <https://gitlab.com/fitorec>`_).

Archivos Vectoriales Disponibles
================================

Logotipo Principal e Isotipo
----------------------------

* ``a2.svg``: Logotipo oficial maestro con la cabeza de águila estilizada, plumaje en tres trazos verdes y el identificador tipográfico ``MxOS`` integrado en su curvatura interior sobre fondo transparente.
* ``isotipo.svg``: Símbolo puro del águila estilizada sin texto, centrado y con fondo transparente. Adecuado para avatares, favicons, iconos de aplicación y elementos compactos.

Imagotipos de Composición Externa
---------------------------------

* ``logo_horizontal.svg``: Versión horizontal con el isotipo a la izquierda y el identificador ``MxOS`` a la derecha sobre fondo transparente.
* ``logo_sub_horizontal.svg``: Banner horizontal con el isotipo a la izquierda, el identificador ``MxOS``, pleca divisoria roja y el lema *Distribución Linux segura, abierta y soberana para México*.
* ``logo_vertical.svg``: Versión vertical centrada con el isotipo en la parte superior y la palabra ``MxOS`` debajo.
* ``logo_sub_vertical.svg``: Versión vertical centrada con el isotipo, ``MxOS``, pleca divisoria roja y lema institucional en la base.

Variantes de Contraste y Fondo
------------------------------

* ``logo_fondo_blanco.svg``: Logotipo oficial sobre lienzo blanco sólido (``#ffffff``).
* ``logo_fondo_negro.svg``: Logotipo oficial adaptado para fondos oscuros (``#191919``), con cabeza de águila en gris claro (``#e6e6e6``), sombra de plumaje en negro (``#000000``) y plumaje/tipografía en verde institucional.

Elementos Simbólicos
--------------------

* ``pattern.svg``: Isotipo monocromático en gris claro (``#e6e6e6``) a tamaño compacto (48x48 px), apto para iconos simbólicos de escritorio, marcas de agua y patrones de fondo.

Paleta de Color Oficial
=======================

.. list-table::
   :widths: 25 20 30 25
   :header-rows: 1

   * - Nombre del Tono
     - Hexadecimal
     - RGB
     - Uso
   * - Verde Principal
     - ``#389476``
     - rgb(56, 148, 118)
     - Plumaje del águila y acentos primarios
   * - Verde Esmeralda
     - ``#10b981``
     - rgb(16, 185, 129)
     - Identificador tipográfico ``MxOS`` en ``a2.svg``
   * - Gris Carbón
     - ``#333333``
     - rgb(51, 51, 51)
     - Cabeza del águila, sombras y textos neutros
   * - Rojo Institucional
     - ``#a02c2c``
     - rgb(160, 44, 44)
     - Pleca divisoria y acentos secundarios
   * - Gris Claro
     - ``#e6e6e6``
     - rgb(230, 230, 230)
     - Cabeza del águila en versión oscura e icono simbólico
   * - Fondo Oscuro
     - ``#191919``
     - rgb(25, 25, 25)
     - Lienzo de contraste nocturno
   * - Blanco
     - ``#ffffff``
     - rgb(255, 255, 255)
     - Lienzo de contraste claro

Tipografía de Marca
===================

El identificador ``MxOS`` en ``a2.svg`` está trazado a curvas a partir de **Metrophobic**. Para lemas, documentación técnica, interfaz y código fuente se utiliza **Hack**, acompañada de **Fira Sans** o **Roboto** como fuentes secundarias.

Exportación a PNG
=================

Para generar versiones rasterizadas en formato PNG de todos los logotipos:

.. code-block:: bash

   make

Los archivos generados se ubicarán en la carpeta ``output/``.

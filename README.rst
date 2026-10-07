============================================
Recursos Gráficos de la Fundación MxOS
============================================

Este repositorio alberga el acervo oficial de identidad visual, logotipos maestros, manuales de marca, fondos de pantalla y diagramas arquitectónicos de la Fundación MxOS.

Estructura del Repositorio
==========================

* ``logo/``: Logotipos e imagotipos oficiales de producción, basados en la propuesta ganadora comunitaria (**a2**).
* ``wallpapers/``: Ilustraciones panorámicas y fondos de pantalla oficiales del sistema operativo.
* ``diagramas/``: Diagramas declarativos de arquitectura, gobernanza y soberanía técnica en formato D2.
* ``posters/``: Carteles y material visual de difusión institucional y comunitaria.
* ``source/``: Fuentes en Sphinx del *Manual de Identidad Visual* de MxOS.
* ``propuestas_logotipo/``: Acervo histórico de todas las propuestas vectoriales evaluadas durante el concurso de identidad visual.

Logotipo Oficial
================

El logotipo institucional de MxOS representa la cabeza estilizada de un águila real mexicana en tonalidades verde bandera, terracota y dorado. El diseño fue seleccionado por la comunidad mediante proceso de votación a partir de la propuesta **a2** creada por `@fitorec <https://gitlab.com/fitorec>`_.

En el directorio ``logo/`` se encuentran disponibles los archivos maestros:

* ``logo/isotipo.svg`` / ``logo/a2.svg``: Símbolo esencial del águila.
* ``logo/logo_horizontal.svg``: Versión horizontal con imagotipo e identificador "MxOS".
* ``logo/logo_vertical.svg``: Versión vertical para portadas y bloqueos de pantalla.
* ``logo/logo_fondo_blanco.svg``: Variante con contenedor circular blanco.
* ``logo/logo_fondo_negro.svg``: Variante con contenedor circular oscuro.
* ``logo/pattern.svg``: Patrón geométrico decorativo para fondos y cintillos.

Requisitos de Compilación
=========================

* **GNU Make**: Sistema de compilación y ejecución de metas.
* **Python 3 con CairoSVG**: Rasterización de vectores SVG a PNG (``pip install cairosvg``).
* **D2**: Compilador de diagramas declarativos (``d2``).
* **Sphinx con Furo**: Compilador de documentación técnica (``pip install sphinx furo sphinx-design``).

Comandos Disponibles
====================

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Comando
     - Acción
   * - ``make`` o ``make all``
     - Compila los logotipos oficiales, fondos de pantalla y diagramas arquitectónicos.
   * - ``make logo``
     - Rasteriza todas las variantes del logotipo en ``logo/output/``.
   * - ``make wallpapers``
     - Genera los fondos de pantalla a resolución QHD (2560x1440) en ``wallpapers/output/``.
   * - ``make diagramas``
     - Compila los diagramas D2 a formatos PNG, PDF y SVG.
   * - ``make manual-html``
     - Compila el *Manual de Identidad Visual* en HTML (ubicado en ``source/_build/html/``).
   * - ``make clean``
     - Elimina todos los directorios de salida y archivos temporales generados.

Licencia
========

Este proyecto implementa una estructura de licenciamiento dual para proteger tanto el software de conversión como el acervo gráfico original:

* **Herramientas de conversión, scripts y compilación:** El script rasterizador ``svg2png.py`` y los archivos ``GNUmakefile`` se distribuyen bajo los términos de la `GNU General Public License v3.0 o posterior`_ (GPL-3.0-or-later).
* **Diseños gráficos, diagramas, posters y fondos de pantalla:** Todo el material artístico, ilustraciones vectoriales, logotipos derivados, carteles y fondos de pantalla se distribuyen bajo la licencia `Creative Commons Attribution-ShareAlike 4.0 International`_ (CC-BY-SA-4.0).
* **Identidad de marca y marcas registradas:** Los nombres, logotipos institucionales y marcas distintivas de la Fundación MxOS están reservados conforme a las políticas de marca de la organización.

Consulta el archivo `LICENSE`_ para el texto íntegro de la licencia principal y el directorio ``LICENSES/`` para los textos canónicos de cumplimiento REUSE.

..
   Referencias y Enlaces:
.. _GNU General Public License v3.0 o posterior: https://www.gnu.org/licenses/gpl-3.0.html
.. _Creative Commons Attribution-ShareAlike 4.0 International: https://creativecommons.org/licenses/by-sa/4.0/
.. _LICENSE: LICENSE

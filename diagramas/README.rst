==============
MxOS Diagramas
==============

Descripción
===========
Este repositorio contiene recursos gráficos para los diagramas de MxOS. Los diagramas están definidos en formato D2 (Declarative
Diagramming) y se generan automáticamente en formatos PDF, PNG, SVG y TXT.

Archivos
--------
- ``mxos-general.d2``: Diagrama general de MxOS.
- ``mxos-reducido.d2``: Diagrama reducido de MxOS.
- ``GNUmakefile``: Makefile para generar los diagramas.


Pre-requisitos
==============
- D2: Herramienta para generar diagramas. Descárgala desde `https://d2lang.com/ <https://d2lang.com/>`_.
- GNU Make: Para ejecutar el GNUmakefile.


Uso
===
Para generar los diagramas, necesitas tener D2 instalado. Ejecuta el siguiente comando:

.. code-block:: bash

   make

Esto generará los archivos PDF, PNG, SVG y TXT a partir de los archivos D2.

También, puedes generar archivos individuales con:

.. code-block:: bash

   make mxos-general.png

por ejemplo. Las recetas se generan automáticamente para cualquier nuevo diagrama que agreguemos.


Contribución
============
Si deseas contribuir, edita los archivos .d2 y ejecuta ``make`` para actualizar los diagramas.


Licencia
========
Este proyecto está bajo la Licencia GPLv3 o >.


Referencias
===========
* https://docs.mx-os.mx/
* https://d2lang.com/

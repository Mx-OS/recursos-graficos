.. image:: logo/logo_horizontal.svg
   :alt: Logotipo Oficial de la Fundación MxOS
   :align: center
   :width: 260px

============================================
Recursos Gráficos de la Fundación MxOS
============================================

Acervo oficial de identidad visual, logotipos maestros de producción, manual de marca, fondos de pantalla y diagramas de arquitectura de la `Fundación MxOS <https://mx-os.mx/>`_.

Estructura
==========

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Directorio
     - Descripción
   * - ``logo/``
     - Logotipos maestros oficiales en SVG y versiones rasterizadas, basados en la propuesta comunitaria **a2** de `@fitorec <https://gitlab.com/fitorec>`_.
   * - ``wallpapers/``
     - Fondos de pantalla e ilustraciones para el entorno de escritorio.
   * - ``diagramas/``
     - Diagramas declarativos de arquitectura y soberanía técnica en D2.
   * - ``source/``
     - Fuentes del *Manual de Identidad Visual* en Sphinx.
   * - ``posters/``
     - Carteles de difusión institucional y comunitaria.
   * - ``propuestas_logotipo/``
     - Acervo histórico del concurso comunitario de diseño.

Compilación
===========

Requisitos: GNU Make, Python 3 con CairoSVG, D2 y Sphinx.

.. code-block:: bash

   make              # Compila logotipos, fondos y diagramas
   make logo         # Rasteriza variantes del logotipo en logo/output/
   make wallpapers   # Genera fondos QHD (2560x1440) en wallpapers/output/
   make diagramas    # Genera diagramas en PNG, SVG y PDF
   make manual-html  # Compila el manual Sphinx en source/_build/html/
   make clean        # Limpia archivos generados

Licencia
========

* **Herramientas y scripts:** GPL-3.0-or-later (`LICENSE <LICENSE>`_).
* **Arte, diagramas y fondos:** CC-BY-SA-4.0 (`LICENSES/ <LICENSES/>`_).
* **Marca:** El nombre y los distintivos visuales están reservados conforme a las políticas de la Fundación MxOS.

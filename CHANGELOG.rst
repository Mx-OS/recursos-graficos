=========
Changelog
=========

Todos los cambios notables en este proyecto se documentan en este archivo.

El formato está basado en `Keep a Changelog <https://keepachangelog.com/es-ES/1.1.0/>`_,
y este proyecto se adhiere a `Semantic Versioning <https://semver.org/lang/es/>`_.

[Unreleased]
============

.. rubric:: Added

- Directorio ``brochures/`` con el folleto ejecutivo de una página (``folleto-ejecutivo.svg``) y el tríptico plegable de doble cara (``triptico-exterior.svg`` y ``triptico-interior.svg``) organizados por capas editables de Inkscape y tipografía ``Liberation Mono``.
- Códigos QR vectoriales e hipervínculos interactivos (``<a>``) en todos los enlaces y códigos QR de los folletos y trípticos.
- Disposición en zigzag de los códigos QR en el folleto ejecutivo y en el panel de enlaces del tríptico para facilitar su lectura individual con cámara.
- Meta ``brochures`` en ``GNUmakefile`` y artefactos ``brochures/output/`` en ``.gitlab-ci.yml``.

.. rubric:: Changed

- Enfoque editorial del folleto y del tríptico orientado a la comunidad de software libre, estudiantes, jugadores en Linux/Steam y aprendizaje colaborativo de empaquetado e infraestructura en México.
- Imagen principal en ``README.rst`` apuntando directamente al logotipo oficial ``logo/a2.svg``.
- Documentación de paleta de color y tipografía en ``logo/README.rst`` alineada con los trazos y tonos reales de ``a2.svg``.

.. rubric:: Fixed

- Reconstrucción de las variantes en ``logo/`` (``isotipo.svg``, ``logo_fondo_blanco.svg``, ``logo_fondo_negro.svg``, ``logo_horizontal.svg``, ``logo_sub_horizontal.svg``, ``logo_vertical.svg``, ``logo_sub_vertical.svg`` y ``pattern.svg``) a partir de la geometría exacta de ``logo/a2.svg`` de ``@fitorec``, eliminando los trazos ajenos con texto marcador ``NAME`` y los biseles distorsionados en la versión oscura.

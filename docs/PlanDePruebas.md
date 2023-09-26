# Plan de Pruebas
**Introducción**

Este documento describe el plan de pruebas para el proyecto Modeulo de Seguimiento a Estudiantes. El objetivo de este plan es establecer los criterios, las actividades, los recursos y las herramientas necesarias para realizar y documentar las pruebas del software desarrollado.


**Entity: Student**

*Crear estudiante valido*

| test | Precondición | Attributes | Resultado |
| --- | --- | --- | --- |
| 1 | Base de datos disponible | String: name, code, id, email, phone, Date: birth, Int: ICFES, Donor: code   | estudiante creado |
| 2 | Base de datos no disponible | String: name, code, id, email, phone, Date: birth, Int: ICFES, Donor: code    | estudiante creado  |
| 3 | Base de datos disponible | tring: name, code, id, email, phone, Date: birth, Int: ICFES | estudiante no creado |

*Crear estudiante con codigo repetido*


| test | Precondición | Attributes | Resultado |
| --- | --- | --- | --- |
| 1 | Base de datos disponible | String: name, code = 123, id, email, phone, Date: birth, Int: ICFES, Donor: code   | estudiante creado |
| 2 | Base de datos disponible | String: name, code = 123, id, email, phone, Date: birth, Int: ICFES, Donor: code    | estudiante no creado  |


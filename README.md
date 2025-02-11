# Project Platzi Fake Store API


# **Descripción del proyecto**

Platzi Fake Store es una API simulada proporcionada por Platzi. La API se puede utilizar 
con cualquier tipo de proyecto que necesite productos, usuarios, categorías, autenticación y usuarios en formato
JSON.

En este proyecto, utilicé la API pública de FakeAPI Platzi (https://fakeapi.platzi.com/en/rest/products/) para realizar 
pruebas de funcionalidad y validar los métodos HTTP más comunes: GET, POST, PUT y DELETE. El objetivo fue practicar y 
demostrar mi capacidad para interactuar con APIs REST, asegurando el correcto funcionamiento de los endpoints y la 
integridad de los datos. Para ello, combiné el uso de Postman para pruebas manuales y exploratorias, y Python en PyCharm 
para automatizar y profundizar en las validaciones.

## Actividades realizadas

### Pruebas con GET:
- Obtuve la lista completa de productos.
- Validé la respuesta JSON, verificando la estructura de los datos y los códigos de estado HTTP.
- Realicé consultas específicas para obtener un producto por su ID.

### Pruebas con POST:
- Creé nuevos productos enviando datos en formato JSON.
- Verifiqué que los productos se añadieran correctamente y que los campos obligatorios fueran validados.

### Pruebas con PUT:
- Actualicé información de productos existentes, modificando campos como nombre, precio y descripción.
- Confirmé que los cambios se reflejaran correctamente en la base de datos.

### Pruebas con DELETE:
- Eliminé productos específicos por su ID.
- Validé que los productos fueran removidos correctamente y que la API retornara el código de estado adecuado.

## Herramientas utilizadas:

- Postman: Para diseñar, ejecutar y automatizar las pruebas. 
- FakeAPI Platzi: Como entorno de práctica para interactuar con una API RESTful real.
- PyCharm: Como entorno de desarrollo para escribir scripts en Python.
- Python: Para automatizar pruebas, utilizando librerías como requests para interactuar con la API y pytest
para estructurar y ejecutar los casos de prueba.

## Resultados:

- Validé el correcto funcionamiento de los métodos HTTP en la API.
- Automaticé pruebas para reducir tiempos de ejecución y aumentar la cobertura de testing.
- Documenté los casos de prueba.
- Aseguré la coherencia y calidad de los datos en cada operación.
- Este proyecto me permitió fortalecer mis habilidades en pruebas de APIs, comprensión de arquitecturas REST y uso de herramientas como Postman para garantizar la calidad del software.

# Laboratorio 08 Implementación de servicios web con Django

## Propósito y resultado
La aplicación quiz del proyecto GLAB-S03-Meneses se amplió con una API REST para exámenes, preguntas y opciones. Se conservaron los modelos y las vistas HTML existentes. Se verificaron siete pruebas automáticas y 32 solicitudes HTTP reales. La interfaz navegable se probó con un examen temporal: listar, consultar, crear, modificar parcialmente y eliminar.

Estudiante: Pamela Meneses. Confirmar el nombre completo y agregar los integrantes y sus aportes antes de presentar el informe. Fecha de ejecución: 26 de octubre de 2026. Curso: Desarrollo de Aplicaciones Empresariales.

## 1 Preparación y dependencias
El entorno venv anterior no podía ejecutarse porque apuntaba a una instalación de Python ausente. Se creó .venv-lab08 con Python 3.12. Se instalaron Django 5.2.18, Django REST Framework 3.18.3, django-jazzmin 3.0.5 y Pillow 13.0.0. Pillow es necesario por los campos ImageField de las otras aplicaciones. requirements.txt registra las dependencias. Se añadió rest_framework a INSTALLED_APPS. No hicieron falta cambios de modelos ni migraciones nuevas.

Desde la terminal de VS Code, ubicada en C:\Users\pamel\GLAB-S03-Meneses:
```powershell
.\.venv-lab08\Scripts\python.exe manage.py check
.\.venv-lab08\Scripts\python.exe manage.py test quiz --noinput
.\.venv-lab08\Scripts\python.exe manage.py runserver 127.0.0.1:8008
```
Si el servidor ya está ejecutándose en ese puerto, no inicies otro. Para detenerlo, usa Ctrl+C en su terminal. El entorno nuevo se puede seleccionar en VS Code con Python: Select Interpreter y la ruta .venv-lab08/Scripts/python.exe.

## 2 Configuración de la API
REST_FRAMEWORK utiliza PageNumberPagination con PAGE_SIZE igual a 5, SearchFilter y permisos AllowAny para esta práctica local. Las peticiones de escritura no requieren iniciar sesión. El servidor escucha solamente en 127.0.0.1. La clave SECRET_KEY se obtiene de DJANGO_SECRET_KEY o se genera temporalmente; para conservar sesiones entre reinicios debe definirse una clave estable en una variable de entorno. No hay credenciales escritas en settings.py.

## 3 Serializadores y campos
ExamSerializer, QuestionSerializer y ChoiceSerializer derivan de ModelSerializer. Exam expone id, title, description y created_at; id y created_at son de solo lectura. Question expone id, exam, text, score y choices; id es de solo lectura. Choice expone id, question, text e is_correct; id es de solo lectura. NestedChoiceSerializer expone las opciones dentro de la pregunta.

## 4 Relaciones y escritura anidada
El examen de una pregunta se envía por su identificador en exam. Las opciones se incluyen como una lista de objetos en choices. Al crear la pregunta, se guardan la pregunta y sus opciones en una transacción. Si PATCH omite choices, las opciones actuales se conservan. Si PATCH o PUT incluye choices, la lista completa reemplaza las opciones anteriores y se generan identificadores nuevos. Para cambiar cuál opción es correcta, se envía la lista completa en el endpoint de la pregunta.

Ejemplo de creación de pregunta, usando un identificador de examen existente:
```json
{"exam": 1, "text": "What is Django?", "score": 2, "choices": [{"text": "Web framework", "is_correct": true}, {"text": "Database", "is_correct": false}]}
```

## 5 Validación propia
La suma de opciones con is_correct verdadero debe ser exactamente uno. Una lista vacía, ninguna correcta o dos correctas producen HTTP 400. La validación se ejecuta antes de guardar. También se impide crear una segunda opción correcta, eliminar la única correcta o mover una opción a otra pregunta desde el recurso choices. Se permite añadir, editar o eliminar distractores. Estas restricciones protegen la coherencia de los datos expuestos por la API.

## 6 Vistas y rutas
ExamViewSet, QuestionViewSet y ChoiceViewSet derivan de ModelViewSet. DefaultRouter registra exams, questions y choices. config/urls.py incluye quiz.api_urls bajo api/. La raíz http://127.0.0.1:8008/api/ muestra los tres recursos. La aplicación web original sigue disponible en http://127.0.0.1:8008/.

## 7 Comprobación en la API navegable
Se comprobó la lista de exámenes con HTTP 200, se creó el examen temporal LAB08 browser evidence con HTTP 201, se consultó su detalle con HTTP 200, se modificó su descripción mediante Raw data y PATCH con HTTP 200 y se eliminó con HTTP 204. Las capturas guardadas corresponden a operaciones reales. El examen temporal ya fue eliminado.

Para repetirlo en el navegador: abre /api/exams/, escribe un título y pulsa POST. Anota el id devuelto y abre /api/exams/ID/. Selecciona Raw data, reemplaza el contenido por {"description":"Actualizado"} y pulsa PATCH. Después utiliza DELETE y confirma solo sobre el registro temporal creado para la prueba. Para preguntas utiliza Raw data con el JSON anidado de la sección anterior. Para opciones utiliza {"question": ID, "text":"Distractor adicional", "is_correct":false}.

## 8 Cliente HTTP externo
El script docs/lab08/verify_http.py usa urllib.request desde un proceso separado y se conecta por HTTP al servidor real. Ejecuta las cinco operaciones sobre los tres recursos, valida códigos y contenido, prepara siete preguntas para comprobar paginación y finalmente elimina sus datos temporales. No utiliza el cliente interno de Django para esas comprobaciones.
```powershell
.\.venv-lab08\Scripts\python.exe docs/lab08/verify_http.py
```
La colección Lab08.postman_collection.json permite repetir operaciones en Postman, en orden. Importa el archivo y conserva base_url como http://127.0.0.1:8008. Los identificadores se actualizan después de crear cada recurso. Para comprobar más de una página usa el script, que crea el conjunto completo de siete preguntas antes de limpiarlo.

## 9 Errores controlados
Campo obligatorio ausente: POST /api/exams/ con {} devuelve HTTP 400 y un error asociado a title. Tipo incorrecto: POST /api/questions/ con score igual a "abc" devuelve HTTP 400 y un error asociado a score. Regla propia: enviar choices sin exactamente una opción correcta devuelve HTTP 400 y el mensaje A question must have exactly one correct choice. También se probó el caso de dos opciones correctas y la protección contra eliminar la correcta. Los mensajes completos de esta ejecución están en Resultados-HTTP.json.

## 10 Filtrado búsqueda y paginación
GET /api/questions/?exam=ID filtra por examen. GET /api/questions/?search=Python busca por texto del enunciado. Ambos parámetros se pueden combinar. GET /api/questions/?exam=ID&page=2 obtiene la segunda página. Las listas devuelven count, next, previous y results. Con siete preguntas del examen temporal, la primera página devolvió cinco y la segunda dos. La búsqueda Python encontró seis. exam=abc devuelve HTTP 400. Los identificadores exactos del ensayo constan en el registro JSON.

## 11 Tabla de la API
Base: http://127.0.0.1:8008. Sustituir ID por el identificador real. En todas las escrituras se envía Content-Type: application/json.

| Recurso | Dirección | Método | Cuerpo de ejemplo | Respuesta esperada |
|---|---|---|---|---|
| exams | /api/exams/ | GET | Sin cuerpo | 200; count, next, previous, results |
| exams | /api/exams/ID/ | GET | Sin cuerpo | 200; objeto JSON |
| exams | /api/exams/ | POST | {"title":"Sample exam","description":"Practice"} | 201; objeto creado |
| exams | /api/exams/ID/ | PATCH | {"description":"Updated"} | 200; objeto actualizado |
| exams | /api/exams/ID/ | DELETE | Sin cuerpo | 204; sin cuerpo |
| questions | /api/questions/ | GET | Sin cuerpo | 200; count, next, previous, results |
| questions | /api/questions/ID/ | GET | Sin cuerpo | 200; objeto JSON |
| questions | /api/questions/ | POST | {"exam":1,"text":"Question?","score":1,"choices":[{"text":"Yes","is_correct":true}]} | 201; objeto creado |
| questions | /api/questions/ID/ | PATCH | {"score":3} | 200; objeto actualizado |
| questions | /api/questions/ID/ | DELETE | Sin cuerpo | 204; sin cuerpo |
| choices | /api/choices/ | GET | Sin cuerpo | 200; count, next, previous, results |
| choices | /api/choices/ID/ | GET | Sin cuerpo | 200; objeto JSON |
| choices | /api/choices/ | POST | {"question":1,"text":"Wrong option","is_correct":false} | 201; objeto creado |
| choices | /api/choices/ID/ | PATCH | {"text":"Updated wrong option"} | 200; objeto actualizado |
| choices | /api/choices/ID/ | DELETE | Sin cuerpo | 204; sin cuerpo |

PUT también está disponible para reemplazar el recurso completo y devuelve 200 si el cuerpo es válido. Si un recurso no existe, GET, PATCH y DELETE devuelven 404. Los datos inválidos devuelven 400. DELETE de una opción correcta devuelve 400; primero debe reemplazarse la lista de opciones de la pregunta.

## 12 Resultados de las pruebas
Las siete pruebas automáticas verifican creación anidada, campos de solo lectura, cero o varias correctas, campos obligatorios, tipos inválidos, PATCH, protección de opciones, filtros, paginación y borrado en cascada. Se ejecutan sobre una base temporal que Django elimina al terminar. Los 32 controles HTTP reales finalizaron con el código esperado.

| Caso | Método | Código esperado | Código obtenido |
|---|---|---|---|
| Browsable API root | GET | 200 | 200 |
| Create exam | POST | 201 | 201 |
| List exams | GET | 200 | 200 |
| Exam detail | GET | 200 | 200 |
| Update exam | PATCH | 200 | 200 |
| Create question | POST | 201 | 201 |
| List questions | GET | 200 | 200 |
| Question detail | GET | 200 | 200 |
| Update question | PATCH | 200 | 200 |
| Create choice | POST | 201 | 201 |
| List choices | GET | 200 | 200 |
| Choice detail | GET | 200 | 200 |
| Update choice | PATCH | 200 | 200 |
| Delete choice | DELETE | 204 | 204 |
| Missing required field | POST | 400 | 400 |
| Incorrect field type | POST | 400 | 400 |
| Zero correct choices | POST | 400 | 400 |
| Two correct choices | POST | 400 | 400 |
| Protect correct choice | DELETE | 400 | 400 |
| Pagination fixture 1 | POST | 201 | 201 |
| Pagination fixture 2 | POST | 201 | 201 |
| Pagination fixture 3 | POST | 201 | 201 |
| Pagination fixture 4 | POST | 201 | 201 |
| Pagination fixture 5 | POST | 201 | 201 |
| Pagination fixture 6 | POST | 201 | 201 |
| Filter by exam | GET | 200 | 200 |
| Search question text | GET | 200 | 200 |
| Second page | GET | 200 | 200 |
| Browsable questions | GET | 200 | 200 |
| Delete question | DELETE | 204 | 204 |
| Deleted question | GET | 404 | 404 |
| Delete exam and temporary data | DELETE | 204 | 204 |

## 13 Capturas que debes incorporar
Captura 1: VS Code mostrando la estructura quiz, serializers.py, api_views.py, api_urls.py, tests.py y config/urls.py. Debe verse el nombre de la carpeta del proyecto.

Captura 2: terminal con manage.py check y manage.py test quiz mostrando siete pruebas y OK. Explicación: la configuración no presenta errores y los casos de validación pasan.

Captura 3: raíz /api/ con los enlaces exams, questions y choices. Ya se guardó una captura real de referencia.

Captura 4: respuesta POST con HTTP 201 y el objeto creado. Ya se guardó una captura real de creación de examen.

Captura 5: detalle con opciones anidadas y exam como número. Abre /api/questions/1/ para ver los datos existentes.

Captura 6: PATCH con HTTP 200 y el campo modificado. Ya se guardó una captura real.

Captura 7: DELETE con HTTP 204 sobre un registro de prueba. Ya se guardó una captura real.

Captura 8: terminal ejecutando verify_http.py o Postman con los resultados y códigos. El script imprime cada operación y al final PASS: 32 HTTP checks.

Captura 9: tres respuestas 400: título ausente, score inválido y número de respuestas correctas distinto de uno. En Postman puedes repetir las solicitudes Missing required field, Incorrect field type y Zero correct choices.

Captura 10: paginación, filtro y búsqueda. Para capturar datos antes de su limpieza, ejecuta el script con el depurador y coloca un punto de interrupción antes de Delete question; abre el examen temporal cuyo id aparece en la terminal. Alternativamente crea siete preguntas propias en un examen de prueba.

Para cada evidencia incluye nombre del estudiante, título del desarrollo, captura, código relevante, explicación y casos de prueba. Las capturas guardadas de navegador son estrechas porque corresponden al panel integrado; puedes repetirlas con Chrome maximizado para mejorar su lectura.

## 14 Código que debes explicar
quiz/serializers.py contiene los ModelSerializer, validate, create y update con transacciones. quiz/api_views.py contiene los ModelViewSet y el filtro por exam. quiz/api_urls.py registra los tres recursos en DefaultRouter. config/settings.py registra el framework, los permisos, la búsqueda y la paginación. quiz/tests.py contiene la verificación automática. Adjunta estos archivos o pega sus fragmentos junto a las capturas que los demuestren.

## 15 Conclusiones
La API permite administrar los tres recursos por HTTP y devolver representaciones JSON consistentes. La serialización anidada facilita crear preguntas con sus opciones en una sola operación. La validación impide guardar preguntas sin exactamente una respuesta correcta desde la API. Los códigos 200, 201, 204, 400 y 404 permiten diferenciar consultas, creación, eliminación, errores de entrada y recursos inexistentes. El filtrado, la búsqueda y la paginación facilitan consultar conjuntos de preguntas.

## 16 Entrega y responsabilidades
El repositorio del proyecto es https://github.com/pamelameneses-code/GLAB-S03-Meneses-D.E. Agrega la distribución real de trabajo del equipo y comprueba el plazo del campus virtual. La carga final al campus y las capturas personales se deben completar antes de entregar. No incluyas contraseñas, db.sqlite3 ni los entornos virtuales en Git.

## Referencias
Guía del laboratorio GLAB-S08-MMONTGOMERY-2026-02.docx proporcionada por el curso.
https://www.django-rest-framework.org/api-guide/serializers/
https://www.django-rest-framework.org/api-guide/viewsets/
https://www.django-rest-framework.org/api-guide/filtering/

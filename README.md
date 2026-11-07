# GLAB S03 Meneses

Proyecto acumulativo de Desarrollo de Aplicaciones Empresariales. El laboratorio 06 implementa un portal de noticias con el motor de plantillas de Django.

## Puesta en marcha

Desde la carpeta del proyecto, con Python 3.12 o superior:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py seed_news_demo
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Abre [el portal](http://127.0.0.1:8000/news/) o [la administración](http://127.0.0.1:8000/admin/). Si ya tienes un superusuario local, omite `createsuperuser`. La carga de ejemplo se puede repetir sin duplicar las noticias. En una base nueva crea seis publicaciones ficticias, dos por categoría en General, Cultura y Tecnología.

Los archivos de `staticfiles/` se generan con `collectstatic`. Las hojas de estilo fuente están versionadas. Los archivos subidos durante el desarrollo se guardan en `media/`.

## Plantillas y administración

- `news/templates/news/base.html` define los bloques `title`, `content` y `sidebar` y carga la hoja de estilos con `static`.
- `_article_card.html` se incluye en la portada y en los listados por categoría. Usa `date` para la fecha y `truncatewords:20` para el resumen. Los listados usan `for … empty`.
- El detalle muestra el autor, la fecha, un enlace a la categoría y la imagen destacada cuando está disponible. Las tres vistas se enlazan con rutas con nombre.
- En el admin se pueden filtrar categorías por el estado de publicación de sus noticias y autores por las categorías de sus noticias. La búsqueda admite nombre y slug en categorías, y nombre y biografía en autores.

## Verificación del laboratorio 06

Ejecuta `python manage.py test news` con el entorno activo. Las pruebas cubren la reutilización de la tarjeta, el recorte, los estados vacíos, la exclusión de borradores, el escapado y los filtros y búsquedas del admin.

| Caso | Resultado esperado | Evidencia |
| --- | --- | --- |
| Abrir la portada con los datos de ejemplo | Seis tarjetas, fechas formateadas y enlaces a tres categorías. | [Portada](docs/lab06/capturas/01-portada.jpg) |
| Entrar a Tecnología desde la barra lateral | Dos noticias de la categoría, con el mismo formato de tarjeta. | [Categoría](docs/lab06/capturas/02-categoria.jpg) |
| Abrir la noticia del prototipo ambiental | Cargan la imagen y el cuerpo. Se ve el texto literal `<strong>medición de prueba</strong>` porque Django escapa los caracteres HTML antes de que el navegador interprete el contenido. | [Detalle y escapado](docs/lab06/capturas/03-detalle-y-escape.jpg) |
| Abrir la lista de noticias en el admin | Se pueden editar las seis publicaciones y filtrar por categoría o estado. | Verificación local en el admin |
| Quitar la publicación de todas las noticias de una categoría | El listado muestra el mensaje de estado vacío y el detalle de cada borrador devuelve 404. | Pruebas automatizadas |

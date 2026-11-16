# Laboratorio 12 Servicios web con Django y React

Pamela Meneses · Desarrollo de Aplicaciones Empresariales

El cliente del laboratorio 11 se copió a `lab12/frontend`. La API de Django del laboratorio 8 permanece en la raíz del repositorio. Se eligió el recurso Exámenes, que admite listado, alta y borrado.

## Cómo ejecutar la aplicación

Con Python 3.12 o superior y Node.js 20 o superior, desde la raíz del repositorio:

```powershell
python -m venv .venv-lab12
.\.venv-lab12\Scripts\python.exe -m pip install -r requirements.txt
.\.venv-lab12\Scripts\python.exe manage.py migrate
.\.venv-lab12\Scripts\python.exe manage.py runserver 127.0.0.1:8000
```

En otra terminal, también desde la raíz:

```powershell
cd lab12/frontend
npm ci
npm run dev
```

Django responde en http://127.0.0.1:8000/api/. La raíz de la API enlaza a `exams/`, `questions/` y `choices/`. React corre en http://127.0.0.1:5190 y el listado está en http://127.0.0.1:5190/#exams. Usa la dirección 127.0.0.1 tal como aparece aquí. Django autoriza únicamente ese origen de React para rutas bajo /api/. El cliente Axios centraliza la URL base en `src/api/exams.js`, con opción de definir `VITE_API_URL`.

## Desarrollo y pruebas

| Desarrollo | Ubicación | Resultado |
|---|---|---|
| Origen autorizado | config/settings.py y requirements.txt | La raíz respondió 200. Django envió Access-Control-Allow-Origin para 127.0.0.1:5190 y omitió la cabecera para un origen distinto. |
| Listado | lab12/frontend/src/api/exams.js y src/components/Exams/Exams.jsx | Al entrar, React solicita GET /api/exams/. Axios reúne las páginas de resultados. Después del alta, el examen temporal apareció en la tabla. |
| Alta | ExamForm en Exams.jsx | POST /api/exams/ devolvió 201. El formulario volvió al listado sin recargar la página. |
| Validación | ExamForm en Exams.jsx | Con título vacío, Django devolvió 400 con «Este campo no puede estar en blanco.» y React lo mostró debajo del campo. |
| Borrado | ExamList en Exams.jsx | DELETE /api/exams/{id}/ devolvió 204 en la prueba de la API. Desde React, el registro temporal desapareció del listado. |
| Bloqueo por origen | CORS en Django y estado de error de ExamList | Al ejecutar el mismo cliente en 127.0.0.1:5191, el origen no estaba autorizado. La interfaz mostró el aviso de conexión y Reintentar. Al volver a 5190, el listado respondió. |

El cliente pasó npm run lint y npm run build.

| Estado al entrar o reintentar | Qué muestra la pantalla |
|---|---|
| Carga | «Cargando exámenes…» y un bloque que indica la espera. |
| Datos | Tabla con título, descripción y acción Eliminar. Si la lista está vacía, muestra cómo crear el primer examen. |
| Error | Explica que React no pudo conectar con la API, indica revisar Django y el origen, y ofrece Reintentar. |

## Evidencias para el entregable

- Alta exitosa y validación del título vacío. Ambas vistas se capturaron durante la comprobación del cliente.
- Origen rechazado en 5191. Se capturó el aviso de React. Para la evidencia específica de consola que pide la guía, abre las herramientas del navegador, selecciona Consola y recarga el listado con el origen temporalmente excluido. Después restáuralo.
- Servidor apagado. Se detuvo Django con Vite abierto y se recargó el listado. React mostró el mensaje de conexión y Reintentar. Se inició Django y se pulsó Reintentar. React recuperó el listado sin recargar la página.
- Incluye una captura del explorador del editor con config, quiz y lab12/frontend/src. Para la carga rápida, puedes aplicar latencia desde las herramientas del navegador antes de recargar.

## Conclusiones

Separar el cliente Axios permitió que el formulario y el listado usen la misma dirección base. La API se encargó de validar el título obligatorio y React mostró el mensaje junto al campo. Autorizar un origen exacto permitió comprobar el acceso del cliente previsto y observar qué ocurre cuando el mismo cliente se ejecuta desde otro puerto.

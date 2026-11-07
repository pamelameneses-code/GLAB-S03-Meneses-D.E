from datetime import datetime
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify

from news.models import Article, Author, Category


DEMO_ARTICLES = (
    (
        "General",
        "Lanzamiento de la nueva plataforma digital",
        "El portal reúne las novedades del laboratorio y permite consultar "
        "noticias por categoría desde una portada común.",
        "La plataforma centraliza las publicaciones y sus categorías. "
        "Cada noticia tiene una página con la fecha, el autor y el contenido completo.",
    ),
    (
        "General",
        "La biblioteca amplía su horario de atención",
        "La biblioteca suma un turno para que los estudiantes puedan consultar "
        "material y reservar espacios de estudio durante las tardes.",
        "La atención de tarde incluye préstamo de libros y orientación para "
        "encontrar material de consulta. Las reservas se coordinan con la biblioteca.",
    ),
    (
        "Tecnología",
        "Estudiantes presentan un prototipo de monitoreo ambiental",
        "El equipo instaló sensores de humedad y temperatura en un huerto de "
        "prácticas para comparar las mediciones de distintas zonas durante la semana.",
        "El prototipo registra la temperatura y la humedad a intervalos regulares. "
        "Los estudiantes compararán las lecturas para decidir dónde colocar los sensores "
        "en la siguiente prueba.\n\nPrueba de escapado: <strong>medición de prueba</strong>.",
    ),
    (
        "Tecnología",
        "Un taller introduce el control de versiones con Git",
        "Los participantes practican cómo guardar cambios en pasos pequeños, "
        "consultar el historial del proyecto y resolver diferencias entre dos ramas.",
        "El taller empieza con un repositorio local. Cada participante crea una "
        "rama, guarda un cambio y revisa el historial antes de integrar su aporte.",
    ),
    (
        "Cultura",
        "La comunidad inaugura una muestra de fotografía urbana",
        "La exposición reúne imágenes de calles y mercados tomadas durante "
        "recorridos por la ciudad, con fichas que describen los lugares fotografiados.",
        "Las fotografías exploran escenas cotidianas de la ciudad. La muestra "
        "incluye un espacio para que los autores comenten sus decisiones de encuadre.",
    ),
    (
        "Cultura",
        "El club de lectura abre un ciclo de cuentos peruanos",
        "El club propone leer y comentar un cuento por encuentro. La primera "
        "reunión incluye una conversación sobre los personajes, el lugar y la narración.",
        "El ciclo está pensado para estudiantes que quieran conversar sobre "
        "cuentos breves. Cada sesión empieza con la lectura de un fragmento.",
    ),
)

IMAGE_SLUG = "estudiantes-presentan-un-prototipo-de-monitoreo-ambiental"
IMAGE_PATH = Path(__file__).resolve().parents[2] / "demo" / "monitoreo-ambiental.png"


class Command(BaseCommand):
    help = "Carga las seis noticias de ejemplo del laboratorio 06."

    def handle(self, *args, **options):
        created_count = 0
        with transaction.atomic():
            author = Author.objects.filter(name="Admin").order_by("pk").first()
            if author is None:
                author = Author.objects.create(name="Admin")

            for day, (category_name, title, summary, content) in enumerate(
                DEMO_ARTICLES, start=14
            ):
                category, _ = Category.objects.get_or_create(
                    slug=slugify(category_name),
                    defaults={"name": category_name},
                )
                article, created = Article.objects.get_or_create(
                    slug=slugify(title),
                    defaults={
                        "title": title,
                        "summary": summary,
                        "content": content,
                        "category": category,
                        "author": author,
                        "published_at": timezone.make_aware(datetime(2026, 10, day, 9)),
                        "is_published": True,
                    },
                )
                created_count += created
                if article.slug == IMAGE_SLUG and not article.featured_image:
                    with IMAGE_PATH.open("rb") as image:
                        article.featured_image.save(IMAGE_PATH.name, File(image))

        self.stdout.write(self.style.SUCCESS(f"Noticias nuevas: {created_count}."))

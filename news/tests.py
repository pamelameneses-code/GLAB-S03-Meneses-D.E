from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Article, Author, Category


class NewsPortalTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="Tecnología", slug="tecnologia")
        cls.empty_category = Category.objects.create(name="Cultura", slug="cultura")
        cls.author = Author.objects.create(name="Ana Vega")
        cls.article = Article.objects.create(
            title="Noticias del laboratorio",
            slug="noticias-del-laboratorio",
            summary=" ".join(["avance"] * 20 + ["palabraomitida"]),
            content="<strong>Texto literal</strong>",
            published_at=timezone.now(),
            category=cls.category,
            author=cls.author,
        )
        cls.draft = Article.objects.create(
            title="Borrador privado",
            slug="borrador-privado",
            summary="Resumen privado",
            content="Contenido privado",
            published_at=timezone.now(),
            is_published=False,
            category=cls.empty_category,
            author=cls.author,
        )

    def test_home_and_category_reuse_article_card(self):
        for url in (
            reverse("news:article_list"),
            reverse("news:category_articles", args=[self.category.slug]),
        ):
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertTemplateUsed(response, "news/base.html")
                self.assertTemplateUsed(response, "news/_article_card.html")
                self.assertContains(response, self.article.title)
                self.assertContains(response, " ".join(["avance"] * 20))
                self.assertNotContains(response, "palabraomitida")
                self.assertNotContains(response, self.draft.title)

    def test_empty_category_and_home(self):
        response = self.client.get(
            reverse("news:category_articles", args=[self.empty_category.slug])
        )
        self.assertContains(response, "No hay artículos en esta categoría.")

        Article.objects.filter(pk=self.article.pk).update(is_published=False)
        response = self.client.get(reverse("news:article_list"))
        self.assertContains(response, "No hay artículos publicados por el momento.")

    def test_detail_escapes_html_and_hides_drafts(self):
        response = self.client.get(reverse("news:article_detail", args=[self.article.slug]))
        self.assertTemplateUsed(response, "news/base.html")
        self.assertContains(response, "&lt;strong&gt;Texto literal&lt;/strong&gt;")
        self.assertNotContains(response, "<strong>Texto literal</strong>")
        self.assertContains(response, self.author.name)
        self.assertContains(response, self.category.name)
        response = self.client.get(reverse("news:article_detail", args=[self.draft.slug]))
        self.assertEqual(response.status_code, 404)

    def test_admin_category_and_author_search_and_filter(self):
        admin = get_user_model().objects.create_superuser(
            username="news-admin", password="test-password"
        )
        self.client.force_login(admin)

        response = self.client.get(
            reverse("admin:news_category_changelist"),
            {"q": "Tecnología", "articles__is_published__exact": "1"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["cl"].result_list), [self.category])
        self.assertTrue(response.context["cl"].has_active_filters)

        response = self.client.get(
            reverse("admin:news_author_changelist"),
            {"q": "Ana", "articles__category__id__exact": self.category.pk},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["cl"].result_list), [self.author])
        self.assertTrue(response.context["cl"].has_active_filters)

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django_summernote.models import AbstractAttachment

from apps.utils.files import resize_image, upload_to
from apps.utils.rands import custom_slugify


class PostManager(models.Manager):
    def get_published(self):
        return (self
                .filter(is_published=True)
                .order_by('-pk'))


class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255, default=None,
        null=True, unique=True
    )

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.name)

        return super().save(*args, **kwargs)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255, default=None,
        null=True, unique=True
    )

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.name)

        return super().save(*args, **kwargs)


class Page(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField(
        max_length=255, default=None,
        null=True, unique=True
    )
    content = models.TextField()
    is_published = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        return reverse('blog:page', args=(self.slug,))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)

        return super().save(*args, **kwargs)


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    objects = PostManager()

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        max_length=255, default=None, blank=True,
        null=True, unique=True
    )
    cover = models.ImageField(upload_to=upload_to, blank=True, default=None)
    cover_content = models.BooleanField(default=True)
    excerpt = models.CharField(max_length=150)
    content = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None
    )
    tags = models.ManyToManyField(Tag, blank=True, default='')
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                   null=True, blank=True, default=None,
                                   related_name='page_created_by'
                                   )
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                   null=True, blank=True, default=None,
                                   related_name='page_updated_by'
                                   )

    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        return reverse('blog:post', args=(self.slug,))

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title, 4)

        current_cover = str(self.cover.name)
        super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900)


class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        self.name = self.file.name
        super().save(*args, **kwargs)

        current_file = str(self.file.name)
        file_changed = False

        if self.file:
            file_changed = current_file != self.file.name

        if file_changed:
            resize_image(self.file, 900)

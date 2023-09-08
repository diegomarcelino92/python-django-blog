import string
from random import SystemRandom

from django.utils.text import slugify


def random_letter(k=4):
    random_list = SystemRandom().choices(
        string.ascii_lowercase + string.digits, k=k
    )

    return ''.join(random_list)


def custom_slugify(text, count=4):
    return slugify(text + random_letter(count))

from .models import *
from modeltranslation.translator import register, TranslationOptions

@register(Post)
class PersonTranslationOptions(TranslationOptions):
    fields = ('title', 'body')
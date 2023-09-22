from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from polls.models import Question

@receiver(post_save, sender=Question)
def invalidate_cached_question(sender, instance, **kwargs):
    cache.delete("latest_question_list")
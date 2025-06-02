from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import AddRequest, Record

@receiver(pre_save, sender=AddRequest)
def check_accepted_change(sender, instance, **kwargs):
    """
    Store the old accepted value in the instance if it exists
    """
    if instance.pk:
        try:
            old_instance = AddRequest.objects.get(pk=instance.pk)
            instance._old_accepted = old_instance.accepted
        except AddRequest.DoesNotExist:
            pass

@receiver(post_save, sender=AddRequest)
def create_record_on_approval(sender, instance, created, **kwargs):
    """
    Signal handler that creates a new Record when an AddRequest is approved.
    Only triggers when the 'accepted' field changes from False to True.
    """
    # Check if this is an update (not a new record)
    if not created and hasattr(instance, '_old_accepted'):
        # Check if accepted was just changed from False to True
        if instance.accepted and not instance._old_accepted:
            # Create a new Record from the AddRequest
            Record.objects.create(
                workTitle=instance.workTitle,
                workTitleKorean=instance.workTitleKorean,
                authorKorean=instance.authorKorean,
                authorEnglish=instance.authorEnglish,
                translator=instance.translator,
                genre=instance.genre,
                sourceTitle=instance.sourceTitle,
                publisher=instance.publisher,
                year=instance.year,
            )
    # Clean up the temporary attribute
    if hasattr(instance, '_old_accepted'):
        del instance._old_accepted
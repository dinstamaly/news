from celery import shared_task
from celery.utils.log import get_task_logger
from post.models import Post

logger = get_task_logger(__name__)

@shared_task
def sample_task():
    print('Test')
    logger.info("Test")
    Post.upvotes.through.objects.all().delete()

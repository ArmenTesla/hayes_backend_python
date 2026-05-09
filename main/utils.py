from .models import *
from django.db.models import Sum

def calculate_user_level(user):
    total_score = UserProfile.objects.filter(user=user).aggregate(total=Sum('score'))['total'] or 0

    config = LevelConfig.objects.last()
    percent = config.level_percent if config else 100

    adjusted_score = total_score * (percent / 100)
    level = int(adjusted_score // 50)

    return level, total_score
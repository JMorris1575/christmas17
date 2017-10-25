import random

import memory.models

def get_memory():
    return random.choice(memory.models.Memory.objects.all())


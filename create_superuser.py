import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='marekbecht').exists():
    User.objects.create_superuser('marekbecht', 'marek.becht@gmail.com', 'b1l2a3c4k0mb')
    print("Superuser created successfully")
else:
    print("Superuser already exists")

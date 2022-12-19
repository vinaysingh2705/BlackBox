from .dev import *
from dotenv import load_dotenv


load_dotenv(os.path.join(BASE_DIR, '.env'))

print("========================================")
print("========================================")
print(os.environ.get('DJANGO_DEVELOPMENT'))
print("========================================")
print("========================================")
if os.environ.get('DJANGO_DEVELOPMENT', 'False') == 'True':
    from .dev import *
else:
    from .test import *

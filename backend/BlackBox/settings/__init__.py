from .dev import *
from dotenv import load_dotenv


load_dotenv(os.path.join(BASE_DIR, '.env'))

if os.environ.get('DJANGO_DEVELOPMENT', 'False') == 'True':
    from .dev import *
else:
    from .test import *

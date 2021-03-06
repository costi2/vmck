import os
import string
import secrets
from datetime import datetime
from vmck.base_settings import *

def is_true(value):
    text = (value or '').lower().strip()
    return text in ['1', 'yes', 'true', 'on', 'enabled']


vocabulary_64 = string.ascii_letters + string.digits + '.+'

def random_code(length, vocabulary=vocabulary_64):
    return ''.join(secrets.choice(vocabulary) for _ in range(length))


SECRET_KEY = random_code(43)

DEBUG = is_true(os.environ.get('TESTING_DEBUG'))
VM_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

NOMAD_URL = os.environ.get('TESTING_NOMAD_URL', 'http://localhost:4646')
NOMAD_JOB_PREFIX = f'testsuite-{random_code(8)}-'
NOMAD_DEPLOYMENT_NAME = f"test {datetime.now().strftime('%H:%M:%S')}"

github_image = 'https://github.com/mgax/vmck-images/raw/master/bionic.qcow2'
QEMU_IMAGE_URL = os.environ.get('TESTING_QEMU_IMAGE_URL', github_image)
QEMU_IMAGE_USERNAME = 'ubuntu'

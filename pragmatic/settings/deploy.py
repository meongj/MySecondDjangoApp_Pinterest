from .base import *

#배포용

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)



# Take environment variables from .env file
environ.Env.read_env(
    env_file=(os.path.join(BASE_DIR, '.env'))
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# .env 파일에서 SECRET_KEY 읽어옴(git 업로드방지)
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# 모든 host에 대해 접근 허용함
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password1234',
        'HOST': 'mariadb',
        'PORT': '3306',
    }
}

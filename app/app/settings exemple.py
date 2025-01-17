# settings_example.py

# Configurações do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Secret key (mude isso para um valor único no seu ambiente local)
SECRET_KEY = 'sua_chave_secreta_aqui'

# Outras configurações do Django (por exemplo, configuração de email, armazenamento de arquivos, etc.)
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

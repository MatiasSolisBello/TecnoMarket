## Comandos clave

Verificar version de Python y Django respectivamente
```bash
python --version
python -m django --version
```

Crear entorno virtual.
```bash
virtualenv venv
source venv/bin/activate
 ```

Instalar Django / paquetes necesarios
```bash
pip install Django==3.1.2
pip install -r requirements.txt
```

Crear proyecto en la misma carpeta (Para eso esta el punto final) 
```bash
django-admin startproject <NombreProyecto> .
```
Conexión con Postgresql: [Leer](https://cosasdedevs.com/posts/como-conectar-una-base-de-datos-postgresql-con-django/)
```bash
sudo apt install libpq-dev
pip3 install psycopg2
```

Ejecutar servidor
```bash
python manage.py runserver
```

Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

Crear superusuario
```bash
python manage.py createsuperuser
```

## Usuarios

* admin / admin123
* alonso / heave-decompose  (se le asigna permiso view_producto) 
* Auth mediante Facebook

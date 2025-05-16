# Crecer México

Plataforma web para la organización Crecer México, enfocada en programas educativos, becas escolares y donaciones para apoyar a estudiantes.

## Estructura del proyecto

El proyecto está organizado en varias aplicaciones Django:

- **core**: Funcionalidades comunes y página de inicio
- **about**: Sección "¿Quiénes somos?"
- **projects**: Cursos, becas y programas
- **impact**: Estadísticas, testimonios e impacto
- **contact**: Formulario e información de contacto
- **donations**: Sistema de gestión de donaciones

## Configuración del entorno de desarrollo

1. Clona el repositorio:
```bash
git clone https://github.com/TU_USUARIO/crecer-mexico.git
cd crecer-mexico
```

2. Crea y activa un entorno virtual:
```bash
python -m venv venv

source venv/bin/activate  || En Windows: venv\Scripts\activate
```
3. Instala las dependencias:
```bash
pip install -r requirements.txt
```
4. Ejecuta las migraciones:
```bash
python manage.py migrate
```
5. Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

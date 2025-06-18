# scratchuser

`scratchuser` es una librería de Python creada por Vicente García Pastor para obtener información pública de perfiles de [Scratch](https://scratch.mit.edu) usando la API oficial `api.scratch.mit.edu`.

Te permite ver datos como:
- Biografía del usuario
- Estado
- País
- Imagen de perfil
- Fecha de creación del perfil
- Proyectos públicos
- Seguidores
- A quién sigue

---

## 🛠 Instalación

### Instalar desde PyPI (una vez publicada)

```bash
pip install scratchuser

Instalar desde tu código local (para desarrollo)

    Coloca el archivo setup.py y tu carpeta scratchuser/ en una misma carpeta.

    Abre la terminal dentro de esa carpeta y ejecuta:

pip install .

Esto instalará tu librería en el entorno actual de Python.
🚀 ¿Cómo se usa?
1. Importar la clase principal

from scratchuser.user import ScratchUser

2. Crear un objeto con el nombre de usuario

user = ScratchUser("griffpatch")  # Reemplaza con cualquier usuario de Scratch

3. Obtener datos del perfil

print("Usuario:", user.get_username())
print("Biografía:", user.get_bio())
print("Estado:", user.get_status())
print("País:", user.get_country())
print("Fecha de ingreso:", user.get_joined_date())
print("Imagen de perfil:", user.get_image())

4. Ver proyectos del usuario

projects = user.get_projects(limit=3)
print("\nProyectos recientes:")
for p in projects:
    print(f"- {p['title']} (ID: {p['id']})")

5. Ver seguidores

followers = user.get_followers(limit=3)
print("\nSeguidores:")
for f in followers:
    print("-", f["username"])

6. Ver a quién sigue

following = user.get_following(limit=3)
print("\nSiguiendo a:")
for f in following:
    print("-", f["username"])

7. Guardar toda la información en un archivo JSON

user.save_all_info_json("usuario_info.json")

Esto crea un archivo con todos los datos del perfil.
📚 Funciones disponibles
Método	Descripción
get_all_info()	Devuelve toda la información del usuario
get_username()	Devuelve el nombre de usuario
get_bio()	Devuelve la biografía del perfil
get_status()	Devuelve el estado del perfil
get_country()	Devuelve el país registrado
get_joined_date()	Fecha de creación del perfil
get_image()	Imagen de perfil (90x90 px)
get_projects(limit)	Proyectos públicos del usuario
get_followers(limit)	Lista de seguidores
get_following(limit)	Lista de usuarios que el usuario sigue
save_all_info_json()	Guarda todos los datos del perfil en un archivo
🧪 Ejemplo completo

from scratchuser.user import ScratchUser

# Crear objeto del usuario
user = ScratchUser("griffpatch")

# Mostrar información básica
print("Usuario:", user.get_username())
print("Biografía:", user.get_bio())
print("Estado:", user.get_status())
print("País:", user.get_country())
print("Fecha de ingreso:", user.get_joined_date())
print("Imagen de perfil:", user.get_image())

# Proyectos
print("\nProyectos recientes:")
for p in user.get_projects(limit=3):
    print(f"- {p['title']}")

# Seguidores
print("\nSeguidores:")
for f in user.get_followers(limit=3):
    print("-", f["username"])

# A quién sigue
print("\nSiguiendo a:")
for f in user.get_following(limit=3):
    print("-", f["username"])

# Guardar toda la información
user.save_all_info_json("griffpatch_info.json")

👤 Autor

Vicente García Pastor
📧 Correo: vicente.garcia@colegiosocorro.org

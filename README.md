# scratchuser

`scratchuser` es una librería de Python creada por Vicente García Pastor para obtener información pública de perfiles de [Scratch](https://scratch.mit.edu) usando la API oficial `api.scratch.mit.edu`.

Permite ver datos como:
- Biografía del usuario
- Estado
- País
- Imagen de perfil
- Fecha de registro
- Proyectos
- Seguidores
- A quién sigue

---

## 🛠 Instalación

### Desde PyPI (cuando esté publicada)

```bash
pip install scratchuser
```

### Desde código local (modo desarrollo)

```bash
pip install .
```

---

## 🚀 ¿Cómo se usa?

### 1. Importar la clase

```python
from scratchuser.user import ScratchUser
```

### 2. Crear un objeto con el nombre de usuario

```python
user = ScratchUser("griffpatch")  # Reemplaza con cualquier nombre de usuario de Scratch
```

### 3. Obtener información básica

```python
print("Usuario:", user.get_username())
print("Biografía:", user.get_bio())
print("Estado:", user.get_status())
print("País:", user.get_country())
print("Fecha de ingreso:", user.get_joined_date())
print("Imagen de perfil:", user.get_image())
```

### 4. Ver proyectos públicos

```python
projects = user.get_projects(limit=3)
print("\nProyectos recientes:")
for p in projects:
    print(f"- {p['title']} (ID: {p['id']})")
```

### 5. Ver seguidores

```python
followers = user.get_followers(limit=3)
print("\nSeguidores:")
for f in followers:
    print("-", f["username"])
```

### 6. Ver a quién sigue

```python
following = user.get_following(limit=3)
print("\nSiguiendo a:")
for f in following:
    print("-", f["username"])
```

### 7. Guardar información como JSON

```python
user.save_all_info_json("usuario_info.json")
```

---

## 📚 Métodos disponibles

| Método                  | Descripción                                      |
|------------------------|--------------------------------------------------|
| `get_all_info()`       | Toda la información del perfil                   |
| `get_username()`       | Nombre del usuario                               |
| `get_bio()`            | Biografía del usuario                            |
| `get_status()`         | Estado personalizado del perfil                  |
| `get_country()`        | País declarado por el usuario                    |
| `get_joined_date()`    | Fecha en la que el usuario se unió a Scratch     |
| `get_image()`          | URL de la imagen de perfil                       |
| `get_projects(limit)`  | Proyectos públicos del usuario                   |
| `get_followers(limit)` | Seguidores del usuario                           |
| `get_following(limit)` | Usuarios que el usuario sigue                    |
| `save_all_info_json()` | Guarda toda la información en un archivo `.json`|

---

## 🧪 Ejemplo completo

```python
from scratchuser.user import ScratchUser

user = ScratchUser("griffpatch")

print("Usuario:", user.get_username())
print("Biografía:", user.get_bio())
print("Estado:", user.get_status())
print("País:", user.get_country())
print("Fecha de ingreso:", user.get_joined_date())
print("Imagen:", user.get_image())

print("\nProyectos recientes:")
for p in user.get_projects(limit=3):
    print(f"- {p['title']}")

print("\nSeguidores:")
for f in user.get_followers(limit=3):
    print("-", f["username"])

print("\nSiguiendo a:")
for f in user.get_following(limit=3):
    print("-", f["username"])

user.save_all_info_json("griffpatch_info.json")
```

---

## 👨‍💻 Autor

**VIGARPAST_777**  
https://scratch.mit.edu/users/VIGARPAST_777/

---

## 📝 Licencia

Este proyecto está licenciado bajo la **MIT License**.  

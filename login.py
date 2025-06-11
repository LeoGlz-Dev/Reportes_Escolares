usuarios = {
    "admin": "admin123",
    "usuario1": "clave123"
}

def iniciar_sesion():
    print("===== INICIO DE SESIÓN =====")
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")

    if usuario in usuarios:
        if usuarios[usuario] == contrasena:
            print(f"✅ Bienvenido, {usuario}.\nAcceso concedido.")
        else:
            print("❌ Contraseña incorrecta.")
    else:
        print("❌ Usuario no encontrado.")

if __name__ == "__main__":
    iniciar_sesion()

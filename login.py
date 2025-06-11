usuarios = {
    "admin": "admin123",
    "usuario1": "clave123"
}

def iniciar_sesion():
    print("===== INICIO DE SESIÓN =====")
    usuario = input("Nombre de usuario: ").strip()
    contrasena = input("Contraseña: ").strip()

    if usuario in usuarios:
        if usuarios[usuario] == contrasena:
            print(f"✅ Bienvenido, {usuario}.\nAcceso concedido.")
            mostrar_menu(usuario)
        else:
            print("❌ Contraseña incorrecta.")
    else:
        print("❌ Usuario no encontrado.")

def mostrar_menu(usuario):
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Crear nuevo reporte")
        print("2. Ver reportes existentes")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_reporte(usuario)
        elif opcion == "2":
            ver_reportes()
        elif opcion == "3":
            print("👋 Cerrando sesión. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

def crear_reporte(usuario):
    print("\n=== CREAR NUEVO REPORTE ===")
    contenido = input("Escribe el contenido del reporte: ")
    with open("reportes.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Reporte de {usuario}:\n{contenido}\n{'-'*40}\n")
    print("✅ Reporte guardado con éxito.")

def ver_reportes():
    print("\n=== REPORTES GUARDADOS ===")
    try:
        with open("reportes.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido.strip():
                print(contenido)
            else:
                print("No hay reportes todavía.")
    except FileNotFoundError:
        print("No se ha creado ningún reporte aún.")

if __name__ == "__main__":
    iniciar_sesion()


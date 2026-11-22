tareas = []

def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ").strip()
    if not titulo:
        print("Error: El título no puede estar vacío.")
        return
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada correctamente.")

def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    print("\n--- Lista de tareas ---")
    for idx, tarea in enumerate(tareas, start=1):
        estado = "✓" if tarea["completada"] else " "
        print(f"{idx}. [{estado}] {tarea['titulo']}")

def mostrar_menu():
    print("\n=== GESTOR DE TAREAS CLI ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "0":
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Opción no implementada aún.")

if __name__ == "__main__":
    main()

<<<<<<< HEAD
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
=======
import json
import os
import sys

ARCHIVO_TAREAS = "tareas.json"


def cargar_tareas():
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=2, ensure_ascii=False)


def agregar_tarea(titulo):
    tareas = cargar_tareas()
    nueva = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "completada": False,
    }
    tareas.append(nueva)
    guardar_tareas(tareas)
    print(f"Tarea agregada: [{nueva['id']}] {nueva['titulo']}")


def listar_tareas():
    tareas = cargar_tareas()
    if not tareas:
        print("No hay tareas registradas.")
        return
    for t in tareas:
        estado = "✔" if t["completada"] else " "
        print(f"[{estado}] {t['id']}. {t['titulo']}")


def completar_tarea(id_tarea):
    tareas = cargar_tareas()
    for t in tareas:
        if t["id"] == id_tarea:
            t["completada"] = True
            guardar_tareas(tareas)
            print(f"Tarea {id_tarea} marcada como completada.")
            return
    print(f"No se encontró una tarea con el ID {id_tarea}.")


def eliminar_tarea(id_tarea):
    tareas = cargar_tareas()
    nuevas = [t for t in tareas if t["id"] != id_tarea]
    if len(nuevas) == len(tareas):
        print(f"No se encontró una tarea con el ID {id_tarea}.")
        return
    for idx, t in enumerate(nuevas, start=1):
        t["id"] = idx
    guardar_tareas(nuevas)
    print(f"Tarea {id_tarea} eliminada.")


def mostrar_ayuda():
    print("Uso: python app.py <comando> [argumentos]")
    print("Comandos:")
    print("  agregar \"Título de la tarea\"")
    print("  listar")
    print("  completar <id>")
    print("  eliminar <id>")


def main():
    if len(sys.argv) < 2:
        mostrar_ayuda()
        return

    comando = sys.argv[1].lower()

    if comando == "agregar" and len(sys.argv) >= 3:
        agregar_tarea(" ".join(sys.argv[2:]))
    elif comando == "listar":
        listar_tareas()
    elif comando == "completar" and len(sys.argv) >= 3 and sys.argv[2].isdigit():
        completar_tarea(int(sys.argv[2]))
    elif comando == "eliminar" and len(sys.argv) >= 3 and sys.argv[2].isdigit():
        eliminar_tarea(int(sys.argv[2]))
    else:
        mostrar_ayuda()


if __name__ == "__main__":
    main()
>>>>>>> 46b9270242a2a1d5b1b4525025a8a0bcbfad0945

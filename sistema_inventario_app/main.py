from modelos.producto import Producto
from servicios.inventario_service import Inventario


def leer_entero(mensaje: str) -> int:
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("Entrada invalida. Debe ser un numero entero.")


def leer_flotante(mensaje: str) -> float:
    while True:
        valor = input(mensaje)
        try:
            return float(valor)
        except ValueError:
            print("Entrada invalida. Debe ser un numero (puede tener decimales).")


def mostrar_menu():
    print("\n================ SISTEMA DE INVENTARIO =================")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Listar inventario completo")
    print("0. Salir")
    print("=======================================================")


def opcion_agregar(inventario: Inventario):
    print("\n--- Agregar producto ---")
    id_producto = input("ID (unico): ").strip()
    nombre = input("Nombre: ").strip()
    cantidad = leer_entero("Cantidad: ")
    precio = leer_flotante("Precio: ")

    producto = Producto(id_producto, nombre, cantidad, precio)
    if inventario.agregar_producto(producto):
        print("Producto agregado correctamente.")
    else:
        print("Ya existe un producto con ese ID.")


def opcion_eliminar(inventario: Inventario):
    print("\n--- Eliminar producto ---")
    id_producto = input("ID del producto a eliminar: ").strip()
    if inventario.eliminar_producto(id_producto):
        print("Producto eliminado.")
    else:
        print("No se encontro un producto con ese ID.")


def opcion_actualizar(inventario: Inventario):
    print("\n--- Actualizar producto ---")
    id_producto = input("ID del producto a actualizar: ").strip()

    print("Deja vacio si no deseas cambiar ese valor.")
    texto_cant = input("Nueva cantidad: ").strip()
    texto_precio = input("Nuevo precio: ").strip()

    nueva_cantidad = int(texto_cant) if texto_cant != "" else None
    nuevo_precio = float(texto_precio) if texto_precio != "" else None

    if nueva_cantidad is None and nuevo_precio is None:
        print("No se ingreso ningun cambio.")
        return

    try:
        if inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio):
            print("Producto actualizado correctamente.")
        else:
            print("No se encontro un producto con ese ID.")
    except ValueError as e:
        print(f"Error al actualizar: {e}")


def opcion_buscar(inventario: Inventario):
    print("\n--- Buscar producto por nombre ---")
    texto = input("Texto a buscar en el nombre: ").strip()
    resultados = inventario.buscar_por_nombre(texto)

    if not resultados:
        print("No se encontraron productos que coincidan.")
    else:
        print("\nResultados de la busqueda:")
        for p in resultados:
            print(" -", p)


def opcion_listar(inventario: Inventario):
    print("\n--- Inventario completo ---")
    productos = inventario.listar_productos()
    if not productos:
        print("El inventario esta vacio.")
    else:
        for p in productos:
            print(" -", p)


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            opcion_agregar(inventario)
        elif opcion == "2":
            opcion_eliminar(inventario)
        elif opcion == "3":
            opcion_actualizar(inventario)
        elif opcion == "4":
            opcion_buscar(inventario)
        elif opcion == "5":
            opcion_listar(inventario)
        elif opcion == "0":
            print("Saliendo del sistema. Hasta luego.")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
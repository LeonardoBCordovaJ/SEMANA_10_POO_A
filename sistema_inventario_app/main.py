from modelos.producto import Producto
from servicios.inventario_service import Inventario

def main():
    inv = Inventario()
    while True:
        print("\n--- SISTEMA DE INVENTARIO MEJORADO ---")
        print("1. Agregar | 2. Eliminar | 3. Actualizar | 4. Buscar | 5. Listar | 0. Salir")
        op = input("Seleccione: ")

        if op == "1":
            id_p = input("ID: "); nom = input("Nombre: ")
            cant = int(input("Cantidad: ")); prec = float(input("Precio: "))
            if inv.agregar_producto(Producto(id_p, nom, cant, prec)):
                print("Producto guardado en archivo correctamente.")
            else: print("Error: ID duplicado.")

        elif op == "2":
            id_p = input("ID a eliminar: ")
            if inv.eliminar_producto(id_p): print("Producto eliminado del archivo.")
            else: print("No encontrado.")

        elif op == "3":
            id_p = input("ID: "); c = input("Nueva Cant (vacio para omitir): ")
            p = input("Nuevo Precio (vacio para omitir): ")
            cant = int(c) if c else None
            prec = float(p) if p else None
            if inv.actualizar_producto(id_p, cant, prec): print("Archivo actualizado.")
            else: print("No encontrado.")

        elif op == "4":
            nom = input("Nombre a buscar: ")
            res = inv.buscar_producto(nom)
            for r in res: print(r)

        elif op == "5":
            for p in inv.listar_productos(): print(p)

        elif op == "0": break

if __name__ == "__main__":
    main()
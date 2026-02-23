import os
from modelos.producto import Producto

ARCHIVO = "inventario.txt"

class Inventario:
    def __init__(self):
        self._productos = []
        self._cargar_datos()

    def _cargar_datos(self):
        """Carga datos desde el archivo al iniciar, manejando excepciones."""
        try:
            if not os.path.exists(ARCHIVO):
                open(ARCHIVO, 'w').close()
                return
            with open(ARCHIVO, 'r') as f:
                for linea in f:
                    p = Producto.from_csv(linea)
                    if p: self._productos.append(p)
            print("Datos cargados exitosamente desde el archivo.")
        except FileNotFoundError:
            print("Error: El archivo no existe.")
        except PermissionError:
            print("Error: No hay permisos para leer el archivo.")

    def _guardar_datos(self):
        """Guarda los cambios en el archivo, manejando excepciones."""
        try:
            with open(ARCHIVO, 'w') as f:
                for p in self._productos:
                    f.write(p.to_csv() + "\n")
        except PermissionError:
            print("Error: No hay permisos para escribir en el archivo.")

    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self._productos):
            return False
        self._productos.append(producto)
        self._guardar_datos()
        return True

    def eliminar_producto(self, id_p):
        original_count = len(self._productos)
        self._productos = [p for p in self._productos if p.get_id() != id_p]
        if len(self._productos) < original_count:
            self._guardar_datos()
            return True
        return False

    def actualizar_producto(self, id_p, cant=None, precio=None):
        for p in self._productos:
            if p.get_id() == id_p:
                if cant is not None: p.set_cantidad(cant)
                if precio is not None: p.set_precio(precio)
                self._guardar_datos()
                return True
        return False

    def buscar_producto(self, nombre):
        return [p for p in self._productos if nombre.lower() in p.get_nombre().lower()]

    def listar_productos(self):
        return self._productos
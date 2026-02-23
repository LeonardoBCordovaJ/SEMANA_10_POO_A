class Producto:
    """
    Representa un producto del inventario con soporte para archivos CSV.
    """
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self): return self._id
    def get_nombre(self): return self._nombre
    def get_cantidad(self): return self._cantidad
    def get_precio(self): return self._precio

    # Setters con validacion
    def set_cantidad(self, cantidad: int):
        if cantidad < 0: raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = cantidad

    def set_precio(self, precio: float):
        if precio < 0: raise ValueError("El precio no puede ser negativo.")
        self._precio = precio

    def to_csv(self) -> str:
        """Convierte el objeto a una linea de texto para el archivo."""
        return f"{self._id},{self._nombre},{self._cantidad},{self._precio}"

    @staticmethod
    def from_csv(linea: str):
        """Crea un objeto Producto desde una linea del archivo."""
        try:
            p = linea.strip().split(",")
            return Producto(p[0], p[1], int(p[2]), float(p[3]))
        except (ValueError, IndexError):
            return None

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cant: {self._cantidad} | Precio: ${self._precio:.2f}"
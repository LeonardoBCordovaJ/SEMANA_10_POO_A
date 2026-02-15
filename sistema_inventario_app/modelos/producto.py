class Producto:
    """
    Representa un producto del inventario.
    """

    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self) -> str:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_cantidad(self) -> int:
        return self._cantidad

    def get_precio(self) -> float:
        return self._precio

    # Setters
    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def set_cantidad(self, cantidad: int) -> None:
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = cantidad

    def set_precio(self, precio: float) -> None:
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = precio

    def __str__(self) -> str:
        return f"[{self._id}] {self._nombre} - Cantidad: {self._cantidad} - Precio: {self._precio:.2f}"
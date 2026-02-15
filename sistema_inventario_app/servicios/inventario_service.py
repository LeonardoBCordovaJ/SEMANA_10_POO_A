from modelos.producto import Producto


class Inventario:
    """
    Gestiona una coleccion de productos en memoria.
    """

    def __init__(self):
        self._productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> bool:
        """
        Agrega un nuevo producto si el ID no existe.
        Retorna True si lo agrego, False si el ID estaba repetido.
        """
        if self._buscar_por_id(producto.get_id()) is not None:
            return False
        self._productos.append(producto)
        return True

    def eliminar_producto(self, id_producto: str) -> bool:
        """
        Elimina un producto por ID.
        Retorna True si se elimino, False si no se encontro.
        """
        producto = self._buscar_por_id(id_producto)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True

    def actualizar_producto(self, id_producto: str, nueva_cantidad: int | None = None,
                            nuevo_precio: float | None = None) -> bool:
        """
        Actualiza cantidad y/o precio de un producto por ID.
        """
        producto = self._buscar_por_id(id_producto)
        if producto is None:
            return False

        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad)

        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)

        return True

    def buscar_por_nombre(self, texto: str) -> list[Producto]:
        """
        Busca productos cuyo nombre contenga el texto (coincidencia parcial, sin mayusculas).
        """
        texto = texto.lower()
        return [p for p in self._productos if texto in p.get_nombre().lower()]

    def listar_productos(self) -> list[Producto]:
        """
        Retorna la lista completa de productos.
        """
        return list(self._productos)

    # Metodo privado de ayuda
    def _buscar_por_id(self, id_producto: str) -> Producto | None:
        for p in self._productos:
            if p.get_id() == id_producto:
                return p
        return None
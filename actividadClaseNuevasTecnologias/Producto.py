dictProductos = {}

class Producto:
    def __int__(self,nombre,descripcion,costo,cantidad,precio_de_venta,margen_venta):
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = precio_de_venta
        self.margen_venta = margen_venta

    def registrarProducto(self):
        self.nombre = input("Ingrese el nombre del producto: ")
        self.descripcion = input("Ingrese una descripcion para el producto")
        self.costo = float(input("Ingrese el costo del producto"))
        self.cantidad = float(input("Ingrese cuantos productos existen:"))
        self.margen_venta = 100/(float(input("Ingrese cuanto planea ganar respecto al costo")))
        self.precio_de_venta = self.costo / (1 - self.margen_venta)

    def __str__(self):
        return f'nombre: {self.nombre}' \
               f'descripcion: {self.descripcion}' \
               f'costo: {self.costo}' \
               f'cantidad: {self.cantidad}' \
               f'margen de venta: {self.margen_venta}' \
               f'precio de venta: {self.precio_de_venta}'






def flujoDeTrabajo():
    err = True
    while err:
        producto = Producto()
        producto.registrarProducto()
        dictProductos[input("Ingrese el ID: ")] = str(producto)
        err2 = True
        while err2:
            option = int(input("Desea ingresar un nuevo producto? 1.Si 2.No"))
            if option == 1:
                print("Vas a ingresar un nuevo producto")
                err2 = False
            elif option == 2:
                print("Hasta pronto")
                err = False
                err2 = False
            else:
                print("Ingrese una opcion valida")

def mostrarProductos():
    print(dictProductos)

flujoDeTrabajo()
mostrarProductos()
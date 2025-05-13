# Documentacion del programa
## Inventario
Este programa permite llevar un inventario mas organizado y facil de manejar, dando opciones para un buen manejo de los productos.

# Como funciona el programa
## Los productos se almacenan en un diccionario:
Este diccionario almacena productos teniendo en cuenta el nombre del producto como llave, los valores como el precio y la cantidad dentro de una tupla.
## Ejemplo:
inventory = {
        "Arroz":(5000, 68)
}
- El nombre del producto ("Arroz") es la llave.
- La tupla sera el valor ("5000, 68") donde 5000 sera el precio y 68 la cantidad existente.

Para acceder al inventario se da un menu de opciones:
- 1.Añadir productos.
- 2.Consultar productos.
- 3.Actualizar productos (precio).
- 4.Eliminar productos.
- 5.Calcular el valor total del inventario.
- 6.Cambiar la cantidad de los productos.
- 7.Salir del inventario.

## Las opciones se manejan con un match-case, dependiendo de la eleccion del usuario permite ejecutar dicha tarea, las cuales se pueden desarrollar en funciones que fueron creadas para un propocito en especifico.

# Opcion 1:
La funcion "add_product()" fue creada para realizar esta tarea en especifico, la funcion pide:
- Nombre del producto.
- Precio del producto.
- Cantidad del producto.

Añade estos datos a nuestro diccionario, solo se detiene hasta que el usuario haya ingresado 5 productos con todos los datos necesarios; de ahi sale de la funcion y vuelve al menu.


# Opcion 2:
La funcion "consult_product()" permite consultar un producto en especifico por medio de su nombre, mostrando su estado como:
- Nombre
- Precio
- Cantidad

## Ejemplo:
Ingrese el nombre del producto: Arroz


Nombre | Precio | Cantidad

Arroz  | 5000   | 68



## Opcion 3:
Esta opcion permite cambiar el precio del producto de una manera eficiente dentro de la funcion "update_product()":

## Ejemplo:
Ingrese el nombre del producto: Arroz

Ingrese el nuevo precio del producto: 3000

El precio de Arroz actualizado.


Para ser mas claro con el ejemplo, el inventario quedaria asi:

Nombre | Precio | Cantidad

Arroz  | 3000   | 68



## Opcion 4:
La funcion "eliminate_product()" permite eliminar un producto si su cantidad es cero, de lo contrario notifica que hay productos:

## Ejemplo:
Ingrese el nombre del producto: Arroz


El producto arroz no se puede eliminar aun hay productos.



## Opcion 5:
Esta opcion deja ver en pantalla el valor total del inventario:
## Ejemplo:


El valor total del inventario es: 23000.00


## Opcion 6:
Permite modificar la cantidad del producto:

## Ejemplo:

ingrese el nombre del producto: Arroz


ingrese la cantidad: 50


Nombre | Precio | Cantidad

Arroz  | 5000   | 50


## Opcion 7:
Sale del programa:

## Ejemplo:

Has salido del programa.






















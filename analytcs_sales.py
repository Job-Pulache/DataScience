"""
Ejercicio: Análisis de ventas mensuales con NumPy

Una tienda registra las ventas (en miles de pesos) de tres productos entre
enero y junio. Completa estas tareas:
1. Calcula las ventas totales de cada mes y de cada producto.
2. Encuentra el mes con mayores ventas y el producto más vendido.
3. Calcula el cambio porcentual de ventas de un mes al siguiente.
4. Compara las ventas del primer trimestre (ene-mar) con el segundo (abr-jun).
5. Calcula qué porcentaje del total representa cada producto.

Debajo está una solución ejecutable. Modifica los datos para practicar.
"""

import numpy as np


def main() -> None:
    meses = np.array(["Ene", "Feb", "Mar", "Abr", "May", "Jun"])
    productos = np.array(["Laptop", "Tablet", "Accesorios"])
    # Filas = productos; columnas = meses. Valores en miles de pesos.
    ventas = np.array(
        [
            [120, 135, 128, 150, 170, 165],
            [90, 95, 105, 110, 108, 120],
            [60, 72, 70, 85, 90, 100],
        ]
    )

    ventas_por_mes = ventas.sum(axis=0)
    ventas_por_producto = ventas.sum(axis=1)
    crecimiento_mensual = (ventas_por_mes[1:] - ventas_por_mes[:-1]) / ventas_por_mes[:-1] * 100
    ventas_primer_trimestre = ventas[:, :3].sum()
    ventas_segundo_trimestre = ventas[:, 3:].sum()
    cambio_trimestral = (
        (ventas_segundo_trimestre - ventas_primer_trimestre)
        / ventas_primer_trimestre
        * 100
    )
    participacion_producto = ventas_por_producto / ventas_por_producto.sum() * 100

    mes_maximo = meses[np.argmax(ventas_por_mes)]
    producto_maximo = productos[np.argmax(ventas_por_producto)]

    print("VENTAS TOTALES POR MES (miles de pesos)")
    for mes, total in zip(meses, ventas_por_mes):
        print(f"  {mes}: ${total:,.0f}")

    print("\nVENTAS TOTALES POR PRODUCTO (miles de pesos)")
    for producto, total, participacion in zip(
        productos, ventas_por_producto, participacion_producto
    ):
        print(f"  {producto}: ${total:,.0f} ({participacion:.1f}% del total)")

    print("\nCAMBIO PORCENTUAL MENSUAL")
    for mes_anterior, mes_actual, cambio in zip(
        meses[:-1], meses[1:], crecimiento_mensual
    ):
        print(f"  {mes_anterior} -> {mes_actual}: {cambio:+.1f}%")

    print("\nCOMPARACIÓN DE TRIMESTRES")
    print(f"  Ene-Mar: ${ventas_primer_trimestre:,.0f}")
    print(f"  Abr-Jun: ${ventas_segundo_trimestre:,.0f} ({cambio_trimestral:+.1f}%)")

    print("\nINSIGHTS")
    print(f"  El mejor mes fue {mes_maximo}, con ${ventas_por_mes.max():,.0f}.")
    print(f"  El producto con más ventas fue {producto_maximo}.")
    print(f"  Las ventas del segundo trimestre cambiaron {cambio_trimestral:+.1f}% frente al primero.")


if __name__ == "__main__":
    main()
# Función para agregar una compra a la lista
def agregar_compra(compras, total_gastado):
    compra = float(input("Ingrese el monto de la compra: "))
    compras.append(compra)
    total_gastado[0] += compra  # Actualiza el total gastado
    print("Compra agregada correctamente.")

# Función para mostrar las compras registradas
def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Compras registradas:")
        for i, compra in enumerate(compras, start=1):
            print(f"Compra {i}: ${compra:.2f}")

# Función para mostrar el total gastado
def mostrar_total(total_gastado):
    if total_gastado[0] == 0:
        print("Aún no has gastado nada.")
    else:
        print(f"Total gastado: ${total_gastado[0]:.2f}")

# Función principal
def main():
    compras = []
    total_gastado = [0]  # Utilizamos una lista para mantener el total gastado

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_compra(compras, total_gastado)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(total_gastado)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
votos = {}
votantes_registrados = set()

def registrar_voto(nombre, opcion):
    """Registra un voto validando que la persona no vote dos veces."""
    if nombre in votantes_registrados:
        print(f"❌ {nombre} ya votó. No puede votar dos veces.")
        return False
    votantes_registrados.add(nombre)
    votos[opcion] = votos.get(opcion, 0) + 1
    print(f"✅ Voto de {nombre} registrado por: {opcion}")
    return True
def ver_resultados():
    """Muestra los resultados con porcentajes."""
    total = sum(votos.values())
    if total == 0:
        print("📊 No hay votos registrados aún.")
        return
    print("\n📊 RESULTADOS:")
    for opcion, conteo in votos.items():
        porcentaje = (conteo / total) * 100
        print(f"  {opcion}: {conteo} votos ({porcentaje:.2f}%)")
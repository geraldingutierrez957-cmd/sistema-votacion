import json
from datetime import datetime

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


def reiniciar_votacion():
    """Reinicia votos y guarda historial en archivo."""
    global votos
    if votos:
        historial = {
            "fecha": datetime.now().isoformat(),
            "resultados": votos.copy()
        }
        with open("historial.json", "a") as f:
            f.write(json.dumps(historial) + "\n")
        print("💾 Historial guardado en historial.json")
    votos.clear()
    votantes_registrados.clear()
    print("🔄 Votacion reiniciada.")


# ---------- MEJORA ADICIONAL ----------
def mostrar_ganador():
    """Muestra quién va ganando la votación."""
    if not votos:
        print("🏆 No hay votos registrados aún.")
        return
    ganador = max(votos, key=votos.get)
    print(f"🏆 El ganador es: {ganador} con {votos[ganador]} voto(s)")


# ---------- MENÚ PRINCIPAL ----------
def menu():
    while True:
        print("\n===== SISTEMA DE VOTACIÓN =====")
        print("1. Registrar voto")
        print("2. Ver resultados")
        print("3. Reiniciar votación")
        print("4. Ver ganador")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del votante: ").strip()
            candidato = input("¿Por quién vota?: ").strip()
            registrar_voto(nombre, candidato)
        elif opcion == "2":
            ver_resultados()
        elif opcion == "3":
            reiniciar_votacion()
        elif opcion == "4":
            mostrar_ganador()
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")


# ---------- ARRANQUE ----------
if __name__ == "__main__":
    menu()
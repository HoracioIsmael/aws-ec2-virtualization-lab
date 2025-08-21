import pyautogui
import time
import os
from pyautogui import ImageNotFoundException

# Configuración
IMAGES_PATH = os.path.join(os.getcwd(), "img")
UNIRSE_IMG = os.path.join(IMAGES_PATH, "unirse.png")
MARCHA2_IMG = os.path.join(IMAGES_PATH, "marcha2.png")
BOTON_MARCHAR_IMG = os.path.join(IMAGES_PATH, "boton_marchar.png")

NUM_MAX_RALLYS = 5  # Número máximo de rallys a los que unirse
INTERVALO_SEGUNDOS = 30  # Espera 30 segundos si no se encuentran rallys

def buscar_y_click(imagen, descripcion, timeout=10):
    print(f"🔄 Buscando {descripcion}...")
    inicio = time.time()
    while time.time() - inicio < timeout:
        try:
            ubicacion = pyautogui.locateCenterOnScreen(imagen, confidence=0.6)  # Ajusta el nivel de confianza
        except ImageNotFoundException:
            return False
        if ubicacion:
            pyautogui.moveTo(ubicacion, duration=0.2)
            pyautogui.click()
            print(f"✔ Click en '{descripcion}'")
            return True
        time.sleep(0.5)
    print(f"❌ No se encontró {descripcion}")
    return False

def hacer_scroll_ventana():
    print("🔄 Haciendo scroll...")
    pyautogui.moveTo(250, 700)
    pyautogui.scroll(-300)  # Scroll hacia abajo

def unir_a_rallys():
    uniones_realizadas = 0

    print("🔄 Iniciando búsqueda de rallys...")
    while uniones_realizadas < NUM_MAX_RALLYS:
        try:
            ubicaciones = list(pyautogui.locateAllOnScreen(UNIRSE_IMG, confidence=0.6))  # Ajusta el nivel de confianza
            if not ubicaciones:
                print("🔁 No se encontraron más botones visibles. Haciendo scroll...")
                hacer_scroll_ventana()
                time.sleep(1)
                continue

            for ubicacion in ubicaciones:
                if uniones_realizadas >= NUM_MAX_RALLYS:
                    break

                pyautogui.moveTo(ubicacion.left + ubicacion.width / 2, ubicacion.top + ubicacion.height / 2, duration=0.2)
                pyautogui.click()
                print(f"✔ Click en 'Unirse' [{uniones_realizadas + 1}]")
                time.sleep(1)

                if not buscar_y_click(MARCHA2_IMG, "Marcha II", timeout=5):
                    print("⚠ No se encontró 'Marcha II'. Quizás el juego reinició. Saltando.")
                    break

                time.sleep(0.5)
                if buscar_y_click(BOTON_MARCHAR_IMG, "botón Marchar", timeout=5):
                    print(f"✅ Unión al rally #{uniones_realizadas + 1} completada.")
                    uniones_realizadas += 1
                else:
                    print("⚠ No se encontró botón 'Marchar'. Saltando esta unión.")

                time.sleep(2)

            hacer_scroll_ventana()

        except ImageNotFoundException:
            print("❌ No se encontró la imagen. Intentando de nuevo...")
            time.sleep(1)
            continue

    print(f"🎯 Total de uniones realizadas: {uniones_realizadas}")
    print(f"⏳ No se encontraron más rallys. Esperando {INTERVALO_SEGUNDOS} segundos antes de buscar nuevamente...")
    time.sleep(INTERVALO_SEGUNDOS)

# Loop infinito
print("🤖 BOT INICIADO (modo cíclico)")
while True:
    unir_a_rallys()

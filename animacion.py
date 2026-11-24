import threading
import time
from colorama import Back, Fore, Style, init

# Inicializa colorama para que funcione bien en VS Code
init(autoreset=True)

# Bandera para controlar cuándo detener el parpadeo
parpadeando = True


def cartel_intermitente(texto):
  while parpadeando:
    # Encendido: Fondo rojo con letras blancas
    print(f"\r{Back.RED}{Fore.WHITE} {texto} ", end="", flush=True)
    time.sleep(0.5)

    # Apagado: Sin fondo (o podés poner Back.BLACK)
    print(f"\r{Style.RESET_ALL} {texto} ", end="", flush=True)
    time.sleep(0.5)


# 1. Arrancamos la animación en segundo plano
hilo = threading.Thread(target=cartel_intermitente, args=("¡ATENCIÓN!",))
hilo.start()

# 2. Tu programa sigue funcionando normal (acá espera 5 segundos como ejemplo)
time.sleep(5)

# 3. Frenamos la animación y limpiamos la línea
parpadeando = False
hilo.join()
print("\rListo, proceso terminado.      ")

print(
    Style.BRIGHT
    + Fore.WHITE
    + Back.BLUE
    + "Important Message"
    + Style.RESET_ALL
)
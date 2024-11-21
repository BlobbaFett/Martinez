from tkinter import *
import random

# Inicialización de las dimensiones del juego
WIDTH = 500
HEIGHT = 500
SPEED = 100
SPACE_SIZE = 20
BODY_SIZE = 2
SNAKE_HEAD_COLOR = "#FFFF00"  # Color amarillo para la cabeza feliz
SNAKE_BODY_COLOR = "#00FF00"  # Color verde para el cuerpo
FOOD = "#FF0000"  # Color rojo para la comida
BACKGROUND = "#000000"  # Fondo negro

# Clase para diseñar la serpiente
class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []

        # Crear cuerpo de la serpiente, inicialmente con dos segmentos
        for i in range(0, BODY_SIZE):
            self.coordinates.append([0, 0])

        # Dibujar el cuerpo
        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=SNAKE_BODY_COLOR, tag="snake")
            self.squares.append(square)

        # Crear la cabeza feliz como la cabeza de la serpiente (el primer segmento)
        self.head = self.create_happy_face(self.coordinates[0][0], self.coordinates[0][1])

    def create_happy_face(self, x, y):
        """Dibuja una cabeza feliz como la cabeza de la serpiente"""
        # Cabeza (círculo amarillo)
        head = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_HEAD_COLOR, tag="snake_head")

        # Ojos (círculos negros)
        eye_size = 5
        left_eye = canvas.create_oval(x + 5, y + 5, x + 5 + eye_size, y + 5 + eye_size, fill="black", tag="snake_head")
        right_eye = canvas.create_oval(x + SPACE_SIZE - 5 - eye_size, y + 5, x + SPACE_SIZE - 5, y + 5 + eye_size, fill="black", tag="snake_head")

        # Sonrisa (arco)
        smile = canvas.create_arc(x + 5, y + SPACE_SIZE - 10, x + SPACE_SIZE - 5, y + SPACE_SIZE, start=0, extent=-180, style=ARC, width=2, outline="black", tag="snake_head")

        return [head, left_eye, right_eye, smile]

# Clase para diseñar la comida
class Food:
    def __init__(self):
        x = random.randint(0, (WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD, tag="food")

# Función para comprobar el siguiente movimiento de la serpiente
def next_turn(snake, food):
    global direction

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    # Eliminar la cabeza anterior
    canvas.delete("snake_head")

    # Dibujar la nueva cabeza (carita feliz) en la nueva posición
    snake.head = snake.create_happy_face(x, y)

    # Añadir una nueva parte del cuerpo
    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_BODY_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Puntos:{}".format(score))

        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

# Función para controlar la dirección de la serpiente
def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

# Función para comprobar las colisiones de la serpiente
def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

# Función para controlar el final del juego
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")

# Configuración del juego
window = Tk()
window.title("Juego de Serpiente con Carita Feliz")

score = 0
direction = 'down'

# Mostrar los puntos obtenidos en el juego
label = Label(window, text="Puntos:{}".format(score),
              font=('consolas', 20))
label.pack()

canvas = Canvas(window, bg=BACKGROUND, height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Enlazar las teclas para controlar la dirección de la serpiente
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

# Iniciar el bucle del juego
next_turn(snake, food)

# Iniciar el bucle principal
window.mainloop()

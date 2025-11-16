import tkinter as tk
from math import dist

# Configuracion del tablero de juego
class GameBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size=32, color1="white", color2="black"):
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.fichas = []

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        self.canvas.bind("<Configure>", self.refresh)

    def refresh(self, event):
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2

    def poner_pieza(self, col, row, text):
        x = col * self.size + self.size / 2
        y = row * self.size + self.size / 2

        label = tk.Label(self.canvas, text=text)
        id = self.canvas.create_window(x, y, window=label)
        self.fichas.append((id, label))
        return label
    
    def clear(self):
        for win_id, label in self.fichas:
            self.canvas.delete(win_id)
            label.destroy()
        self.fichas.clear()

def check_winner():
    for i in range(len(cops)):
        if robber[0] == cops[i][1] and robber[1] == cops[i][2]:
            labelWin.config(text="Los policias han ganado", fg="#ff0000")
            print("Los policias ganan")

    if robber[1] == 7:
        labelWin.config(text="El ladron ha ganado", fg="#57f542")
        print(f"El ladron gana")

def move_robber(directionX, directionY):
    movX = robber[0] + directionX
    movY = robber[1] + directionY

    print(f"movimiento: {(movX, movY)}")

    if movX < 0 or movY > 8 or movX > 8 or movY < 0:
        print("Movimiento no valido")
    else:    
        robber[0] = movX
        robber[1] = movY

        board.clear()

        board.poner_pieza(robber[0], robber[1], "0")

        for i in range(len(cops)):
            board.poner_pieza(cops[i][1], cops[i][2], "X")
        check_winner()
        move_cop()

    print(robber)

def move_cop():
    distance = 100
    closest_id = 10
    
    calc_distance()
    
    for i in range(len(cops)):
            if cops[i][3] < distance:
                distance = cops[i][3]
                closest_id = i

    print(f"Policia más cercano: {closest_id+1}")

    posRob = (robber[0], robber[1])

    moveL = dist((cops[closest_id][1]-1,cops[closest_id][2]-1), posRob)
    moveR = dist((cops[closest_id][1]+1,cops[closest_id][2]-1), posRob)

    if moveR < moveL:
        cops[closest_id][1] = cops[closest_id][1]+1
        cops[closest_id][2] = cops[closest_id][2]-1
    else:
        cops[closest_id][1] = cops[closest_id][1]-1
        cops[closest_id][2] = cops[closest_id][2]-1

    board.clear()

    board.poner_pieza(robber[0], robber[1], "0")

    for i in range(len(cops)):
        board.poner_pieza(cops[i][1], cops[i][2], "X")
    
    check_winner()

def start_game():
    pos = posIni.get()
    pos = int(pos)

    if pos or pos == 0:
        robber[0] = pos
        print(robber[0])
        board.poner_pieza(robber[0], 0, "0")

        for i in range(len(cops)):
            board.poner_pieza(cops[i][1], cops[i][2], "X")
        calc_distance()
    
    else:
        print("No input")

def reset_game():
    robber[0] = 0
    robber[1] = 0

    for i in range(len(cops)):
        cops[i][1] = (i*2)+1
        
        cops[i][2] = 7
        cops[i][3] = 10
    
    board.clear()
    
    labelWin.config(text="")

    print("Juego reiniciado")

def calc_distance():
    print("Posiciones")

    for i in range(len(cops)):
            posCop = (cops[i][1],cops[i][2])
            posRob = (robber[0], robber[1])

            cops[i][3] = dist(posCop, posRob)

            print(f"Policia {i+1}: {cops[i][3]}")
            
if __name__ == "__main__":
    # Variables

    # Posicion del ladron (Columna, Fila)
    robber = [0, 0]

    # Datos de cada policia
    # Id, Columna, Fila, Distancia
    cops = [
        [0, 1, 7, 10],
        [1, 3, 7, 10],
        [2, 5, 7, 10],
        [3, 7, 7, 10]
    ]

    root = tk.Tk()
    root.title("Policias y Ladrones")

    Frame = tk.Frame(root)
    Frame.grid(row=0, column=0)

    # Tablero
    board = GameBoard(Frame)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    board.grid(row=0, column=1)

    labelWin = tk.Label(Frame, text="")
    labelWin.grid(row=0, column=2)

    # Seccion de configuracion
    labelPos = tk.Label(Frame, text="Casilla inical del ladron (0, 2, 4, 6)")
    labelPos.grid(row=1, column=0)

    posIni = tk.Entry(Frame)
    posIni.grid(row=2, column=0)

    btnReiniciar = tk.Button(Frame, text="Reiniciar Juego", command=reset_game)
    btnComenzar = tk.Button(Frame, text="Comenzar Juego", command=start_game)

    btnComenzar.grid(row=3, column=0)
    btnReiniciar.grid(row=0, column=0)
        
    #Seccion de movimiento
    btnMoverIzqArr = tk.Button(Frame, text="Avanzar a la diagonal izquierda", command= lambda: move_robber(-1, 1))
    btnMoverDerArr = tk.Button(Frame, text="Avanzar a la diagonal derecha", command= lambda: move_robber(1, 1))
    btnMoverIzqAb = tk.Button(Frame, text="Retroceder a la diagonal izquierda", command= lambda: move_robber(-1, -1))
    btnMoverDerAb = tk.Button(Frame, text="Retroceder a la diagonal derecha", command= lambda: move_robber(1, -1))

    btnMoverIzqArr.grid(row=1, column=1)
    btnMoverDerArr.grid(row=2, column=1)
    btnMoverIzqAb.grid(row=3, column=1)
    btnMoverDerAb.grid(row=4, column=1)

    root.mainloop()
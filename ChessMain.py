"""
This is our main driver file. It is responsible for handing user input and displaying the current GameState object
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 #8x8 board size
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 30
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called once in the main
'''

def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

"""
The main driver for the code
"""

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

"""
Responsible for graphics within a current game state
"""

def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on the board
    #add in pieces highlighting or move suggestions later
    drawPieces(screen, gs.board)

"""
draw the squares on the board. Top left is always White/Light
"""

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))



"""
Draw the pieces on the board using the current GameState.board
"""

def drawPieces(screen, board):
    pass


if __name__ == "__main__":
    main()
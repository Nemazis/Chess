"""
This is our main driver file. It is responsible for handing user input and displaying the current GameState object
"""

import pygame as p
import ChessEngine as ChessEngine

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
        IMAGES[piece] = p.transform.scale(p.image.load("C:/Visual Studio Code/Chess Project/Chess/src/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

"""
The main driver for the code
"""

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False
    loadImages()
    running = True
    sqSelected = () #Nothing selected to start. Keeps track of the last click. Tuple, so keeps track of (Row and Column)
    playerClicks = [] #Keeps track of player clicks (two tuples)
    
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                #mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y) location of mouse
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = () #Un-selects piece
                    playerClicks = [] #Clears selection
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                        sqSelected = ()
                        playerClicks = []
                    else:
                        playerClicks = [sqSelected]
                #key handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
                    
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
                    
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
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #If NOT an empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
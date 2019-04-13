from world.cell import Cell, CellType

"""Custom Pick-Up Drop-off World"""""


class PDWorld:
    def __init__(self):
        self.cells = []
        for x in range (1,6):
            for y in range (1,6):
                if x == y and (x % 2 == 1):
                    self.cells.append(Cell(CellType.PICKUP, (x,y)))
                elif x == 2 and y == 5:
                    self.cells.append(Cell(CellType.DROPOFF, (x,y)))
                elif x == 5 and y == 1:
                    self.cells.append(Cell(CellType.DROPOFF, (x,y)))
                elif x == 5 and y == 3:
                    self.cells.append(Cell(CellType.DROPOFF, (x,y)))
                else:
                    self.cells.append(Cell(CellType.REGULAR, (x,y)))

        self.inTerminalState = False
        self.startCell = (1, 5)

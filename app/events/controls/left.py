class MoveLeftEvent:

    def handle(self, grid, _next):
        item = grid.current()

        if item is not None:
            x, y, w, h = item.pos()

            if x == 0:
                return next(_next)

            move = True
            for j in range(h):
                for i in range(w):
                    if item.is_fill(i, j) and grid.cells[y+j][x+i-1] is not None:
                        move = False

        if move:
            item.inc_grid_x(-1)

        return next(_next)

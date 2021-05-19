class MoveLeftEvent:

    def handle(self, grid, _next):
        item = grid.current()

        if item is not None:
            x = item.get_grid_x()
            y = item.get_grid_y()
            h = item.get_grid_height()

            move = False
            if x > 0:
                move = True
                for i in range(h):
                    if grid.cells[h][-x] == 0:
                        move = False

        if move:
            item.inc_grid_x(-1)

        return next(_next)

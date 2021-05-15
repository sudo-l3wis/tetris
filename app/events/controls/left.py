class MoveLeftEvent:

    def handle(self, grid, _next):
        item = grid.current()

        if item is not None:
            if item.get_grid_x() > 0:
                item.inc_grid_x(-1)

        return next(_next)

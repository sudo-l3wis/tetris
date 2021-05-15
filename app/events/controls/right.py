class MoveRightEvent:

    def handle(self, grid, _next):
        cols = config('display.grid.cols')

        item = grid.current()
        gx = item.get_grid_x()
        gw = item.get_grid_width()

        if item is not None:
            if gx + gw < cols:
                item.inc_grid_x(1)

        return next(_next)

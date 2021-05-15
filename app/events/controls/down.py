class MoveDownEvent:

    def handle(self, grid, _next):
        while grid.tick():
            continue

        return next(_next)

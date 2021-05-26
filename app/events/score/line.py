from app.framework.decorator import inject


class LineComplete:

    @inject('singleton.score')
    def handle(self, lines, _next, score):
        amt = config('score.multiplier') * config('score.line')
        score.inc_score(lines * amt)
        return next(_next)

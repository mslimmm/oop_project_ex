class player: #컴퓨터와 플레이어
    class egg: #가지고 있는 알의 특성
        def __init__(self):
            self.x = 0
            self.y = 0
            self.carrying_egg = []

        def move(self, movecnt):

            if self.x == 1 and self.y == 0:
                self.x = -1
            elif self.x == 2 and self.y == 0:
                self.x = -2
            elif self.x == -1 and self.y == 3:
                self.x = -2

            for i in range(movecnt):
                self.y += 1
                if 0 <= self.x <= 3 and self.y == 5:
                    self.y = 0
                    self.x += 1
                elif self.x == -1 and self.y == 6:
                    self.y = 0
                    self.x = 3
                elif self.x == -2 and self.y == 6:
                    self.y = 0
                    self.x = 4

                if self.x == 4 and self.y > 0:
                    break

            for i in self.carrying_egg:
                i.x = self.x
                i.y = self.y


    def __init__(self):
        self.egglist = [self.egg(), self.egg(), self.egg(), self.egg()]
        self.onmap = []
        self.onmapno = 0
        self.finegg = []
        self.fineggno = 0

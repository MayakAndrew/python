class Road:
    _length = 0
    _width = 0

    def area(pl, _length, _width):
        sq = _length * _width * 25 * 5
        return sq

pl = Road()
print('Масса полотна дороги - ', pl.area(10, 20))
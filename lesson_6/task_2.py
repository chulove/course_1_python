class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_vol(self, spec_cons=2, thickness=5):
        return f'''Парамеры дорожного полотна:
Длина: {self._length} м
Ширина: {self._length} м
Толщина: {thickness} см
Удельный расход асфальта {spec_cons} т/м3
Масса асфальта, необходимого для покрытия дорожного полотна {self._length * self._width * thickness * spec_cons / 100} т'''


road_1 = Road(5000, 20)
print(road_1.calc_asphalt_vol(spec_cons=2.5, thickness=5))

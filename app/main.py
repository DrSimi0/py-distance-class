from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        distance = self.km
        return f"Distance: {distance} kilometers."

    def __repr__(self) -> str:
        distance = self.km
        return f"Distance(km={distance})"

    def __add__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            distance3 = Distance(self.km + other.km)
            return distance3
        else:
            distance3 = Distance(self.km + other)
            return distance3

    def __iadd__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float, Distance)):
            distance2 = Distance(self.km * other)
            return distance2
        else:
            distance2 = Distance(self.km * other.km)
            return distance2

    def __truediv__(self, other: Union[int, float, "Distance"]) -> "Distance":
        if isinstance(other, (int, float, Distance)):
            distance2 = Distance(round(self.km / other, 2))
            return distance2
        else:
            distance2 = Distance(round(self.km / other.km, 2))
            return distance2

    def __lt__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: Union[int, float, "Distance"]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other

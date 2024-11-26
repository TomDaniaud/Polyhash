"""Module.
"""
from __future__ import annotations
from .wind import Wind

class Cell:
    def __init__(self, x: int, y: int, winds: tuple[Wind]) -> None:
        """Entity that describe the wind and the target cell in range of a position"""
        self.pos: tuple[int,int] = (x,y)
        self.x: int = x
        self.y: int = y
        self._winds: tuple[Wind] = winds
        self.targets: list[Cell] = []

    def addTarget(self, target: Cell) -> None:
        """Add target cell into the cell's targets list"""
        self.targets.append(target)

    def getWinds(self, alt: int) -> Wind:
        """Get wind at the altitude

        args:
            alt: choosen altitude (0<alt<maxAlt)
        """
        assert len(self._winds)+1 > alt > 0
        return self._winds[alt-1]
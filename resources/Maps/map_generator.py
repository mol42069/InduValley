import pygame as pg
from scripts import save

class MapGen:
    def __init__(self):
        self.map = [["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],
                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],
                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],
                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    [
                        "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],
                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],
                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],
                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],
                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],
                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],
                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    [
                        "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                        "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                        "Grass", "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],
                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],
                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],
                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],
                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ["Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Dirt",
                     "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt", "Grass"],

                    ["Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Dirt", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass", "Grass",
                     "Grass", "Grass", "Dirt", "Stone", "Stone", "Stone", "Grass", "Dirt"],

                    ]

        save.save(self.map, "save1", "Farm")

        return
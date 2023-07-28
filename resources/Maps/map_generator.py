from scripts import save

class MapGen:
    def __init__(self):

        self.map = [["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    [
                        "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    [
                        "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                        "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                        "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],
                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],
                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ["Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Dirt:Ta",
                     "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta", "Grass:Ta"],

                    ["Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Dirt:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta", "Grass:Ta",
                     "Grass:Ta", "Grass:Ta", "Dirt:Ta", "Stone:nT", "Stone:nT", "Stone:nT", "Grass:Ta", "Dirt:Ta"],

                    ]

        save.save(self.map, "save1", "Farm")

        return
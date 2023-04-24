import os
import csv


def load_from_path(file_path: str) -> dict[tuple[int, int], str]:
    tiles = {}
    with open(file_path, newline='') as file:
        reader = csv.reader(file, delimiter=' ')
        tile_mappings = {}
        while (len(i := next(reader)) > 1):
            num, path = int(i[0]), i[1]
            absolute = os.path.join(os.path.dirname(file_path), path)
            tile_mappings[num] = absolute

        for row in reader:
            x, y, num = map(int, row)
            tiles[(x, y)] = tile_mappings[num]

        return tiles

def save_to_path(tiles: dict[tuple[int, int], str], file_path: str):
    dir = os.path.dirname(file_path)
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        tile_mappings = {}
        for i, tile_id in enumerate(set(tiles.values())):
            path = os.path.relpath(tile_id, dir)
            writer.writerow([i, path])
            tile_mappings[tile_id] = i

        writer.writerow([])

        for (x, y), tile_id in tiles.items():
            writer.writerow([int(x), int(y), tile_mappings[tile_id]])

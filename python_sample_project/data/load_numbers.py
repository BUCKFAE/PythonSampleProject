
import os

from python_sample_project.utils import get_project_root


def load_numbers() -> list[tuple[int, int, int]]:
    """Loads the numbers present in the file"""

    path = os.path.join(get_project_root(), 'data', 'numbers.txt')
    assert os.path.isfile(path), f'File not found: {path}'

    res: list[tuple[int, int, int]] = []

    with open(path, 'r') as f:

        for line in f.read().splitlines():
            splitted = line.split(' ')
            assert len(splitted) == 3, f'Expected exactly 3 numbers in line: {line}'
            assert all([c.isdigit() for c in splitted]), f'Line contained a non-digit: {line}'
            a, b, c = [int(num) for num in line.split(' ')]
            res += [(a, b, c)]

        return res

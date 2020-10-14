#!/usr/bin/env python
# Usage: python blosum.py blosum62.txt
#        Then, enter input in "row col" format -- e..g, "s f".
import sys

class InvalidPairException(Exception):
  pass

class Matrix:
  def __init__(self, matrix_filename):
    self._load_matrix(matrix_filename)

  def _load_matrix(self, matrix_filename):
    with open(matrix_filename) as matrix_file:
      matrix = matrix_file.read()
    lines = matrix.strip().split('\n')

    header = lines.pop(0)
    columns = header.split()
    matrix = {}

    for row in lines:
      entries = row.split()
      row_name = entries.pop(0)
      matrix[row_name] = {}

      if len(entries) != len(columns):
        raise Exception('Improper entry number in row')
      for column_name in columns:
        matrix[row_name][column_name] = entries.pop(0)

    self._matrix = matrix

  def lookup_score(self, a, b):
    a = a.upper()
    b = b.upper()

    if a not in self._matrix or b not in self._matrix[a]:
      raise InvalidPairException('[%s, %s]' % (a, b))
    return self._matrix[a][b]


def run_repl(matrix):
  while True:
    try:
      user_input = input('>>> ').strip()
    except (EOFError, KeyboardInterrupt) as e:
      print()
      return
    if user_input.lower() in ['q', 'exit', 'quit']:
      return

    components = user_input.split()
    if len(components) != 2:
      continue
    try:
      print(matrix.lookup_score(components[0], components[1]))
    except InvalidPairException:
      continue

def main():
  if len(sys.argv) != 2:
    sys.exit('Usage: %s [matrix filename]')
  matrix_filename = sys.argv[1]
  matrix = Matrix(matrix_filename)
  run_repl(matrix)

if __name__ == '__main__':
  main()
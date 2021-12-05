#!/usr/bin/env python3

import fileinput
import pprint
import sys
import typing


class Cell(object):
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.marked: bool = False

    def compare(self, proposed_value: int) -> None:
        if proposed_value == self.value:
            self.marked = True

    def is_marked(self) -> bool:
        return self.marked

    def print(self) -> str:
        output = str(self.value).zfill(3)
        if self.is_marked():
            output = output.replace("0", "x", 1)
        return output

    def get_value(self) -> int:
        return self.value


class Board(object):
    def __init__(self, board_input: typing.List[str]) -> None:
        self.board: typing.List[typing.List[Cell]] = []
        for row in board_input:
            # print(f"DEBUG2: board.__init__ row is {row}")
            if row[0] == " ":
                row = row[1:]
            self.board.append([Cell(int(x)) for x in row.split()])

    def called_number(self, number: str) -> None:
        for row in self.board:
            for c in row:
                c.compare(int(number))

    def has_won_row(self) -> bool:
        for row in self.board:
            if all([c.is_marked() for c in row]):
                return True
        return False

    def has_won_column(self) -> bool:
        for idx in range(len(self.board[0])):
            if all([row[idx].is_marked() for row in self.board]):
                return True
        return False

    def has_won_diag(self) -> bool:
        diag1 = []
        for x in range(len(self.board[0])):
            for y in range(len(self.board)):
                diag1.append(self.board[y][x].is_marked())

        diag2 = []
        for x in range(len(self.board[0])-1, -1, -1):
            for y in range(len(self.board)):
                diag2.append(self.board[y][x].is_marked())

        if all(diag1):
            return True
        if all(diag2):
            return True
        return False

    def has_won(self) -> bool:
        if self.has_won_row():
            print(f"DEBUG5: row win")
            return True
        elif self.has_won_column():
            print(f"DEBUG5: column win")
            return True
        elif self.has_won_diag():
            print(f"DEBUG5: diag win")
            return True
        return False

    def print(self) -> None:
        for row in self.board:
            print(" ".join([c.print() for c in row]))

    def score(self) -> int:
        return sum([cell.get_value() for row in self.board for cell in row if not cell.is_marked()])
        # values = [cell.get_value() for row in self.board for cell in row if not cell.is_marked()]
        # print(f"DEBUG7: values are {values} sum is {sum(values)}")
        # return sum(values)


def main() -> None:
    called_numbers = []
    boards: typing.List[Board] = []
    current_board_input: typing.List[str] = []
    for line in fileinput.input():
        # print(f"DEBUG: len called_numbers is {len(called_numbers)} len(line) is {len(line.strip())} line is {line.strip()}")
        if len(called_numbers) == 0:
            called_numbers = line.strip().split(',')
        elif len(line.strip()) == 0:
            if len(current_board_input) > 0:
                boards.append(Board(current_board_input))
            current_board_input = []
        else:
            current_board_input.append(line.strip())
    boards.append(Board(current_board_input))

    # for board in boards:
    #     board.print()
    #     print()

    someone_won = False
    for called in called_numbers:
        for board in boards:
            board.called_number(called)
            if board.has_won():
                # print(f"called numbers are {called_numbers}")
                board.print()
                someone_won = True
                board_score = board.score()
                print(f"board_score is {board_score} called number is {called} product is {board_score*int(called)}")
                break
        if someone_won:
            break


if __name__ == "__main__":
    main()

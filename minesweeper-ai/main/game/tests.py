from constants import *
from game import Game


class TestGame:
    def test_place_mines(self):
        game = Game()
        num_mines = sum(1 for x in range(BOARD_WIDTH) for y in range(
            BOARD_HEIGHT) if game.board[x][y]["value"] == -1)
        assert num_mines == NUM_MINES

    def test_update_numbers(self):
        game = Game()
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                if game.board[x][y]["value"] == -1:
                    continue
                count = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if x + dx < 0 or x + dx >= BOARD_WIDTH or y + dy < 0 or y + dy >= BOARD_HEIGHT:
                            continue
                        if game.board[x + dx][y + dy]["value"] == -1:
                            count += 1
                assert game.board[x][y]["value"] == count

    def test_uncover_cell(self):
        game = Game()
        game.uncover_cell(0, 0)
        assert game.board[0][0]["state"] == CELL_UNCOVERED
        if game.board[0][0]["value"] == -1:
            assert game.game_over
        else:
            assert not game.game_over

    def run_all_tests(self):
        self.test_place_mines()
        self.test_update_numbers()
        self.test_uncover


def run_tests():
    test_game = TestGame()
    test_game.run_all_tests()
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()

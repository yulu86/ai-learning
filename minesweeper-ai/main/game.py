import random
import pygame

# 雷区大小
BOARD_WIDTH = 9
BOARD_HEIGHT = 9
NUM_MINES = 10

# 方格大小
CELL_SIZE = 48

# 游戏窗口大小
SCREEN_WIDTH = CELL_SIZE * BOARD_WIDTH
SCREEN_HEIGHT = CELL_SIZE * BOARD_HEIGHT

# 方格状态
CELL_COVERED = 0
CELL_UNCOVERED = 1
CELL_FLAGGED = 2

# 颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Game:
    def __init__(self):
        # 初始化 Pygame
        pygame.init()

        # 创建游戏窗口
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # 设置游戏窗口标题
        pygame.display.set_caption("扫雷游戏")

        # 加载图像
        self.load_images()

        self.reset()

    def reset(self):
        # 创建雷区
        self.board = [[{"value": 0, "state": CELL_COVERED}
                       for y in range(BOARD_HEIGHT)] for x in range(BOARD_WIDTH)]

        # 布置地雷
        self.place_mines()

        # 更新方格周围的数字
        self.update_numbers()

        # 设置游戏状态
        self.game_over = False
        self.game_won = False

    def load_images(self):
        self.images = {}
        self.images["covered"] = pygame.image.load(
            "images/covered.png").convert_alpha()
        self.images["uncovered"] = pygame.image.load(
            "images/uncovered.png").convert_alpha()
        self.images["mine"] = pygame.image.load(
            "images/mine.png").convert_alpha()
        self.images["flag"] = pygame.image.load(
            "images/flag.png").convert_alpha()

    def run(self):
        while True:
            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # 退出游戏
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    # 处理鼠标按下事件
                    x, y = event.pos
                    x = x // CELL_SIZE
                    y = y // CELL_SIZE
                    if event.button == 1:
                        # 左键按下
                        if self.board[x][y]["state"] == CELL_COVERED:
                            self.uncover_cell(x, y)
                            if self.board[x][y]["value"] == -1:
                                self.game_over = True
                    elif event.button == 3:
                        # 右键按下
                        if self.board[x][y]["state"] == CELL_COVERED:
                            self.board[x][y]["state"] = CELL_FLAGGED
                        elif self.board[x][y]["state"] == CELL_FLAGGED:
                            self.board[x][y]["state"] = CELL_COVERED

            # 绘制游戏界面
            self.draw()

            # 更新游戏界面
            pygame.display.update()

    def place_mines(self):
        # 随机布置地雷
        num_mines = 0
        while num_mines < NUM_MINES:
            x = random.randint(0, BOARD_WIDTH - 1)
            y = random.randint(0, BOARD_HEIGHT - 1)
            if self.board[x][y]["value"] == 0:
                self.board[x][y]["value"] = -1
                num_mines += 1

    def update_numbers(self):
        # 更新方格周围的数字
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                if self.board[x][y]["value"] == -1:
                    continue
                count = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if x + dx < 0 or x + dx >= BOARD_WIDTH or y + dy < 0 or y + dy >= BOARD_HEIGHT:
                            continue
                        if self.board[x + dx][y + dy]["value"] == -1:
                            count += 1
                self.board[x][y]["value"] = count

    def uncover_cell(self, x, y):
        # 翻开方格
        if self.board[x][y]["value"] == -1:
            # 点到地雷，游戏结束
            self.game_over = True
            self.board[x][y]["state"] = CELL_UNCOVERED
        elif self.board[x][y]["state"] == CELL_COVERED:
            # 翻开方格并显示数字
            self.board[x][y]["state"] = CELL_UNCOVERED
            if self.board[x][y]["value"] == 0:
                # 如果周围没有地雷，递归翻开周围的方格
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if x + dx < 0 or x + dx >= BOARD_WIDTH or y + dy < 0 or y + dy >= BOARD_HEIGHT:
                            continue
                        self.uncover_cell(x + dx, y + dy)

    def draw(self):
        # 绘制游戏界面
        self.screen.fill(WHITE)

        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                if self.board[x][y]["state"] == CELL_COVERED:
                    self.screen.blit(
                        self.images["covered"], (x * CELL_SIZE, y * CELL_SIZE))
                elif self.board[x][y]["state"] == CELL_UNCOVERED:
                    if self.board[x][y]["value"] == -1:
                        self.screen.blit(
                            self.images["mine"], (x * CELL_SIZE, y * CELL_SIZE))
                    elif self.board[x][y]["value"] == 0:
                        self.screen.blit(
                            self.images["uncovered"], (x * CELL_SIZE, y * CELL_SIZE))
                    else:
                        font = pygame.font.Font(None, CELL_SIZE)
                        text = font.render(
                            str(self.board[x][y]["value"]), True, BLACK)
                        self.screen.blit(
                            self.images["uncovered"], (x * CELL_SIZE, y * CELL_SIZE))
                        self.screen.blit(text, (x * CELL_SIZE + CELL_SIZE // 2 - text.get_width(
                        ) // 2, y * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2))
                elif self.board[x][y]["state"] == CELL_FLAGGED:
                    self.screen.blit(
                        self.images["flag"], (x * CELL_SIZE, y * CELL_SIZE))

        if self.game_over:
            font = pygame.font.Font(None, SCREEN_HEIGHT // 10)
            text = font.render("Game Over", True, RED)
            self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() //
                             2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

        # 绘制网格线
        for x in range(BOARD_WIDTH + 1):
            pygame.draw.line(self.screen, BLACK, (x * CELL_SIZE,
                             0), (x * CELL_SIZE, SCREEN_HEIGHT))
        for y in range(BOARD_HEIGHT + 1):
            pygame.draw.line(self.screen, BLACK,
                             (0, y * CELL_SIZE), (SCREEN_WIDTH, y * CELL_SIZE))


if __name__ == "__main__":
    game = Game()
    game.run()

# Имопортируем необходимые пакеты
from easyAI import TwoPlayersGame, id_solve, Human_Player, AI_Player
from easyAI.AI import TT


# Создание нового класа
class LastCoin_init(TwoPlayersGame):
    """Наследуется от TwoPlayersGame"""

    def __init__(self, players):
        # Определение игроков и игрока который начинает игру
        self.players = players
        self.nplayer = 1
        #  Определяем кол-во монет используемых для игры
        self.num_coins = int(input("Введите кол-во монет, которые будут используемых для игры "))
        # Максимальное кол-во монет, которое игрок может взять за ход
        self.max_coins = int(input("Введите кол-во монет, которые можно взять за 1 ход "))

    # Определяем все возможные ходы
    def possible_moves(self):
        return [str(a) for a in range(1, self.max_coins + 1)]

    # Определяем удаление монет
    def make_move(self, move):
        self.num_coins -= int(move)

    # Определяем, кто взял последнюю монету
    def win_game(self):
        return self.num_coins <= 0

    # Определяем условия победы (когда останавливаться) (когда кто-то победил)
    def is_over(self):
        return self.win_game()

    # Расчитываем счёт (подсчёт очков)
    def score(self):
        return 100 if self.win_game() else 0

    # Определяем кол-во монет оставшихся в стопке
    def show(self):
        print(self.num_coins, ' монеток осталось в стоп0чке')

    # Считаем балы
    def scoring(self):
        return -100 if not self.win_game() else 0


if __name__ == "__main__":
    tt = TT()
    LastCoin_init.ttentry = lambda self: self.num_coins
    # Все решения игры:
    r, d, m = id_solve(LastCoin_init, range(2, 20), win_score=100, tt=tt)
    print(r, d, m)
    # Решаем кому первому ход делать
    game = LastCoin_init([AI_Player(tt), Human_Player()])
    game.play()

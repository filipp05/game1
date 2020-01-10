class World:
    def __init__(self, max_err):
        self.max_err = max_err
        self.current_day = 1
        self.days = []

    def show_wellcome_message(self):
        # todo
        print("ткст приветствия из предыдущей игры")


class DayTask:
    def __init__(self, day_quest, day_corr_ans, day_variants):
        self.question = day_quest
        self.correct_ans = day_corr_ans
        self.ans_variants = day_variants

    def show(self):
        print(self.question)
        print(self.ans_variants)

    def is_day_complete(self, user_ans):
        return user_ans == self.correct_ans


class User:
    def __init__(self):
        self.errors = 0
        self.level = 0


def main():
    max_err = int(input())
    world = World(max_err)
    world.show_wellcome_message()

main()

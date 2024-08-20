import random


class ExceptionRaiser:
    @staticmethod
    def throw_error():
        if random.random() < 0.2:  # 20% chance of failure
            raise Exception('Unexpected error')

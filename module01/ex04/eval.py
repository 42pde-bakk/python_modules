class Evaluator:
    @staticmethod
    def zip_evaluate(coefs: list, words: list):
        if not Evaluator.__parameters_are_valid(coefs, words):
            return -1
        return sum(coef * len(word) for (coef, word) in zip(coefs, words))

    @staticmethod
    def enumerate_evaluate(coefs: list, words: list):
        if not Evaluator.__parameters_are_valid(coefs, words):
            return -1
        return sum(coef * len(words[i]) for (i, coef) in enumerate(coefs))

    @staticmethod
    def __parameters_are_valid(coefs: list, words: list) -> bool:
        if not all(isinstance(x, list) for x in (coefs, words)) or len(coefs) != len(words):
            return False
        if not all(isinstance(w, str) for w in words) or not all(isinstance(c, (int, float)) for c in coefs):
            return False
        return True


def main():
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    zip_evaluate = Evaluator.zip_evaluate(coefs, words)
    enumerate_evaluate = Evaluator.enumerate_evaluate(coefs, words)
    print(f'{zip_evaluate=}, {enumerate_evaluate=}')
    assert zip_evaluate == 32 == enumerate_evaluate
    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    zip_evaluate = Evaluator.zip_evaluate(coefs, words)
    enumerate_evaluate = Evaluator.enumerate_evaluate(coefs, words)
    print(f'{zip_evaluate=}, {enumerate_evaluate=}')
    assert enumerate_evaluate == -1 == zip_evaluate


if __name__ == '__main__':
    main()

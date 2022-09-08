class Evaluator:

    @staticmethod
    def zip_evaluate(coefs: list, words: list):
        if len(coefs) != len(words):
            return -1
        return sum(coef * len(word) for (coef, word) in zip(coefs, words))

    @staticmethod
    def enumerate_evaluate(coefs: list, words: list):
        if len(coefs) != len(words):
            return -1
        return sum(coef * len(words[i]) for (i, coef) in enumerate(coefs))


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

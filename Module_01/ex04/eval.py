Class Evaluator:
    @staticmethod
    def zip_evaluate(self, coefs, words):
        if len(coefs) is not len(words):
            return -1
        new_str = zip(coefs, words)
    @staticmethod
    def enumerate_evaluate(self, coefs, words):
        if len(coefs) is not len(words):
            return -1

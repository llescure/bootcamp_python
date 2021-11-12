class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) is not len(words):
            print(-1)
            return
        result = 0
        lenght_words = []
        for word in words:
            lenght_words.append(float(len(word)))
        new_str = list(zip(coefs, lenght_words))
        for elements in new_str:
            result += elements[0] * elements[1]
        print(result)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) is not len(words):
            print(-1)
            return
        lenght_words = []
        result = 0
        for word in words:
            lenght_words.append(float(len(word)))
        for index1, lenght in enumerate(lenght_words):
            result += lenght * coefs[index1]
        print(result)

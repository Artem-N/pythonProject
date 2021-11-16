class CalcModel:
    ERROR_MASSAGE = "Error occurred"

    def evaluate_expression(self, expression):
        try:
            return str(eval(expression))
        except (TypeError, ZeroDivisionError, SyntaxError):
            return self.__class__.ERROR_MASSAGE

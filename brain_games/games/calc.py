"""Module for calculate game."""
import operator, random

rules = 'What is the result of the expression?'
OPERATOR = ((operator.add, '+'), (operator.sub, '-'), (operator.mul, '*'))


def round_data():
    """Code for engine."""
    first_num = random.randint(0, 100)
    second_num = random.randint(0, 100)
    operator, symb_operator = random.choice(OPERATOR)
    question = '%s%s%s' % (first_num, symb_operator, second_num)
    right_answer = str(operator(first_num, second_num))
    return question, right_answer

import pytest

import lab4


def rpnOf(expression):
    return " ".join(lab4.expressionToRpn(expression))


#tokenize
def test_tokenizeSimple():
    assert lab4.tokenize("12+3.5*(2-1)") == ["12", "+", "3.5", "*", "(", "2", "-", "1", ")"]


def test_tokenizeSkipsSpaces():
    assert lab4.tokenize("  1   +   2 ") == ["1", "+", "2"]


def test_tokenizeUnaryMinus():
    assert lab4.tokenize("-1") == ["u-", "1"]
    assert lab4.tokenize("2*-3") == ["2", "*", "u-", "3"]
    assert lab4.tokenize("(-1)") == ["(", "u-", "1", ")"]
    assert lab4.tokenize("1--1") == ["1", "-", "u-", "1"]


def test_tokenizeUnaryPlusIsSkipped():
    assert lab4.tokenize("+5") == ["5"]
    assert lab4.tokenize("1++2") == ["1", "+", "2"]


def test_tokenizeUnknownSymbol():
    with pytest.raises(ValueError):
        lab4.tokenize("2 & 3")
    with pytest.raises(ValueError):
        lab4.tokenize("2 + a")


def test_tokenizeWrongNumber():
    with pytest.raises(ValueError):
        lab4.tokenize("1.2.3")
    with pytest.raises(ValueError):
        lab4.tokenize("2 + .")


#RPN
def test_rpnSimple():
    assert rpnOf("1 + 2") == "1 2 +"


def test_rpnPriority():
    assert rpnOf("1 + 2 * 3") == "1 2 3 * +"
    assert rpnOf("1 * 2 + 3") == "1 2 * 3 +"


def test_rpnBrackets():
    assert rpnOf("(1 + 2) * 3") == "1 2 + 3 *"
    assert rpnOf("2 * (3 + 4) * 5") == "2 3 4 + * 5 *"


def test_rpnLeftAssociativity():
    assert rpnOf("8 - 3 - 2") == "8 3 - 2 -"
    assert rpnOf("8 / 4 / 2") == "8 4 / 2 /"


def test_rpnPowerIsRightAssociative():
    assert rpnOf("2 ^ 3 ^ 2") == "2 3 2 ^ ^"


def test_rpnClassicExample():
    assert rpnOf("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3") == "3 4 2 * 1 5 - 2 3 ^ ^ / +"


def test_rpnUnaryMinus():
    assert rpnOf("-2 ^ 2") == "2 2 ^ u-"
    assert rpnOf("2 * -3") == "2 3 u- *"


def test_rpnBracketsNotBalanced():
    with pytest.raises(ValueError):
        lab4.expressionToRpn("(1 + 2")
    with pytest.raises(ValueError):
        lab4.expressionToRpn("1 + 2)")


#calculate
def test_calculateSimple():
    assert lab4.calculate("1 + 2") == 3
    assert lab4.calculate("10 - 4") == 6
    assert lab4.calculate("6 * 7") == 42
    assert lab4.calculate("9 / 4") == 2.25
    assert lab4.calculate("2 ^ 10") == 1024


def test_calculatePriorityAndBrackets():
    assert lab4.calculate("2 + 3 * 4") == 14
    assert lab4.calculate("(2 + 3) * 4") == 20
    assert lab4.calculate("((1 + 2) * (3 + 4)) / 7") == 3


def test_calculateAssociativity():
    assert lab4.calculate("8 - 3 - 2") == 3
    assert lab4.calculate("100 / 10 / 5") == 2
    assert lab4.calculate("2 ^ 3 ^ 2") == 512


def test_calculateUnaryMinus():
    assert lab4.calculate("-5") == -5
    assert lab4.calculate("-2 ^ 2") == -4
    assert lab4.calculate("(-2) ^ 2") == 4
    assert lab4.calculate("2 * -3") == -6
    assert lab4.calculate("5 - -3") == 8
    assert lab4.calculate("-(2 + 3)") == -5
    assert lab4.calculate("2 ^ -1") == 0.5


def test_calculateDecimalNumbers():
    assert lab4.calculate("1.5 + 2.25") == 3.75
    assert lab4.calculate(".5 * 4") == 2


def test_calculateClassicExample():
    assert lab4.calculate("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3") == pytest.approx(3.0001220703125)


def test_calculateManyOperands():
    assert lab4.calculate("1+2+3+4+5+6+7+8+9+10") == 55
    assert lab4.calculate("2*3*4*5") == 120


def test_calculateDivisionByZero():
    with pytest.raises(ValueError):
        lab4.calculate("1 / 0")
    with pytest.raises(ValueError):
        lab4.calculate("1 / (2 - 2)")


def test_calculateWrongPower():
    with pytest.raises(ValueError):
        lab4.calculate("(-8) ^ 0.5")
    with pytest.raises(ValueError):
        lab4.calculate("0 ^ -1")


def test_calculateTooLargeNumber():
    with pytest.raises(ValueError):
        lab4.calculate("10 ^ 1000")
    with pytest.raises(ValueError):
        lab4.calculate("10 ^ 308 * 10")


def test_calculateWrongExpressions():
    for expression in ["", "   ", "()", "1 +", "* 2", "1 2", "1 + * 2", "(1)(2)", "2 (3)", "1 -", "^ 2"]:
        with pytest.raises(ValueError):
            lab4.calculate(expression)


#calculateRpn
def test_calculateRpn():
    assert lab4.calculateRpn(["3", "4", "+", "2", "*"]) == 14


def test_calculateRpnNotEnoughOperands():
    with pytest.raises(ValueError):
        lab4.calculateRpn(["3", "+"])
    with pytest.raises(ValueError):
        lab4.calculateRpn(["u-"])


#formatNumber 
def test_formatNumber():
    assert lab4.formatNumber(3.0) == "3"
    assert lab4.formatNumber(-0.0) == "0"
    assert lab4.formatNumber(2.5) == "2.5"
    assert lab4.formatNumber(0.1 + 0.2) == "0.3"
    assert lab4.formatNumber(1 / 3) == "0.3333333333"


#main 
def test_mainSession(monkeypatch, capsys):
    answers = iter(["1 + 2 * 3", "(1 + 2) * 3", "1 / 0", "2 +", ""])
    monkeypatch.setattr("builtins.input", lambda text: next(answers))
    lab4.main()
    lines = capsys.readouterr().out.splitlines()
    assert lines == ["RPN: 1 2 3 * +", "Result: 7",
                     "RPN: 1 2 + 3 *", "Result: 9",
                     "RPN: 1 0 /", "Error: Division by zero",
                     "RPN: 2 +", "Error: Not enough operands",
                     "Exit()"]
import pytest
from source import stack1

def test_stack_push_and_pop():
    s = stack1.Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1
    with pytest.raises(ValueError):
        s.pop()

def test_stack_peek():
    s = stack1.Stack()
    s.push(1)
    assert s.peek() == 1
    s.push(2)
    assert s.peek() == 2
    s.pop()
    assert s.peek() == 1
    s.pop()
    with pytest.raises(ValueError):
        s.peek()

def test_stack_length():
    s = stack1.Stack()
    assert len(s) == 0
    s.push(1)
    assert len(s) == 1
    s.push(2)
    assert len(s) == 2
    s.pop()
    assert len(s) == 1
    s.pop()
    assert len(s) == 0

def test_check_parenthesis():
    assert stack1.check_parenthesis("") == True
    assert stack1.check_parenthesis("()") == True
    assert stack1.check_parenthesis("([])") == True
    assert stack1.check_parenthesis("{[()]}") == True
    assert stack1.check_parenthesis("{[(])}") == False
    assert stack1.check_parenthesis("([)]") == False
    assert stack1.check_parenthesis("{[}") == False
    assert stack1.check_parenthesis("}") == False

def test_postfix_eval():
    assert stack1.postfix_eval("2 3 +") == 5
    assert stack1.postfix_eval("2 3 * 4 +") == 10
    assert stack1.postfix_eval("5 1 2 + 4 * + 3 -") == 14
    assert stack1.postfix_eval("3 4 2 * 1 5 - 2 3 ^ ^ / +") == 3

    with pytest.raises(ValueError):
        stack1.postfix_eval("2 +")
    with pytest.raises(ValueError):
        stack1.postfix_eval("2 3")
    with pytest.raises(ValueError):
        stack1.postfix_eval("2 3 + 4 +")  # Extra operand

    with pytest.raises(ValueError):
        stack1.postfix_eval("2 a +")  # Invalid token

    with pytest.raises(ValueError):
        stack1.postfix_eval("")  # Empty input
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=line-too-long

"""Интеграционные тесты транслятора и машины
"""

import pytest
import machine
import translator


def start(source_code, output_file, input_file):
    translator.main([source_code, output_file])
    if input_file == "":
        return machine.main([output_file])
    return machine.main([output_file, input_file])


@pytest.mark.golden_test
def test_hello():
    output = start("examples/hello.asm", "examples/hello_code.out", "")
    assert output == "Hello world!\0"


@pytest.mark.golden_test
def test_cat():
    output = start("examples/cat.asm", "examples/cat_code.out", "examples/input.txt")
    assert output == "Good news, everyone!\n"


@pytest.mark.golden_test
def test_prob2():
    output = start("examples/prob2.asm", "examples/prob2_code.out", "")
    print(output)
    assert output == '4613732'

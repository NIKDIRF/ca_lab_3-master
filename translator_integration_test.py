# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-self-use

"""Интеграционные тесты транслятора и машины
"""

import pytest

import isa
import translator


def run_test(input_file, output_file, correct_file):
    translator.main([input_file, output_file])
    result = isa.read_code(output_file)
    correct_code = isa.read_code(correct_file)
    assert result == correct_code


@pytest.mark.golden_test
def test_prob2():
    run_test("examples/prob2.asm", "examples/prob2_code.out",
             "examples/correct_prob2_code.out")


@pytest.mark.golden_test
def test_cat():
    run_test("examples/cat.asm", "examples/cat_code.out",
             "examples/correct_cat_code.out")


@pytest.mark.golden_test
def test_hello_world():
    run_test("examples/hello.asm", "examples/hello_code.out",
             "examples/correct_hello_code.out")

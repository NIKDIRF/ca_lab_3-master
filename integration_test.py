# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

"""Интеграционные тесты транслятора и машины
"""
import os
import tempfile
import pytest
import isa
import machine
import translator


@pytest.mark.golden_test("golden/*.yml")
def test_prob2(golden):
    with tempfile.TemporaryDirectory() as tmpdirname:
        source = os.path.join(tmpdirname, "source.asm")
        binary = os.path.join(tmpdirname, "binary.json")
        inp = os.path.join(tmpdirname, "inp.txt")

        with open(source, "w", encoding="utf-8") as src,  open(inp, "w", encoding="utf-8") as input_file:
            src.write(golden["source"])
            input_file.write(golden.get("input", ""))

        translator.main([source, binary])
        result, data_section = isa.read_code(binary)
        assert result == golden.out['code']
        assert data_section == golden.out['data']

        if not golden.get("input", None):
            assert machine.main([binary]) == golden.out['output']
        else:
            assert machine.main([binary, inp]) == golden.out['output']

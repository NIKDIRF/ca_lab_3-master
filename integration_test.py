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
        bin = os.path.join(tmpdirname, "bin.json")
        inp = os.path.join(tmpdirname, "inp.txt")

        with open(source, "w", encoding="utf-8") as s,  open(inp, "w", encoding="utf-8") as i:
            s.write(golden["source"])
            i.write(golden.get("input", ""))

        translator.main([source, bin])
        result, data_section = isa.read_code(bin)
        assert result == golden.out['code']
        assert data_section == golden.out['data']

        if not golden.get("input", None):
            assert machine.main([bin]) == golden.out['output']
        else:
            assert machine.main([bin, inp]) == golden.out['output']

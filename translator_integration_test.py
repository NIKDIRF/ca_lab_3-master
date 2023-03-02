# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

"""Интеграционные тесты транслятора и машины
"""
import os
import tempfile
import pytest
import isa
import translator


@pytest.mark.golden_test("golden/*.yml")
def test_prob2(golden):
    with tempfile.TemporaryDirectory() as tmpdirname:
        source = os.path.join(tmpdirname, "source.asm")
        bin = os.path.join(tmpdirname, "bin.json")

        with open(source, "w", encoding="utf-8") as file:
            file.write(golden["source"])

        translator.main([source, bin])
        result, data_section = isa.read_code(bin)
        assert result == golden.out['code']
        assert data_section == golden.out['data']

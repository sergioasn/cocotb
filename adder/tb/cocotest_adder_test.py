from cocotb_test.run import run
import pytest
import os

#SIM=ghdl pytest -s cocotest_adder_test.py
@pytest.mark.skipif(os.getenv("SIM") == "ghdl", reason="VHDL not suported")
def test_adder_vhdl():
    run(vhdl_sources=["$(PWD)/../../src/adder.vhd"],
        simulation_args=["--wave=adder.ghw"],
        toplevel="adder",
        module="adder_test"
        )

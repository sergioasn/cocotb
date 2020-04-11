
TOPLEVEL_LANG=verilog
VERILOG_SOURCES = $(PWD)/../src/adder.v
TOPLEVEL=adder
MODULE=adder_test
#TESTCASE=adder_basic_test,adder_basic2_test
SIM=verilator
COCOTB_HDL_TIMEPRECISION = 1us
# EXTRA_ARGS += --coverage
# --coverage
VERILATOR_TRACE = 1
#SIM_ARGS=--vcd=func.vcd
include $(shell cocotb-config --makefiles)/Makefile.inc
include $(shell cocotb-config --makefiles)/Makefile.sim

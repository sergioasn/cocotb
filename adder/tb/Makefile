
TOPLEVEL_LANG=verilog
VERILOG_SOURCES = $(PWD)/../src/adder.v
TOPLEVEL=adder
MODULE=adder_test
SIM=verilator
# COCOTB_HDL_TIMEPRECISION = 1us
EXTRA_ARGS += --coverage
# VERILATOR_TRACE = 1
include $(shell cocotb-config --makefiles)/Makefile.inc
include $(shell cocotb-config --makefiles)/Makefile.sim

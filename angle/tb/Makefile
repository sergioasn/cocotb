
TOPLEVEL_LANG=verilog
VERILOG_SOURCES = $(PWD)/../src/angle_venv.v
TOPLEVEL=angle_venv
MODULE=angle_test
SIM=verilator
COCOTB_HDL_TIMEPRECISION = 1us
EXTRA_ARGS += --coverage
VERILATOR_TRACE = 1
include $(shell cocotb-config --makefiles)/Makefile.inc
include $(shell cocotb-config --makefiles)/Makefile.sim

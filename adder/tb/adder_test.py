import cocotb
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock
from cocotb.binary import BinaryValue, BinaryRepresentation
from cocotb.scoreboard import Scoreboard
from cocotb.monitors import Monitor
from cocotb.drivers import Driver
from cocotb_coverage.coverage import *
from cocotb_coverage.crv import *
from adder_model import adder_model
import numpy as np
import math
import struct
# ==============================================================================
class inMonitor(Monitor):
    def __init__(self, name, clock, dv ,data0, data1, callback=None, event=None):
        self.name = name
        self.clock = clock
        self.dv = dv
        self.data0 = data0
        self.data1 = data1
        Monitor.__init__(self, callback, event)

    @cocotb.coroutine
    def _monitor_recv(self):
        clkedge = RisingEdge(self.clock)
        while True:
            # Capture signal at rising edge of clock
            yield clkedge
            if self.dv == 1:
                vec = [int(self.data0.value), int(self.data1.value)]
                # print(vec)
                self._recv(vec)
# ==============================================================================
class outMonitor(Monitor):
    def __init__(self, name, data_out, dv_out, clock, callback=None, event=None):
        self.name = name
        self.data_out = data_out
        self.dv_out = dv_out
        self.clock = clock
        Monitor.__init__(self, callback, event)

    @cocotb.coroutine
    def _monitor_recv(self):
        clkedge = RisingEdge(self.clock)
        # Capture signal at rising edge of clock
        while True:
            yield clkedge
            if self.dv_out == 1:
                vec = int(self.data_out.value)
                # print (vec)
                self._recv(vec)

# ==============================================================================
class TB(object):
    def __init__(self, dut):
        self.dut = dut
        # Input monitor
        self.input_mon = inMonitor("input", dut.clk, dut.dv, dut.data0_in, dut.data1_in, callback=self.model)
        # Output monitor
        self.output_mon = outMonitor("output", dut.data_out,dut.dv_out, dut.clk)
        self.expected_output = []
        self.scoreboard = Scoreboard(dut)
        self.scoreboard.add_interface(self.output_mon, self.expected_output, strict_type=True)

    def model(self,transaction):
        #transaction viene de input monitos _recv, ese dato es transaction
        # if not self.stopped:
            # self.expected_output.append(transaction)
        outModel = transaction[0]+transaction[1]
        self.expected_output.append(outModel)

    # def start(self):
    #     """Start generating input data."""
    #     self.input_mon.start()
    #
    # def stop(self):
    #     """Stop generating input data.
    #     Also stop generation of expected output transactions.
    #     One more clock cycle must be executed afterwards so that the output of
    #     the D flip-flop can be checked.
    #     """
    #     # self.input_drv.stop()
    #     self.stopped = True

# ==============================================================================
def gen_input():
    # Generate random data
    dataOutInt = np.random.randint(0,2**2,10)
    return dataOutInt

# # ==============================================================================
ADDER_Coverage = coverage_section (
  #CoverPoint("top.c", vname="C", bins = [True, False]),
  CoverPoint(name ="top.(A <250)", xf = lambda dut,data0_in,data1_in  : int(dut.data_out) < 250, bins = list(range(0,260))),
  #[True, False]
  CoverPoint(name ="top.(A <150)", xf = lambda dut,data0_in,data1_in  : int(dut.data_out) <150, bins = [True, False]),
  CoverPoint(name ="top.(A >250)", xf = lambda dut,data0_in,data1_in  : int(dut.data_out) >250, bins = [True, False]),
  CoverPoint(name ="top.(A =250)", xf = lambda dut,data0_in,data1_in  : int(dut.data_out) ==250, bins = [True, False]),
  CoverPoint(name ="top.(A =0)", xf = lambda dut,data0_in,data1_in  : int(dut.data_out) ==0, bins = [True, False]),
  CoverCross(name ="top.rwXfull", items = ["top.(A <150)", "top.(A >250)"]),
)
# # ==============================================================================
# @ADDER_Coverage
# def check(dut,data0_in,data1_in):
#     if int(dut.data_out) != adder_model(data0_in,data1_in):
#         raise TestFailure(
#             "Randomised test failed with: %s + %s = %s" %
#             (int(dut.data0_in), int(dut.data1_in), int(dut.data_out)))
#     #else:  # these last two lines are not strictly necessary
#         #dut._log.info("Ok!")

@cocotb.test(skip = False, stage=1)
def adder_test(dut):
    # Initialise signals
    dut.reset <= 1
    dut.dv <= 0
    # Create clock
    CLK_PERIOD = 10
    cocotb.fork(Clock(dut.clk, CLK_PERIOD).start())
    yield Timer(CLK_PERIOD * 5)
    dut.reset <= 0
    yield Timer(CLK_PERIOD*5)
    # call function of generate data
    dataIn = gen_input()
    # call TB class
    tb = TB(dut)
    for i in range(0,len(dataIn)-1):
        dut.dv <= 1
        dut.data0_in <= int(dataIn[i])
        dut.data1_in <= int(dataIn[i+1])
        # yield Timer(CLK_PERIOD)
        # dut.dv <= 0
        # tb.model(dataIn[i],dataIn[i+1])
        yield Timer(CLK_PERIOD*2)
        # check(dut,dataIn[i],dataIn[i+1])
    # Stop the stimulus
    dut.dv <= 0

    # coverage =coverage_db["top"].cover_percentage
    # dut._log.info("Coverage = %f %%", coverage)
    # coverage_db.report_coverage(dut._log.info, bins=True)
    # coverage_db.export_to_xml(xml_name="coverage.xml")

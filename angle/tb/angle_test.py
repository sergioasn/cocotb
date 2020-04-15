import cocotb
from cocotb.triggers import Timer, RisingEdge, FallingEdge, ReadOnly
from cocotb.result import TestFailure
from cocotb.clock import Clock
from cocotb.binary import BinaryValue, BinaryRepresentation
from cocotb.scoreboard import Scoreboard
from cocotb.monitors import Monitor
from cocotb.drivers import Driver
from cocotb.drivers import BitDriver
from cocotb_coverage.coverage import *
from cocotb_coverage.crv import *
from angle_model import angle_model
import numpy as np
import math
import struct
# ==============================================================================
class inMonitor(Monitor):
    def __init__(self, name, clock, theta_in ,freq, SEQUENCE,callback=None, event=None):
        self.name = name
        self.clock = clock
        self.theta_in = theta_in
        self.freq = freq
        self.SEQUENCE = SEQUENCE
        # self.data = event
        Monitor.__init__(self, callback, event)

    @cocotb.coroutine
    def _monitor_recv(self):
        clkedge = RisingEdge(self.clock)
        while True:
            # Capture signal at rising edge of clock
            yield clkedge
            vec = [int(self.theta_in.value), int(self.freq.value)]
            self._recv(vec)
# ==============================================================================
class outMonitor(Monitor):
    def __init__(self, name, theta_out, clock, CYCLE, callback=None, event=None):
        self.name = name
        self.theta_out = theta_out
        self.clock = clock
        self.CYCLE = CYCLE
        Monitor.__init__(self, callback, event)

    @cocotb.coroutine
    def _monitor_recv(self):
        clkedge = RisingEdge(self.clock)
        # Capture signal at rising edge of clock

        while True:
            yield clkedge
            yield ReadOnly()
            vec = int(self.theta_out.value)
            # print('out')
            # print(vec)
            self._recv(vec)
# ==============================================================================
class TB(object):
    def __init__(self, dut):
        self.dut = dut
        #input driver solo para bit
        # self.input_drv = BitDriver(signal=dut.theta_in, clk=dut.clk, generator=gen_input())
        # Input monitor
        self.input_mon = inMonitor("input", dut.clk, dut.theta_in, dut.freq,dut.SEQUENCE, callback=self.model)
        # Output monitor
        self.output_mon = outMonitor("output", dut.theta_out, dut.clk, dut.CYCLE)
        self.expected_output = []
        self.scoreboard = Scoreboard(dut)
        self.scoreboard.add_interface(self.output_mon, self.expected_output, strict_type=True)

    def model(self,transaction):
        outModel = angle_model(transaction[0],transaction[1])
        # print('outmodel')
        # print (outModel)
        self.expected_output.append(int(outModel))

# ==============================================================================
def gen_input(loop):
    # Generate random data tupla
    data_gen = np.random.randint(0,2**8,loop)
    wait_gen= np.random.randint(0,2**12,loop)
    return [data_gen,wait_gen]

# # ==============================================================================
# ADDER_Coverage = coverage_section (
#   #CoverPoint("top.c", vname="C", bins = [True, False]),
#   CoverPoint(name ="top.(A <250)", xf = lambda dut,data0_in,data1_in  : int(dut.data_out) < 250, bins = list(range(0,260))),
#   #[True, False]
#   CoverPoint(name ="top.(A <150)", xf = lambda dut,data0_in,data1_in  : int(dut.data_out) <150, bins = [True, False]),
#   CoverPoint(name ="top.(A >250)", xf = lambda dut,data0_in,data1_in  : int(dut.data_out) >250, bins = [True, False]),
#   CoverPoint(name ="top.(A =250)", xf = lambda dut,data0_in,data1_in  : int(dut.data_out) ==250, bins = [True, False]),
#   CoverPoint(name ="top.(A =0)", xf = lambda dut,data0_in,data1_in  : int(dut.data_out) ==0, bins = [True, False]),
#   CoverCross(name ="top.rwXfull", items = ["top.(A <150)", "top.(A >250)"]),
# )
# # ==============================================================================
# @ADDER_Coverage
# def check(dut,data0_in,data1_in):
#     if int(dut.data_out) != adder_model(data0_in,data1_in):
#         raise TestFailure(
#             "Randomised test failed with: %s + %s = %s" %
#             (int(dut.data0_in), int(dut.data1_in), int(dut.data_out)))
    #else:  # these last two lines are not strictly necessary
        #dut._log.info("Ok!")

@cocotb.test(skip = False, stage=1)
def angle_test(dut):
    # Initialise signals
    dut.RESET <= 1
    # Create clock
    CLK_PERIOD = 10
    cocotb.fork(Clock(dut.clk, CLK_PERIOD).start())
    yield Timer(CLK_PERIOD * 5)
    dut.RESET <= 0
    # call function of generate data
    dut.SEQUENCE <= 1
    # call TB class
    tb = TB(dut)
    # yield Timer(CLK_PERIOD)
    stimulus=gen_input(2)
    data_in=stimulus[0]
    wait_in=stimulus[1]
    # print(data_in[0,0])
    for i in range(0,len(data_in)):
        dut.theta_in <= int(data_in[i])
        yield Timer(CLK_PERIOD*wait_in[i])
    # Stop the stimulus
    yield Timer(CLK_PERIOD*5)
    raise tb.scoreboard.result

    # coverage =coverage_db["top"].cover_percentage
    # dut._log.info("Coverage = %f %%", coverage)
    # coverage_db.report_coverage(dut._log.info, bins=True)
    # coverage_db.export_to_xml(xml_name="coverage.xml")

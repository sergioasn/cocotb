`timescale 1ns / 1ps
//*****************************************************************************
// File:           adder.v
// Project:
// Author:         salonso
// Description:    adder
// Limitations/Bugs:
//*****************************************************************************
module adder(
  input clk,
  input reset,
  input dv,
  input [31:0]   data0_in,
  input [31:0]   data1_in,
  output reg [31:0] data_out,
  output reg dv_out);

always @ (posedge clk) begin
  if( reset) begin
    data_out <= 0;
    dv_out  <= 0;
  end
  else begin
  dv_out  <= 0;
    if( dv == 1) begin
      data_out <= data0_in + data1_in;
      dv_out  <= 1;
    end
  end
end

`ifndef VERILATOR
  // Dump waves
  // Gtkwave file
  initial begin
    $dumpfile("dump.vcd");
    $dumpvars(1, adder);
  end
`endif

endmodule

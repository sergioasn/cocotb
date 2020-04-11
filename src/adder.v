`timescale 1ns / 1ps
//*****************************************************************************
// File:           angle_gen.v
// Project:
// Author:         PTrujillo
// Description:    Own angle generator
// Limitations/Bugs:
//*****************************************************************************
module adder(
  input clk,
  input reset,
  input dv,
  input [31:0]   data0_in,
  input [31:0]   data1_in,
  output  [31:0] data_out,
  output  dv_out);

reg [31:0] r_sum_out;
reg  r_dv_out;

always @ (posedge clk) begin
  if( reset) begin
    r_sum_out <= 0;
    r_dv_out  <= 0;
  end
  else begin
  r_dv_out  <= 0;
    if( dv == 1) begin
      r_sum_out <= data0_in + data1_in;
      r_dv_out  <= 1;
    end
    // else begin
    // end
  end
end

assign data_out = r_sum_out;
assign dv_out = r_dv_out;
`ifndef VERILATOR
  // Dump waves
  initial begin
    $dumpfile("dump.vcd");
    $dumpvars(1, adder);
  end
`endif

endmodule

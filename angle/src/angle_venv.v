`timescale 1ns / 1ps
//*****************************************************************************
// File:           angle_gen.v
// Project:
// Author:         PTrujillo
// Description:    Own angle generator
// Limitations/Bugs:
//*****************************************************************************

module angle_venv(
  input clk,
  input RESET,
  input [9:0] theta_in,
  input [1:0] freq, /* 1 = 50Hz; 0 = 60Hz, 2 = CLK(SIMU), 3 = 60Hz(SIMU) */
  input SEQUENCE,
  output reg CYCLE,
  output [9:0] theta_out
  );

/* registers */
reg [8:0] counter;
reg [9:0] theta_gen_aux;
reg [9:0] last_theta;//, last_theta_timeout;
reg cycle_set;

/* wires */
wire [8:0]max_count;

assign max_count = (freq == 3)?408:(freq == 2)?0:(freq == 1)?489:408; /* 489 -> 49.92Hz 408 -> 59.83Hz*/

always @ (posedge clk) begin
  if( RESET) begin
    counter <= 0;
    last_theta <= 0;
    theta_gen_aux <= 0;
  end
  else begin
    if( theta_in != last_theta) begin
      theta_gen_aux <= theta_in;
      last_theta <= theta_in;
      counter <= 9'd0;
      CYCLE <= 1;
    end
    // else if( counter < max_count) begin
    //   counter <= counter + 1;
    // end
    else begin
      if( freq < 3) begin /* No new angle received */
        if( SEQUENCE) begin
          if( theta_gen_aux < 1023) begin
            theta_gen_aux <= theta_gen_aux + 1;
            CYCLE <= 1;
          end
          else begin
            theta_gen_aux <= 0;
            CYCLE <= 1;
          end
        end
        else begin
          if( theta_gen_aux > 0) begin
            theta_gen_aux <= theta_gen_aux - 1;
            CYCLE <= 0;
          end
          else begin
            theta_gen_aux <= 1023;
            CYCLE <= 1;
          end
        end
      end
      counter <= 0;
    end /* else*/
  end /* else*/
end /* always*/

assign theta_out = theta_gen_aux; /* Sawtooth generated according the phase sequence. */
`ifndef VERILATOR
  // Dump waves
  // Gtkwave file
  initial begin
    $dumpfile("dump.vcd");
    $dumpvars(1, angle_venv);
  end
`endif
endmodule

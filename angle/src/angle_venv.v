`timescale 1ns / 1ps


module angle_venv(
  input clk,
  input rst,
  input [9:0] theta_in,
  input freq,
  input sequence_in,
  output reg [9:0] theta_out
  );

wire [8:0] w9_prescaler;
reg [8:0] r9_prescaler_count;
reg [9:0] r10_last_theta_rcv;

assign w9_prescaler = freq? 9'd489: 9'd408; /* 489 -> 49.92Hz 408 -> 59.83Hz*/

always @(posedge clk)begin
  if (rst) begin
    r9_prescaler_count <= 9'd0;
    theta_out <= 10'd0;
    r10_last_theta_rcv <= 10'd0;
  end
  else
    if (r10_last_theta_rcv != theta_in) begin
      r10_last_theta_rcv <= theta_in;
      theta_out <= theta_in;
      r9_prescaler_count <= 9'd0;
    end
    else
      if (r9_prescaler_count < w9_prescaler)
        r9_prescaler_count <= r9_prescaler_count+9'd1;
      else begin
        r9_prescaler_count <= 0;
        theta_out <= sequence_in? theta_out+10'd1: theta_out-10'd1;
      end
end

`ifndef VERILATOR
  // Dump waves
  // Gtkwave file
  initial begin
    $dumpfile("dump.vcd");
    $dumpvars(1, angle_venv);
  end
`endif

// Add assertion here
// psl default clock = (posedge clk);
// psl ERRORsum: assert never {sequence_in && CYCLE && theta_gen_aux=1023};
 // ERRORreadempty: assert never {empty && rd_en && rd_cs};
endmodule

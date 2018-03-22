/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Ultra(TM) in wire load mode
// Version   : K-2015.06-SP5-1
// Date      : Thu Mar 22 09:42:11 2018
/////////////////////////////////////////////////////////////


module fby2 ( clk, rst, q );
  input clk, rst;
  output q;
  wire   N4;

  CFD1QXL q_reg ( .D(N4), .CP(clk), .Q(q) );
  CNR2XL U4 ( .A(q), .B(rst), .Z(N4) );
endmodule


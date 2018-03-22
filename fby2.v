//*******************************************************//
//Project name:frequency divide by 2                     //
//Module name: fby2                                      //
//Design version: 1.0                                    //
//Tools used: Synopsys VCS
//Tools version:
//Desctiption:
//Developer name:
//Additional comments:
//******************************************************//

`timescale 1ns/10ps
module fby2(clk,rst, q);
input clk,rst;
output reg q;

always @(posedge (clk)) begin
if(rst)begin
q <=0;
$display("D-F/F output",q);
end else begin
q <=!q;
$display("D-F/F output",q);
end
end
endmodule

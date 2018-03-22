//***************Frequency divider by 2*****************//
//Project name:
//Module name:
//Design version:
//Tools used:
//Tools version:
//Desctiption:
//Developer name:
//Additional comments:
//******************************************************//

`timescale 1ns/10ps
module tb();
//declaring inputs and output
reg clk, rst;
wire q; 

//instantiating desing module
fby2 f(clk,rst,q);

//providing input stimulus
initial 
clk = 1;
always #5 clk = !clk;
initial begin
rst =1;   
#20 rst =0;

//end simulation at 200ns
#200 $finish; 
end 

//dump variables and generate vcd file to view waveforms
initial begin
$dumpfile("fby2.vcd");
$dumpvars(0,tb);
end



endmodule

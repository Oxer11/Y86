var Write_Memory=function()
{
	$("#MEM1").load("./js/ajax/Memory.txt #MEM1");
	$("#MEM2").load("./js/ajax/Memory.txt #MEM2");
	$("#MEM3").load("./js/ajax/Memory.txt #MEM3");
}

var Write_PipeRegister=function()
{
	$("#regFpredPC").load("./js/ajax/PipeRegister.txt #regFpredPC");
	$("#regDicode").load("./js/ajax/PipeRegister.txt #regDicode");
	$("#regDifun").load("./js/ajax/PipeRegister.txt #regDifun");
	$("#regDrA").load("./js/ajax/PipeRegister.txt #regDrA");
	$("#regDrB").load("./js/ajax/PipeRegister.txt #regDrB");
	$("#regDvalC").load("./js/ajax/PipeRegister.txt #regDvalC");
	$("#regDvalP").load("./js/ajax/PipeRegister.txt #regDvalP");
	$("#regEicode").load("./js/ajax/PipeRegister.txt #regEicode");
	$("#regEifun").load("./js/ajax/PipeRegister.txt #regEifun");
	$("#regEvalC").load("./js/ajax/PipeRegister.txt #regEvalC");
	$("#regEvalA").load("./js/ajax/PipeRegister.txt #regEvalA");
	$("#regEvalB").load("./js/ajax/PipeRegister.txt #regEvalB");
	$("#regEdstE").load("./js/ajax/PipeRegister.txt #regEdstE");
	$("#regEdstM").load("./js/ajax/PipeRegister.txt #regEdstM");
	$("#regEsrcA").load("./js/ajax/PipeRegister.txt #regEsrcA");
	$("#regEsrcB").load("./js/ajax/PipeRegister.txt #regEsrcB");
	$("#regMicode").load("./js/ajax/PipeRegister.txt #regMicode");
	$("#regMCnd").load("./js/ajax/PipeRegister.txt #regMCnd");
	$("#regMvalE").load("./js/ajax/PipeRegister.txt #regMvalE");
	$("#regMvalA").load("./js/ajax/PipeRegister.txt #regMvalA");
	$("#regMdstE").load("./js/ajax/PipeRegister.txt #regMdstE");
	$("#regMdstM").load("./js/ajax/PipeRegister.txt #regMdstM");
	$("#regWicode").load("./js/ajax/PipeRegister.txt #regWicode");
	$("#regWvalE").load("./js/ajax/PipeRegister.txt #regWvalE");
	$("#regWvalM").load("./js/ajax/PipeRegister.txt #regWvalM");
	$("#regWdstE").load("./js/ajax/PipeRegister.txt #regWdstE");
	$("#regWdstM").load("./js/ajax/PipeRegister.txt #regWdstM");
}

var Write_Register=function()
{
	$("#RAX").load("./js/ajax/Register.txt #RAX");
	$("#RBX").load("./js/ajax/Register.txt #RBX");
	$("#RCX").load("./js/ajax/Register.txt #RCX");
	$("#RDX").load("./js/ajax/Register.txt #RDX");
	$("#RSI").load("./js/ajax/Register.txt #RSI");
	$("#RDI").load("./js/ajax/Register.txt #RDI");
	$("#RBP").load("./js/ajax/Register.txt #RBP");
	$("#RSP").load("./js/ajax/Register.txt #RSP");
	$("#R8").load("./js/ajax/Register.txt #R8");
	$("#R9").load("./js/ajax/Register.txt #R9");
	$("#R10").load("./js/ajax/Register.txt #R10");
	$("#R11").load("./js/ajax/Register.txt #R11");
	$("#R12").load("./js/ajax/Register.txt #R12");
	$("#R13").load("./js/ajax/Register.txt #R13");
	$("#R14").load("./js/ajax/Register.txt #R14");
	$("#R15").load("./js/ajax/Register.txt #R15");
}

var Write_Code=function()
{
	$("#InsCode").load("./js/ajax/InsCode.txt #InsCode");
	$("#Assembly").load("./js/ajax/Assembly.txt #Assembly");
}

var Write_CC_Status_CPI=function()
{
	$("#ZF").load("./js/ajax/CC_Status_CPI.txt #ZF");
	$("#OF").load("./js/ajax/CC_Status_CPI.txt #OF");
	$("#SF").load("./js/ajax/CC_Status_CPI.txt #SF");
	$("#Stat").load("./js/ajax/CC_Status_CPI.txt #Stat");
	$("#CPI").load("./js/ajax/CC_Status_CPI.txt #CPI");
}

var Load=function()
{
	var DELAY=1;
	setInterval(Write_Code,DELAY);
	setInterval(Write_Memory,DELAY);
	setInterval(Write_Register,DELAY);
	setInterval(Write_CC_Status_CPI,DELAY);
	setInterval(Write_PipeRegister,DELAY);
}

$(document).ready(Load);


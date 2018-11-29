var Write_Stack=function()
{
    $("#Stack").load("./js/ajax/Stack.txt");
}

var Write_PipeRegister=function()
{
    $("#Stage").load("./js/ajax/Stage.txt");
}

var Write_Register=function()
{
    $("#tab_content3").load("./js/ajax/tab_content3.txt");
}

var Write_Code=function()
{
	$("#Codes").load("./js/ajax/Codes.txt ");
}

var Write_CC_Status_CPI=function()
{
    $("#tab_content1").load("./js/ajax/tab_content1.txt");
}

var Write_Display=function()
{
    $("#columns").load("./js/ajax/columns.txt");
}

var Load=function()
{
	var DELAY=1;
	setInterval(Write_Code,DELAY);
	setInterval(Write_Register,DELAY);
	setInterval(Write_CC_Status_CPI,DELAY);
	setInterval(Write_PipeRegister,DELAY);
	setInterval(Write_Display,DELAY);
	setInterval(Write_Stack,DELAY);
}

$(document).ready(Load);


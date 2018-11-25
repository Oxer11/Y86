var Write_Memory=function()
{
    $("#tab_content2").load("./js/ajax/tab_content2.txt");
}

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
	$("#InsCode").load("./js/ajax/InsCode.txt ");
	$("#Assembly").load("./js/ajax/Assembly.txt");
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
	setInterval(Write_Memory,DELAY);
	setInterval(Write_Register,DELAY);
	setInterval(Write_CC_Status_CPI,DELAY);
	setInterval(Write_PipeRegister,DELAY);
}

$(document).ready(Load);


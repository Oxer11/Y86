// https://zeit.co/blog/async-and-await
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}
   
$.ajaxSetup({ 
    async : false 
});    
var cmd_id=0;
$(document).ready(function(){
 		$("#btn_input").click(function(){
			$("#number_div").css("border-right-color","green");
  			var content=$("#input_code").val();                
  			$.post("/IDE/",{'type':'code', 'content':content},     
    			function(data,status){              
         			$("#yo_Code").html(data.Code);
					yo=$("#yo_Code").html();
					$("#error").html(data.error);
         			$("#Codes").html(data.Codes);
         			$("#tab_content1").html(data.Stat);
         			$("#Stage").html(data.Stage);
         			$("#columns").html(data.Display);
         			$("#Stack").html(data.Stack);
         			$("#tab_content3").html(data.Register);
         			$("#cmd_output").html("");
					$("#Cache").html(data.Cache);
					
					if(data.error.match("Fail")=="Fail"){
						$(".error_info").css("bottom","0px");
						$("#error_arrow").css("transform","rotate(180deg)");
					}
					else{
						$(".error_info").css("bottom","-260px");
						$("#error_arrow").css("transform","rotate(0deg)");
					}
  				});
			
			$(".code").scrollTop(0);
		});
	});
	$(document).on("dblclick", ".error_line",function(){
			var line=this.innerHTML;
			var id1=line.indexOf("line");
			var id2=line.indexOf("</td>");
			var i=parseInt(line.substring(id1+5,id2));
			var s=yo.split('\n');
			s[i-1]="<mark>"+s[i-1]+"</mark>";
			$("#yo_Code").html(s.join('\n'));
			if(i>8&&i<s.length)
				$("#yo").scrollTop((i-8)*20);
			else
				$("#yo").scrollTop(0);
	});
	$(document).ready(function()
	{
 		$("#cmd_input").on("keyup",function(e)
 		{
 			var eCode = e.keyCode ? e.keyCode : e.which ? e.which : e.charCode;
 			if (eCode==13)
 			{
  				var content=$("#cmd").val(); 
	  			var cmd=content.split(" ");
	  			cmd_id++;
  				function B()
  				{  
  					var end=1, THREAD='';
  					$.post("/IDE/",{'type':'command', 'content':content, 'cmdid':cmd_id},     
    					function(data,status)
    					{              
    	     				$("#yo_Code").html(data.Code);
    	     				$("#Codes").html(data.Codes);
    	     				$("#tab_content1").html(data.Stat);
 		        			$("#Stage").html(data.Stage);
    		     			$("#columns").html(data.Display);
    		     			$("#Stack").html(data.Stack);
    		     			$("#tab_content3").html(data.Register);
    		     			$("#cmd_output").html(data.CMD);
							$("#Cache").html(data.Cache);
		
							$(".cmd").scrollTop(99999);
							var ls=data.Codes.split('\n');
							var i=0;
							for(i=0;i!=ls.length;i++)
								if(ls[i][1]=='m')
									break;
							if(i>8&&i<ls.length)
								$(".code").scrollTop((i-8)*20);
							else
								$(".code").scrollTop(0);
								
							THREAD = data.THREAD;
							end = data.end;
  						});
  					$("#cmd").val("");  
  					var FF=0,DD=0,EE=0,MM=0,WW=0;
  					function A(i)
  					{
  						if (THREAD[i] == 'F')
						{
							if (FF%2 == 0) $("#Fetch").css("background-color","rgb(216,191,216)");
							else $("#Fetch").css("background-color","white");
							FF++;
						}
						if (THREAD[i] == 'D')
						{
							if (DD%2 == 0) $("#Decode").css("background-color","rgb(216,191,216)");
							else $("#Decode").css("background-color","white");
							DD++;
						}
						if (THREAD[i] == 'E')
						{
							if (EE%2 == 0) $("#Execute").css("background-color","rgb(216,191,216)");
							else $("#Execute").css("background-color","white");
							EE++;
						}
						if (THREAD[i] == 'M')
						{
							if (MM%2 == 0) $("#Memory").css("background-color","rgb(216,191,216)");
							else $("#Memory").css("background-color","white");
							MM++;
						}
						if (THREAD[i] == 'W')
						{
							if (WW%2 == 0) $("#Write").css("background-color","rgb(216,191,216)");
							else $("#Write").css("background-color","white");
							WW++;
						}
						if (i<THREAD.length-1) sleep(200).then(() => { A(i+1); })
					}
					A(0);
  					if (end == 0)
  						sleep(2100).then(() => { B(); })
  				}
  				B();
  			}
		});
	});
	$(document).ready(function(){
	$("#input_code").focus(function(){
	  $("#input_code").keyup(function(){
		  $("#number_div").css("border-right-color","yellow");
		  var lines=$("#input_code").val();
		  var array=lines.split("\n");
		  var s="";
		  for(var i=1;i!=array.length+1;i++){
			s=s+i.toString()+"<br>";
		  }
		  document.getElementById("number").innerHTML=s;
			});
		});
	});
	$(document).ready(function(){
		$("#input_code").scroll(function(){
			var h=$("#input_code").scrollTop();
			$("#number_div").css("top","-"+h.toString()+"px");
			//alert(h.toString()+' '+hei.toString());
		});
	});

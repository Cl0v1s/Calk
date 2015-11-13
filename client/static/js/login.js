//require md5.js

$(document).ready(function()
{
	$("#password").keydown(function(ev)
	{
		sendCredentials(ev);
	});
});

function sendCredentials(event)
{
	console.log(event.keyCode);
	if(event.keyCode == 13 || event.keyCode == 9)
		return;
	var user = $("#user").val();
	var password = hex_md5($("#password").val());
	$("#user_final").val(user);
	$("#password_final").val(password);
	console.log($("#password_final").val());


}
//Gestion des boutons formulaires
$(document).ready(function(){
	setButtons();
});

function setButtons()
{
	$(".button").click(function()
	{
		if($(this).data("link") == undefined)
			return;
		var link = $(this).data("link");
		$.post(link, $(this).data(),function(dat)
		{
			if(dat.state == "success")
				notify("Opération terminée.");
			else
				notify(dat.sate);
		});
	});
}

//Gestion des entrées de données annimées
$(document).ready(function()
{
	setInputs();
});

function setInputs()
{
	//Ajout de l'apparition du bouton d'envoie l'information
	$(".input").click(function()
	{

		//TODO: adapter le code suivant pour prendre en charge les images


		//Ajout du bouton envoyer
		if($(this).parent().find(".input-submit").length == 0)
		{
			var node = $("<a href='#' class='button input-submit'>Envoyer</a>");
			if($(this).hasClass("input-dark"))
				node.addClass("button-dark");
			$(this).parent().append(node);
			$(node).animate({width: "100px", opacity: "1"}, 400, "swing");
			//Ajout de la suppression du bouton envoyer
			$(this).focusout(function()
			{
					$(node).animate({opacity: "0"}, 400, "swing", function(){$(this).remove();});
			});
		}
		else
			return;

		//Ajout de l'action lors du l'appui sur le bouton envoyer
		$(node).click(function()
		{
			var bro = $(this).parent().find(".input");
			var link = $(bro).data("link");
			var variable = $(bro).attr("name");
			var data = $(bro).val();
			$.post(link, {valueName: variable, value:data}, function(dat)
			{
				if(dat.state == "success")
				{
					notify("Modifications enregistrées.");
				}
				else
					notify(dat.state);
			}).fail(function(dat){console.log(dat);});
				$(node).animate({width: "0px", opacity: "0"}, 400, "swing", function(){$(this).remove();});
		});
	});
}


//Permet de suivre un utilisateur
function follow(id)
{
		$.post("/follow/execute", {"follow": "yes", "id": id},function(data)
		{
				if(data.state=="success")
						notify("Vous suivez désormais " + data.follow +".");
				else
						notify("Une erreur est survenue.");
		} );
}

//Permet de ne plus suivre un utilisateur
function unFollow(id)
{
		$.post("/follow/execute", {"unfollow": "yes", "id": id},function(data)
		{
				if(data.state=="success")
						notify("Vous ne suivez plus " + data.unfollow +".");
				else
						notify("Une erreur est survenue.");
		} );
}

function checkForFollow()
{
	//intialise les boutons de follow et d'un follow
	follows = $(document).find(".follow");
	for(i=0; i<follows.length;i++)
	{
		var id = $(follows[i]).data("id");
		var input = $(follows[i]);
		$.getJSON("/user/json/" + id, function(data) {
			if(data.followed == false)
			{
				input.html("Suivre");
				input.click(function(){
					follow(id);
					checkForFollow();
				});
			}
			else if(data.followed != "None")
			{
				input.html("Ne plus suivre");
				input.click(function(){
					unFollow(id);
					checkForFollow();
				});
			}
			else
			{
				input.css("display","none");
			}
		});
	}
}


$(document).ready(function() {

	checkForFollow();


	//Initialise tooltipster pour les informations sur les utilisateur (.user_info)
	$(".user_info").tooltipster({
		content: "Chargement...",
		animation: "fall",
		interactive: true,
		contentAsHTML: true,
		functionBefore: function(origin, continueToolTip)
		{
			continueToolTip();
			if ($(origin).data("cached") != "true")
			{
				$.getJSON("/user/json/" + $(origin).data("id"), function(data)
				{
					var content = "<img style='float: left;width: 25px; height: 25px;' src='" + data.picture + "'><span style='margin-left: 20px;vertical-align: middle;height: 25px; float: left;line-height: 25px;'>" + data.firstName + " " +data.lastName+"</span><br><br>";
					if (data.followed == false)
					{
							var buttonId = "follow-" + $(origin).data("id");
							content = content + "<a id='" + buttonId + "' href='#' class='button follow'>Suivre</a>";
							buttonId = "#"+buttonId;
					}
					else if(data.followed != 'None')
					{
							var buttonId = "follow-" + $(origin).data("id");
							content = content + "<a id='" + buttonId + "' href='#' class='button unfollow'>Ne plus suivre</a>";
							buttonId = "#"+buttonId;
					}
					origin.tooltipster('content', content);
					if(data.followed == false)
					{
							$(buttonId).click(function()
							{
									follow($(origin).data("id"));
							});
					}
					else if (data.followed != 'None')
					{
							$(buttonId).click(function()
							{
									unFollow($(origin).data("id"));
							});
					}
				});
			}
		}
	});
});

// Gestion des notifications
function notify(message) {
	// Voyons si le navigateur supporte les notifications
	if (!("Notification" in window)) {
		return;
	}

	// Voyons si l'utilisateur est OK pour recevoir des notifications
	if (Notification.permission === "granted") {
		// Si c'est ok, créons une notification
		var notification = new Notification(message);
	}

	// Sinon, nous avons besoin de la permission de l'utilisateur
	// Note : Chrome n'implémente pas la propriété statique permission
	// Donc, nous devons vérifier s'il n'y a pas 'denied' à la place de 'default'
	else if (Notification.permission !== 'denied') {
		Notification.requestPermission(function (permission) {

			// Quelque soit la réponse de l'utilisateur, nous nous assurons de stocker cette information
			if(!('permission' in Notification)) {
				Notification.permission = permission;
			}

			// Si l'utilisateur est OK, on crée une notification
			if (permission === "granted") {
				var notification = new Notification(message);
			}
		});
	}

	// Comme ça, si l'utlisateur a refusé toute notification, et que vous respectez ce choix,
	// il n'y a pas besoin de l'ennuyer à nouveau.
}

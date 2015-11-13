$(document).ready(function()
{
    setLayersList();
    removeOnDeleteLayer();
    allowPasswordChange();
});

//bouton déroulant pour liste de calques
function setLayersList()
{
    $(".layer_item").css("display", "none");
    $(".layer_item").css("opacity", "0");
    $("#user_layers_title").click(function()
    {
        if($(this).data("opened") == undefined || $(this).data("opened") == "false")
        {
            $(".layer_item").css("display", "inline-block");
            $(".layer_item").animate({"opacity":"1"}, 400, "swing");
            $(this).data("opened", "true");
        }
        else
        {
            var t = $(this);
            $(".layer_item").animate({"opacity":"0"}, 400, "swing", function()
                {
                    $(".layer_item").css("display", "none");
                    $(t).data("opened", "false");

                });

        }
    });
}

//lors de l'appui sur le bouton de suppression de calque, effacer l'entrée séléctionnée
function removeOnDeleteLayer()
{
    $(".button").click(function()
    {
        if($(this).data("link") == "/layers/execute" && $(this).data("delete") == "yes")
        {
            $(this).animate({"opacity":"0"}, 400, "swing", function()
                {
                    $(this).parent().css("display", "none");
                });
        }
    });
}

function allowPasswordChange()
{
    var sender = $("#user_password_send");
    sender.unbind("click");

    $("#user_password_title").click(function()
    {
        if($(this).data("opened") == "false" ||$(this).data("opened") == undefined)
        {
            $(this).parent().find("form").css("display", "inline-block");
            $(this).parent().find("form").animate({"opacity":"1"}, 400, "swing");
            $(this).data("opened", "true");
        }
        else
        {
             var t = $(this);
            $(this).parent().find("form").animate({"opacity":"0"}, 400, "swing", function()
                {
                    $(this).parent().find("form").css("display", "none");
                    $(t).data("opened", "false");

                });

        }
    });


    $("#user_password_old").keydown(function(event)
    {
        if(event.keyCode == 13 || event.keyCode == 9)
            return;
        var en = hex_md5($(this).val());
        sender.data("old", en);
    });

    $("#user_password_new").keydown(function(event)
    {
        if(event.keyCode == 13 || event.keyCode == 9)
            return;
        var en = hex_md5($(this).val());
        sender.data("password", en);
    });

    $("#user_password_verif").keydown(function(event)
    {
        if(event.keyCode == 13 || event.keyCode == 9)
            return;
        var en = hex_md5($(this).val());
        sender.data("verif", en);
    });

    sender.click(function()
    {
        if($("#user_password_old").val().length <= 0)
        {
            notify("Vous devez entrer votre mot de passe actuel avant de pouvoir continuer.");
            return;
        }

        if($("#user_password_new").val().length < 8)
        {
            notify("Vous devez choisir un nouveau mot de passe d'au moins 8 caractères pour remplacer l'ancien.");
            return;
        }


        if($("#user_password_verif").val().length <= 0)
        {
            notify("Vous devez entrer à nouveau votre futur mot de passe afin d'éviter toute erreur.");
            return;
        }

        if($(this).data("password") != $(this).data("verif"))
        {
            notify("Le nouveau de passe choisi et sa vérification ne correspondent pas.");
            return;
        }

        $.post("/users/execute", {valueName : "password", value : $(this).data("password"), old : $(this).data("old"), username: $(this).data("username")}, function(dat)
        {
            if(dat.state == "success")
                notify("Votre mot de passe a bien été mis à jour.");
            else
                notify(dat.state);
        });



    });

}

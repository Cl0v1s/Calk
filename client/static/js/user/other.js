$(document).ready(function()
{
    setLayersList();
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

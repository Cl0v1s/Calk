$(document).ready(function()
{
    $("#layerToPDF").click(createPDF);
});

//Génère un pdf à partir du calque de la page courante
function createPDF()
{
    var id = $("#layerToPDF").data("layer-id");
    $.get("/layer/generate/"+id,{}, function(dat){
        if(dat.state == "success")
        {
            window.open(dat.link,"_blank");
            notify("Le calque a bien été transposé au format PDF.");
        }
        else
        {
            notify(dat.success);
        }
    });
}



$(document).ready(function() {
    $("#layer_create_editor").editable({
        inlineMode: false,
        buttons: ["bold", "italic", "underline", "strikeThrough", "subscript", "superscript", "fontFamily", "fontSize", "color", "formatBlock", "blockStyle", "inlineStyle", "align", "insertOrderedList", "insertUnorderedList", "outdent", "indent", "selectAll", "createLink", "insertImage", "table", "undo", "redo", "fullscreen"],
        maxHeight: 500,
    });

    $("#layer_create_save").unbind("click");


    $("#layer_create_save").click(function()
    {
        data = {
            save: "yes",
            basedOn: $(this).data("based-on"),
            chapter: $(this).data("chapter"),
            content: $("#layer_create_editor").editable("getHTML", false, false)
        };

        $.post("/layers/execute", data, function(dat)
        {
            if (dat.state == "success")
            {
                notify("Votre calque a bien été enregistré.");
                window.location.replace("/index");
            }
            else
                notify(dat.state);
        });
    });

});

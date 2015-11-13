<!DOCTYPE html>
<html>
    <head>
        <title>Connexion</title>
        <meta charset="utf-8">
        <script type="text/javascript" src="/static/js/jquery.js"></script>
        <script type="text/javascript" src="/static/js/md5.js"></script>
        <script type="text/javascript">
            $(document).ready(function()
            {
               $("#fake").keydown(function(event)
                {
                   if(event.keyCode != 13)
                   {
                    var h = hex_md5($("#fake").val());
                    $("#password").val(h);
                   }
                   console.log($("#password").val());
                });
            });
        </script>
    </head>
    <body>
        <h1>Connexion</h1>
        <div>
            <form action="/auth" method="post">
                Nom d'utilisateur: <input name="user"><br>
                Mot de passe: <input id="fake" type="password" name="password_fake"><br>
                <input type="hidden" id="password" name="password">
                <input type="submit" value="Envoyer">
            </form>
            <span>Notre service utilise les cookies pour fonctionner, veuillez les autoriser pour être en mesure de vous authentifier.</span>
        </div>
    </body>
</html>
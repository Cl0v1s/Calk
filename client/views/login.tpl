<!DOCTYPE html>
<html>
    <head>
        <title>Connexion</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="/static/css/login.css">
        <script type="text/javascript" src="/static/js/jquery.js"></script>
        <script type="text/javascript" src="/static/js/md5.js"></script>
                <script type="text/javascript" src="/static/js/login.js"></script>
    </head>
    <body>
        <div id="login_content">
            <span id="login_title"><h1>Calk</h1></span>
            <span id="login_page"><h2>Connexion</h2></span><br><br>
            <div>
                Nom d'utilisateur:<br><input id="user"><br>
                Mot de passe:<br><input id="password" type="password"><br>
                <form id="form" action="/auth" method="post">
                    <input id="user_final" name="user" style="display:none;">
                    <input id="password_final" name="password" style="display:none;">
                    <input class="button button-dark" type="submit" value="Envoyer">
                </form>
            </div>
            <span id="warning">Notre service utilise les cookies pour fonctionner, veuillez les autoriser pour être en mesure de vous authentifier.</span>
        </div>
    </body>
</html>

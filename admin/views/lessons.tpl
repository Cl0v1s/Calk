<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Cours</title>
    </head>
    <body>
        <h1>Cours</h1>
        <nav>
            <a href="/index">Retour au menu</a>
            <a href="/disconnect">Se déconnecter</a>
        </nav><br><br>
        <div>
            <table>
                <tr>
                    <td>Intitulé du cours</td>
                    <td>Enseignant</td>
                    <td>Supprimer ?</td>
                    <td></td>
                </tr>
                % for lesson in lessons:
                    <tr>
                        <form action="/lessons/execute" method="post">
                            <input type="hidden" name="id" value="{{lesson[0]}}">
                            <td>{{lesson[1]}}</td>
                            <td>{{lesson[2]}}</td>
                            <td><input type="checkbox" name="delete" value="yes"></td>
                            <td><input type="submit" value="Envoyer"></td>
                        </form>
                    </tr>
                % end
                <tr>
                    <td>Ajouter</td>
                </tr>
                <tr>
                    <form action="/lessons/execute" method="post">
                        <input type="hidden" name="add" value="yes">
                        <td><input name="name"></td>
                        <td><input name="teatcher"></td>
                        <td></td>
                        <td><input type="submit" value="envoyer"></td>
                    </form>
                </tr>
            </table>
        </div>
    </body>
</html>
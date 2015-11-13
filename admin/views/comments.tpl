<!DOCTYPE html>
<html>
    <head>
        <title>Commentaires</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Commentaires</h1>
        <nav>
            <a href="/index">Retour au menu</a>
            <a href="/disconnect">Se déconnecter</a>
        </nav><br><br>
        <a href="/index">Retour au menu</a><br><br>
        <div>
            <table>
                <tr>
                    <td>Calque</td>
                    <td>Chapitre</td>
                    <td>Utilisateur</td>
                    <td>Date</td>
                    <td>Contenu</td>
                    <td>Action</td>
                </tr>
                % for comment in comments:
                <tr>
                    <td>
                        <a href="/layers/{{comment[1]}}">#{{comment[1]}}</a>
                    </td>
                    <td>
                        {{comment[2]}}
                    </td>
                    <td>
                        <a href="/user/{{comment[3]}}">{{comment[3]}}</a>
                    </td>
                    <td>
                        {{comment[4]}}
                    </td>
                    <td>
                        {{comment[5]}}
                    </td>
                    <td>
                        <form action="/comments/execute" method="post">
                            <input type="hidden" name="id" value="{{comment[0]}}">
                            <input type="hidden" name="layer" value="{{comment[1]}}">
                            <input type="hidden" name="delete" value="yes">
                            <input type="submit" value="Supprimer">
                        </form>
                    
                    </td>
                
                </tr>
                % end
            </table>
        </div>
    </body>
</html>
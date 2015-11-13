<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Chapitres</title>
    </head>
    <body>
        <h1>Chapitres</h1>
        <nav>
            <a href="/index">Retour au menu</a>
            <a href="/disconnect">Se déconnecter</a>
        </nav><br><br>
        <div>
            <table>
                <tr>
                    <td>Intitulé du chapitre</td>
                    <td>Cours associé</td>
                    <td>Supprimer ?</td>
                </tr>
                % for chapter in chapters:
                    <tr>
                        <form action="/chapters/execute" method="post">
                        <input type="hidden" name="id" value="{{chapter[0]}}">
                        <td>{{chapter[2]}}</td>
                        <td>{{getLessonInformations(chapter[1])[1]}} avec {{getLessonInformations(chapter[1])[2]}} </td>
                        <td><input type="checkbox" value="yes" name="delete"></td>
                        <td><input type="submit" value="Envoyer"></td>
                        </form>
                    </tr>
                % end 
                    <tr>
                        <form action="/chapters/execute" method="post">
                            <input type="hidden" value="yes" name="add">
                            <td>
                                <input name="name">
                            </td>
                            <td>
                                <select name="lesson">
                                    % for lesson in lessons:
                                        <option>{{lesson[0]}}.  {{lesson[1]}} avec {{lesson[2]}}</option>
                                    % end 
                                </select>
                            </td>
                            <td></td>
                            <td><input type="submit" value="Envoyer"></td>
                        </form>
                    </tr>
            </table>
        </div>
    </body>
</html>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Calques</title>
    </head>
    <body>
        <h1>Calques</h1>
        <nav>
            <a href="/index">Retour au menu</a>
            <a href="/disconnect">Se déconnecter</a>
        </nav><br><br>
        <div>
            <span>afficher: <a href="/layers/mod">Les calques à modérer</a> <a href="/layers/ok">Les calques validés</a> <a href="/layers/all">Tout les calquess</a></span>
            % if len(layers) > 0:
                <table>
                    <tr>
                        <td>Utilisateur</td>
                        <td>Chapitre</td>
                        <td>Date</td>
                        <td>Contenu</td>
                        <td>Commentaires</td>
                        <td>Validation</td>
                        <td>Supprimer</td>
                    </tr>
                % for layer in layers:
                    <tr>
                        <td><a href="/user/{{layer[1]}}">{{layer[1]}}</a></td>
                        <td>{{layer[2]}}</td>
                        <td>{{layer[3]}}</td>
                        <td><textarea>{{layer[4]}}</textarea></td>
                        <td><a href="/comments/{{layer[0]}}">Voir les commentaires</a></td>
                        <td>
                            % if layer[4] != 'True':
                                <form action="/layers/execute" method="post">
                                    <input type="hidden" name="validate" value="yes">
                                    <input type="hidden" name="id" value="{{layer[0]}}">
                                    <input type="submit" value="valider">
                                </form>
                            % else:
                                Validé
                            % end
                        </td>
                        <td>
                            <form action="/layers/execute" method="post">
                                <input type="hidden" name="delete" value="yes">
                                <input type="hidden" name="id" value="{{layer[0]}}">
                                <input type="submit" value="supprimer">
                            </form>
                        </td>
                    </tr>            
                % end 
                </table>
            % else:
                <br><span>Aucun calque n'est séléctionné</span>
            % end 
        </div>
    </body>
</html>

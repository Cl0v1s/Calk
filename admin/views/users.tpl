<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Utilisateurs</title>
    </head>
    <body>
        <h1>Utilisateurs</h1>
        <nav>
            <a href="/index">Retour au menu</a>
            <a href="/disconnect">Se déconnecter</a>
        </nav><br><br>
        <div>
            <table>
                <tr>
                    <td>Nom</td>
                    <td>Email</td>
                    <td>Nom</td>
                    <td>Prénom</td>
                    <td>Banni</td>
                    <td>Admin</td>
                    <td>Supprimer ?</td>
                    <td></td>
                </tr>
                
                
            % for user in users:
                <tr>
                    <form action="/users/execute" method="post">
                        <input type="hidden" value="{{user[0]}}" name="id">
                        <td>
                            {{user[1]}}
                        </td>
                        <td>
                            {{user[3]}}
                        </td>
                        <td>
                            {{user[6]}}
                        </td>
                        <td>
                            {{user[5]}}
                        </td>
                        <td>
                            % if user[4]=="True":
                                <input type="checkbox" value="yes" name="banned" checked>
                            % end
                            % if user[4] !="True":
                                <input type="checkbox" value="yes" name="banned">
                            % end
                        </td>
                        <td>
                            % if user[7]=="True":
                                <input type="checkbox" value="yes" name="admin" checked>
                            % else:
                                <input type="checkbox" value="yes" name="admin">
                            % end                            
                        </td>
                        <td>
                            <input type="checkbox" value="yes" name="delete">
                        </td>
                        <td>
                            <input type="submit" value="envoyer">
                        </td>
                    </form>
                </tr>
            % end
            </table>
        </div>
    </body>
</html>
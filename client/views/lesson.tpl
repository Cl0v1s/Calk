<!DOCTYPE html>
<html>
    <head>
        <title>Chapitres</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="/static/css/global.css">
    </head>
    <body>
        <nav>
            <span id="nav_title" class="nav_item">Calk</span>
            <span id="nav_page" class="nav_item">Chapitres</span>
            <span id="nav_links" class="nav_item"><a href="/index"><img id="nav_home" src="/static/img/home.svg"></a></span>
        </nav>
        <div class="first_content_under">
        </div>
            <div class="first_content">
                <div class="panel">
                    <span>Sélectionnez un chapitre pour en voir les calques.</span>
                    <div id="chapter_list">
                        % if len(chapters) > 0:
                            % for chapter in chapters:
                                <div class="chapter_item"><span>#{{chapter[0]}}</span> <span>{{chapter[2]}}</span> <span><a href="/chapter/{{chapter[0]}}">Voir les calques</a></span></div>
                            % end
                        % else:
                            <span class="empty">Aucun chapitre n'est disponible.</span>
                        % end
                    </div>

                </div>
            </div>
    </body>
</html>

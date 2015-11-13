<!DOCTYPE html>
<html>
    <head>
        <title>Cours</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="/static/css/global.css">
    </head>
    <body>
        <nav>
            <span id="nav_title" class="nav_item">Calk</span>
            <span id="nav_page" class="nav_item">Cours</span>
            <span id="nav_links" class="nav_item"><a href="/index"><img id="nav_home" src="/static/img/home.svg"></a></span>
        </nav>
		<div class="first_content_under">
		</div>
			<div class="first_content">
				<div class="panel">
					<span>Sélectionnez un cours pour en voir la liste des chapitres.</span>
                    <div id="lesson_list">
    					% if len(lessons) >= 0:
    						% for lesson in lessons:
    					<div class="lesson_item"><span>#{{lesson[0]}}</span> <span>{{lesson[1]}}</span> avec <span>{{lesson[2]}}</span> <span><a href="/lesson/{{lesson[0]}}">Voir les chapitres</a></span></div>
    						% end 
    					% else:
    						<span class="empty">Aucun cours n'est disponible.</span>
    					% end 
                    </div>
				</div>
			</div>
    </body>
</html>

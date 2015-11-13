<!DOCTYPE html>
<html>
	<head>
		<title>Calque</title>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="/static/css/global.css" />

		<!--jquery-->
		<script type="text/javascript" src="/static/js/jquery.js"></script>

		<!--tooltipster-->
		<link rel="stylesheet" href="/static/css/tooltipster.css" />
		<script type="text/javascript" src="/static/js/tooltipster.js"></script>

		<!--jsPDF-->
		<script type="text/javascript" src="/static/js/jspdf/jspdf.js"></script>
		<script type="text/javascript" src="/static/js/jspdf/jspdf.plugin.standard_fonts_metrics.js"></script>
		<script type="text/javascript" src="/static/js/jspdf/jspdf.plugin.split_text_to_size.js"></script>
		<script type="text/javascript" src="/static/js/jspdf/jspdf.plugin.from_html.js"></script>


		<script type="text/javascript" src="/static/js/global.js" /></script>
		<script type="text/javascript" src="/static/js/layer/base.js"></script>


	</head>
	<body>
		<nav>
			<span id="nav_title" class="nav_item">Calk</span>
			<span id="nav_page" class="nav_item">{{layer[4]}}</span>
			<span id="nav_links" class="nav_item"><a href="/index"><img id="nav_home" src="/static/img/home.svg"></a></span>
		</nav>
		<div class="first_content_under">
		</div>
			<div class="first_content">
				<div class="panel">
					<div id="layer_content">
						<div>
							<!--bouton exporter pdf-->
							<a href="#" class="button" id="layerToPDF" data-layer-id="{{layer[0]}}">Obtenir un <br>PDF</a>
							<!--informations sur le calque-->
							<div id="layer_info">
								Calque #{{layer[0]}},
								% if layer[7] != 'None':
									basé sur le calque <a href="/layer/{{layer[7]}}">#{{layer[7]}}</a>
								% else:
									calque original
								% end
									<br>
									par <a class="user_info" data-id="{{layer[8]}}" href="/user/{{layer[8]}}">{{layer[2]}}</a>
							</div>
							<!--bouton créer un calque-->
							<a href="/layer/create?basedOn={{layer[0]}}" class="button" id="layer_create">Superposer un calque</a>
							<div id="layer_html">
								{{! layer_content}}
							</div>
						</div>
						% if logged==True:
						<br><hr><br>
						<h2>Envoyer un commentaire:</h2>
							<div id="layer_comment_form"><!-- TODO insérer un portrait de l'utilisateur courant-->
								<form action="/comments/execute" method="post">
									<input type="hidden" name="send" value="yes">
									<input type="hidden" name="layer" value="{{layer[0]}}">
									<input name="content">
									<input type="submit" value="envoyer">
								</form>
							</div>
						% end
						<br><hr><br>
						<div id="layer_comments">
							<h2>Voir les commentaires:</h2>
							% if len(comments) == 0:
								<span>Aucun commentaire.</span>
							% end
							% for comment in comments:
								<div class="layer_comment"> <!-- TODO: ajouter aperçu de l'user -->
									<div class="layer_comment_info">
										<span>
											<a class="user_info" data-id="{{comment[1]}}" href="/user/{{comment[1]}}">
											<img class="user_picture" src="{{comment[5]}}">{{comment[2]}}</a>
										</span>
										<span>
											{{comment[3]}}
										</span>
									</div><br>
									<hr>
									<div class="layer_comment_content">
										{{comment[4]}}
									</div>
								</div>
							% end
						</div>
				</div>
			</div>
		</div>
	</body>
</html>

<!DOCTYPE html>
<html>
<head>
	<title>{{chapter[2]}}</title>
	<meta charset="utf-8">

	<link rel="stylesheet" href="/static/css/global.css">

	<!--froala style-->
	<link href="/static/css/font-awesome.min.css" rel="stylesheet" type="text/css">
	<link href="/static/css/froala_editor.min.css" rel="stylesheet" type="text/css">
	<link href="/static/css/froala_style.min.css" rel="stylesheet" type="text/css">

	<!--pwstabs style-->
	<link rel="stylesheet" href="/static/css/pwstabs.css">

	<script type="text/javascript" src="/static/js/jquery.js"></script>
	<script type="text/javascript" src="/static/js/pwstabs.js"></script>

	<!--tooltipster-->
	<link rel="stylesheet" href="/static/css/tooltipster.css">
	<script type="text/javascript" src="/static/js/tooltipster.js"></script>

	<script type="text/javascript" src="/static/js/global.js"></script>

	<!--pwstabs start-->
	<script type="text/javascript">
			$(document).ready(function($){
				 $('.pwstabs').pwstabs({

					// scale / slideleft / slideright / slidetop / slidedown / none
					effect: 'scale',
					defaultTab: 1,

				});
			});
	</script>

</head>
<body>
	<nav>
		<span id="nav_title" class="nav_item">Calk</span>
		<span id="nav_page" class="nav_item">{{chapter[2]}}</span>
		<span id="nav_links" class="nav_item"><a href="/index"><img id="nav_home" src="/static/img/home.svg"></a></span>
	</nav>
	<div class="first_content_under">
	</div>
	<div class="first_content">
		<div class="panel">

		<!--bouton créer un calque-->
		<a href="/layer/create?chapter={{chapter[0]}}" class="button" id="chapter_layer_create">Créer un calque</a>


		<!--bouton série de calques suivant-->
		% next = setdefault(next, index+6)
		% if end < len(layers):
				<a class="chapter_arrow_enabled" href="/chapter/{{chapter[0]}}?index={{next}}" style="font-size:50px;">
		% else:
				<a class="chapter_arrow_disabled">
		% end
					<div id="chapter_next"></div>
				</a>

		<!--bouon série de calques précédents-->
		% prev = setdefault(next, index-6)
		% if index > 0:
				<a class="chapter_arrow_enabled" href="/chapter/{{chapter[0]}}?index={{prev}}" style="font-size:50px;">
		% else:
				<a class="chapter_arrow_disabled">
		% end
					<div id="chapter_previous"></div>
				</a>

			<div class="pwstabs">

				% for i in range(index,end-1):
					% if i<len(layers):

						% if layers[i][3] == 'False':
							<div data-pws-tab="tab_{{i}}" data-pws-tab-name="#{{layers[i][0]}}">
								<div class="chapter_layer_info">
									Calque #{{layers[i][0]}},

									% if layers[i][4] != 'None':
										basé sur le calque <a href="/layer/{{layers[i][4]}}">#{{layers[i][4]}}</a>
									% else:
										calque original
									% end

									<br>
									par <a class="user_info" href="/user/{{layers[i][5]}}">{{layers[i][1]}}</a>
									<br>
									<a href="/layer/{{layers[i][0]}}">Lire la suite</a>
								</div>
								{{! layers_content[i]}}
							</div>
						% else:
							<div data-pws-tab="tab_{{i}}" data-pws-tab-name="Mis en avant">
								<div class="chapter_layer_info">
									Calque #{{layers[i][0]}},

									% if layers[i][4] != 'None':
										basé sur le calque <a href="/layer/{{layers[i][4]}}">#{{layers[i][4]}}</a>
									% else:
										calque original
									% end

									<br>
									par <a class="user_info" data-id="{{layers[i][5]}}" href="/user/{{layers[i][5]}}">{{layers[i][1]}}</a>
									<br>
									<a href="/layer/{{layers[i][0]}}">Lire la suite</a>
								</div>
								{{! layers_content[i]}}
							</div>
						% end
					% end
				% end

			</div>
		</div>

	</div>
</body>
</html>

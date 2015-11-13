<!DOCTYPE html>
<html>
    <head>
        <title>{{user[3]}} {{user[4]}}</title>
        <meta charset="utf-8">
		<link rel="stylesheet" href="/static/css/global.css">

		<!--jquery-->
		<script type="text/javascript" src="/static/js/jquery.js"></script>

		<!--tooltipster-->
		<link rel="stylesheet" href="/static/css/tooltipster.css">
		<script type="text/javascript" src="/static/js/tooltipster.js"></script>

		<script type="text/javascript" src="/static/js/global.js"></script>

		<script type="text/javascript" src="/static/js/user/other.js"></script>

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
					% if user[5] == 'True':
						<span id="user_id" class="id_admin">#{{user[0]}}</span>
					% else:
						<span id="user_id" class="id_normal">#{{user[0]}}</span>
					% end
					<div id="user_info">
						<span id="user_mail">{{user[2]}}</span>
						<span id="user_identity">{{user[3]}} {{user[4]}}</span>
					</div>
					<span id="user_picture"><img src="{{user[8]}}"></span>

					<a href="#" data-id="{{user[0]}}" class="follow button">Chargement...</a>

					<div id="user_stat">
						<span id="user_layer_number">{{user[6]}} calque(s) ajouté(s)</span>
						<span id="user_comments">{{user[7]}} Commentaire(s)</span>
					</div>

					% if len(layers) > 0:
						<div id="user_layers">
							<span id="user_layers_title">
								Voir les calques >>
							</span>
							% for layer in layers:
								<a href="/layer/{{layer[0]}}"><div class="layer_item">
									<span class="layer_item_id">#{{layer[0]}}</span><br>
									<span class="layer_item_chapter">Dans {{layer[2]}}, {{layer[3]}}</span>
								</div></a>
							% end
						</div>
					% end


					<div id="user_follow">
						<div id="followed">
							Suivi par {{followedNumber}} personnes.
							<div id="followed_list"> <!--TODO: ajouter annimation de panneau pliable/dépliable-->
								% for follower in followed:
									<span><a data-id="{{follower[0]}}" href="/user/{{follower[0]}}" class="user_info"><img  class="user_picture" src="{{follower[5]}}"></a></span>
								% end
							</div>
						</div>
						<br>
						<hr>
						<br>
						<div id="follow">
							Suit {{followNumber}} personnes.
							<div id="follow_list"> <!--TODO: ajouter animation de panneau pliable/dépliable-->
								% for follown in follow:
									<span><a data-id="{{follown[0]}}" href="/user/{{follown[0]}}" class="user_info"><img src="{{follown[5]}}"></a></span>
								% end
							</div>
						</div>
					</div>
				</div>
			</div>
	</body>
</html>

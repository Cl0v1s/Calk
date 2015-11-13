<!DOCTYPE html>
<html>
    <head>
        <title>Créer un calque</title>
        <meta charset="utf-8">
		<link rel="stylesheet" href="/static/css/global.css">

		<!--jquery-->
		<script type="text/javascript" src="/static/js/jquery.js"></script>

		<!--tooltipster-->
		<link rel="stylesheet" href="/static/css/tooltipster.css">
		<script type="text/javascript" src="/static/js/tooltipster.js"></script>

		<script type="text/javascript" src="/static/js/global.js"></script>

		<!--froala style-->
		<link href="/static/css/font-awesome.min.css" rel="stylesheet" type="text/css">
		<link href="/static/css/froala_editor.min.css" rel="stylesheet" type="text/css">
		<link href="/static/css/froala_style.min.css" rel="stylesheet" type="text/css">

		<!--froala javascript-->
		<script src="/static/js/libs/jquery-1.11.1.min.js"></script>
		<script src="/static/js/froala_editor.min.js"></script>
		<!--[if lt IE 9]>
			<script src="/static/js/froala_editor_ie8.min.js"></script>
		<![endif]-->
		<script src="/static/js/plugins/tables.min.js"></script>
		<script src="/static/js/plugins/urls.min.js"></script>
		<script src="/static/js/plugins/lists.min.js"></script>
		<script src="/static/js/plugins/colors.min.js"></script>
		<script src="/static/js/plugins/font_family.min.js"></script>
		<script src="/static/js/plugins/font_size.min.js"></script>
		<script src="/static/js/plugins/block_styles.min.js"></script>
		<script src="/static/js/plugins/media_manager.min.js"></script>
		<script src="/static/js/plugins/video.min.js"></script>
		<script src="/static/js/plugins/char_counter.min.js"></script>

		<script type="text/javascript" src="/static/js/layer/create.js"></script>

	</head>
	<body>
		<nav>
			<span id="nav_title" class="nav_item">Calk</span>
			<span id="nav_page" class="nav_item">Créer un calque</span>
			<span id="nav_links" class="nav_item"><a href="/index"><img id="nav_home" src="/static/img/home.svg"></a></span>
		</nav>
		<div class="first_content_under">
		</div>
		<div class="first_content">
			<div class="panel">
				<a href="#" class="button" id="layer_create_save" data-based-on="{{basedOn}}" data-chapter="{{chapter}}">Sauvegarder</a>
				<br>
				<div id="layer_create_editor" style="max-height: 500px;">
					{{! content}}
				</div>
			</div>
		</div>
	</body>
</html>

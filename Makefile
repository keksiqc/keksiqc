image:
	mkdir -p assets
	python -c "import sys; sys.path.append('.')" # Ensure current directory is in path
	freeze ./profile.py -o ./assets/profile.png --language python --window -r 8 --border.width 1 --theme rose-pine --font.ligatures

assets/profile.png: profile.py
	mkdir -p assets
	cat profile.py | freeze -o assets/profile.png --language python -m 20 --window --border.radius 8 --border.width 1 --theme rose-pine --font.ligatures

.PHONY: clean
clean:
	rm -rf assets/profile.png

assets/profile.png: profile.py
	mkdir -p assets
	cat profile.py | freeze -o assets/profile.png --language python --height 420 --border.radius 8 --theme rose-pine --font.ligatures

.PHONY: clean
clean:
	rm -rf assets/profile.png

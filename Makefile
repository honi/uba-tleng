svg:
	find . -name "*.dot" | sed -e 's/\.dot//' | xargs -I % dot -Tpng %.dot -o %.png

.PHONY: svg

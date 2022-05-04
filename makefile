DIR_DATA := ~/.encouragement
FILE_CFG := config.cfg

CFG_SRC := data/$(FILE_CFG)
CFG_DST := $(DIR_DATA)/$(FILE_CFG)

PYCACHE := $(shell find -regex ".*__pycache__")
PYCACHE := $(subst ./,,$(PYCACHE))

.phony: install uninstall clean
install: $(CFG_DST)
uninstall:
	rm -rf $(DIR_DATA)
clean: FORCE
	rm -rf $(PYCACHE)
FORCE:
$(DIR_DATA):
	mkdir $@
$(CFG_DST): $(CFG_SRC) | $(DIR_DATA)
	cp $< $@

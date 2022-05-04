from encouragement import CONFIG
from encouragement.util import contents_file

def phrases() -> list[str]:
	id_file = CONFIG['gdrive']['fileid']
	p = contents_file(id_file) \
	.decode() \
	.split('\n')
	return [s for s in p if s]

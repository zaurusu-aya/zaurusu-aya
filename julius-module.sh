export ALSADEV="plughw:1,0"

DICT=~/julius-dict/am-gmm.jconf
GRAM=meirei
julius -C $DICT -gram $GRAM -nostrip -module
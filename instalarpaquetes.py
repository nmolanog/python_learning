###see https://stackoverflow.com/questions/49839610/attributeerror-module-pip-has-no-attribute-main
###you may have to open python 3 with sudo, i.e: in terminal sudo python3
from pip._internal import main
main(["install","sqlalchemy"])

###old one
import pip
pip.main(["install","matplotlib"])
pip.main(["install","pandas"])
pip.main(["install","matplotlib"])
pip.main(["install","xlrd"])
pip.main(["install","h5py"])
print("termine")
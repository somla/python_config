from .arg import *
from .config_base import ConfigBase

class TheConfig(ConfigBase):
    configFile:StrArg = StrArg(help="Config json file default: config.json", default_value="config.json")
    test:IntArg = IntArg(help="alma")
    test1:BoolArg = BoolArg(help="alma", default_value = True)
    testFloat:FloatArg = FloatArg(help="Float string", is_optional=False)
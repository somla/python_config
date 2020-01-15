# Python config

Ez a könyvtár saját config beolvasásában nyújt segítséget
Json és argparse segítségével

Használat:
1. másold a config/ mappát a projektedbe
2. írd felül a config/the_config.py ízlés szerint
3. importáld a "from config import theConfig" a main.py-odba
4. minden más helyre is, ahol használni akarod
5. a configokat theConfig.xy néven éred el

BUG:
configFile:StrArg kötelező, és nem nevezhető át.
Továbbá configFile is kötelező.
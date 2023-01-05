from deta import Deta

DETA_KEY = "b0ekrw6c_DmRHhaEzMMFgCaPqqNmde9JhhwKFovQR"

deta = Deta(DETA_KEY)

db = deta.Base("all_Users")
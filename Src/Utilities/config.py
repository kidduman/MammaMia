import json
import os
import logging

# Variabile richiesta da loadenv.py
dotenv = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')

# Impostazione del livello log richiesto da mfp.py
LEVEL = "INFO"

# Funzione richiesta da mfp.py per sbloccare i log
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

# Configurazione manuale diretta per evitare KeyError su Render
SITE = {
    "StreamingCommunity": {"url": "https://vixsrc.to", "SC_ForwardProxy": "0", "SC_PROXY": "0", "VX_ForwardProxy": "0", "VX_PROXY": "0"},
    "CB01": {"url": "https://cb01uno.click", "CB_PROXY": "0", "CB_ForwardProxy": "0", "MX_ForwardProxy": "0", "MX_PROXY": "0"},
    "Guardaserie": {"url": "https://guarda-serie.click", "GS_ForwardProxy": "0", "GS_PROXY": "0"},
    "Guardoserie": {"url": "https://guarda-serie.click", "GO_ForwardProxy": "0", "GO_PROXY": "0"},
    "GuardaHD": {"url": "https://guardahd.stream", "GH_ForwardProxy": "0", "GH_PROXY": "0"},
    "OnlineSerieTV": {"url": "https://onlineserie.tv", "OST_ForwardProxy": "0", "OST_PROXY": "0"},
    "Filmpertutti": {"url": "https://filmpertutti.uno", "FPT_ForwardProxy": "0", "FPT_PROXY": "0"},
    "AnimeWorld": {"url": "https://animeworld.so", "AW_ForwardProxy": "0", "AW_PROXY": "0"},
    "Eurostreaming": {"url": "https://eurostreaming.vision", "ES_ForwardProxy": "0", "ES_PROXY": "0"},
    "TantiFilm": {"url": "https://tantifilm.uno", "TF_ForwardProxy": "0", "TF_PROXY": "0"},
    "StreamingCommunityOld": {"url": "https://streamingcommunity.presse", "SCO_ForwardProxy": "0", "SCO_PROXY": "0"},
    "Guardaflix": {"url": "https://guardaflix.bond", "GF_ForwardProxy": "0", "GF_PROXY": "0"},
    "IlGenioDelloStreaming": {"url": "https://ilgeniodellostreaming.wtf", "IDS_ForwardProxy": "0", "IDS_PROXY": "0"},
    "Realtime": {"url": "https://realtime.com", "RT_ForwardProxy": "0", "RT_PROXY": "0"},
    "Altadefinizione": {"url": "https://altadefinizione.click", "AD_ForwardProxy": "0", "AD_PROXY": "0"},
    "Cinemahd": {"url": "https://cinemahd.click", "CHD_HighQuality": "0", "CHD_PROXY": "0"},
    "StreamingCommunityNew": {"url": "https://streamingcommunity.click", "SCN_ForwardProxy": "0", "SCN_PROXY": "0"},
    "Toonitalia": {"url": "https://toonitalia.xyz", "TI_ForwardProxy": "0", "TI_PROXY": "0"},
    "Vidxgo": {"url": "https://vidxgo.biz", "VD_ForwardProxy": "0", "VD_PROXY": "0"}
}

# Mappatura delle variabili singole richieste dal resto del codice
SC_DOMAIN = SITE['StreamingCommunity']['url']
SC_ForwardProxy = SITE['StreamingCommunity']['SC_ForwardProxy']
SC_PROXY = SITE['StreamingCommunity']['SC_PROXY']
VX_ForwardProxy = SITE['StreamingCommunity']['VX_ForwardProxy']
VX_PROXY = SITE['StreamingCommunity']['VX_PROXY']

CB_DOMAIN = SITE['CB01']['url']
CB_PROXY = SITE['CB01']['CB_PROXY']
CB_ForwardProxy = SITE['CB01']['CB_ForwardProxy']
MX_ForwardProxy = SITE['CB01']['MX_ForwardProxy']
MX_PROXY = SITE['CB01']['MX_PROXY']

GS_DOMAIN = SITE['Guardaserie']['url']
GS_ForwardProxy = SITE['Guardaserie']['GS_ForwardProxy']
GS_PROXY = SITE['Guardaserie']['GS_PROXY']

GO_DOMAIN = SITE['Guardoserie']['url']
GO_ForwardProxy = SITE['Guardoserie']['GO_ForwardProxy']
GO_PROXY = SITE['Guardoserie']['GO_PROXY']

GH_DOMAIN = SITE['GuardaHD']['url']
GH_ForwardProxy = SITE['GuardaHD']['GH_ForwardProxy']
GH_PROXY = SITE['GuardaHD']['GH_PROXY']

OST_DOMAIN = SITE['OnlineSerieTV']['url']
FPT_DOMAIN = SITE['Filmpertutti']['url']

AW_DOMAIN = SITE['AnimeWorld']['url']
AW_ForwardProxy = SITE['AnimeWorld']['AW_ForwardProxy']
AW_PROXY = SITE['AnimeWorld']['AW_PROXY']

ES_DOMAIN = SITE['Eurostreaming']['url']
ES_ForwardProxy = SITE['Eurostreaming']['ES_ForwardProxy']
ES_PROXY = SITE['Eurostreaming']['ES_PROXY']

TF_DOMAIN = SITE['TantiFilm']['url']
TF_ForwardProxy = SITE['TantiFilm']['TF_ForwardProxy']
TF_PROXY = SITE['TantiFilm']['TF_PROXY']

GF_DOMAIN = SITE['Guardaflix']['url']
GF_ForwardProxy = SITE['Guardaflix']['GF_ForwardProxy']
GF_PROXY = SITE['Guardaflix']['GF_PROXY']

IDS_DOMAIN = SITE['IlGenioDelloStreaming']['url']
IDS_ForwardProxy = SITE['IlGenioDelloStreaming']['IDS_ForwardProxy']
IDS_PROXY = SITE['IlGenioDelloStreaming']['IDS_PROXY']

AD_DOMAIN = SITE['Altadefinizione']['url']
AD_ForwardProxy = SITE['Altadefinizione']['AD_ForwardProxy']
AD_PROXY = SITE['Altadefinizione']['AD_PROXY']

TI_DOMAIN = SITE['Toonitalia']['url']
TI_ForwardProxy = SITE['Toonitalia']['TI_ForwardProxy']
TI_PROXY = SITE['Toonitalia']['TI_PROXY']

VD_DOMAIN = SITE['Vidxgo']['url']
VD_ForwardProxy = SITE['Vidxgo']['VD_ForwardProxy']
VD_PROXY = SITE['Vidxgo']['VD_PROXY']

# Riferimenti globali richiesti dagli estrattori e dall'interfaccia web
VERSION = "1.0.0"
GLOBAL_PROXY = "0"
GLOBAL_ForwardProxy = "0"
Icon = "https://raw.githubusercontent.com/debridmedialab/mammamia/main/icon.png"
Name = "MammaMia"
Description = "Addon privato per Stremio"

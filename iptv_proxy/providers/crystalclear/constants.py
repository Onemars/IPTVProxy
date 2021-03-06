class CrystalClearConstants(object):
    BASE_URL = 'http://ccmedia.one:25461/'
    DB_FILE_NAME = 'crystalclear.db'
    DEFAULT_EPG_SOURCE = 'crystalclear'
    DEFAULT_PLAYLIST_PROTOCOL = 'hls'
    DEFAULT_PLAYLIST_TYPE = 'dynamic'
    EPG_PATH = 'xmltv.php'
    M3U8_PLAYLIST_FILE_NAME = 'tv_channels_{0}.m3u'
    M3U8_PLAYLIST_PATH = 'get.php'
    PROVIDER_NAME = 'CrystalClear'
    TEMPORARY_DB_FILE_NAME = 'crystalclear_temp.db'
    VALID_EPG_SOURCE_VALUES = ['other', 'crystalclear']
    VALID_PLAYLIST_PROTOCOL_VALUES = ['hls', 'mpegts']
    VALID_PLAYLIST_TYPE_VALUES = ['dynamic', 'static']
    XML_EPG_FILE_NAME = 'xmltv.xml'

    _provider_name = PROVIDER_NAME.lower()

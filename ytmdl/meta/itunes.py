"""
Python module to search itunes using itunespy
"""
import itunespy


def __get_albums_by_name_and_artist(album_name, itunes_artists):
    if itunes_artists is None:
        if album_name is not None:
            return itunespy.search_album(album_name)
        else:
            return None

    albums_itunes = []
    for artist in itunes_artists:
        albums = artist.get_albums()
        for album in albums:
            if album_name is None \
                    or album_name.lower() in album.collection_name.lower():
                albums_itunes.append(album)
    return albums_itunes


def __get_tracks_by_name_and_album(song_name, albums_itunes):
    if albums_itunes is None:
        return None

    SONG_INFO = []
    for itunes_album in albums_itunes:
        tracks = itunes_album.get_tracks()
        for track in tracks:
            if song_name.lower() in track.track_name.lower():
                SONG_INFO.append(track)
    return SONG_INFO


def searchSong(song_name, artist=None, album=None):
    artists_itunes = None
    if artist is not None:
        artists_itunes = itunespy.search_artist(artist)

    albums_itunes = __get_albums_by_name_and_artist(album, artists_itunes)

    SONG_INFO = __get_tracks_by_name_and_album(song_name, albums_itunes)

    if SONG_INFO is None:
        SONG_INFO = itunespy.search_track(song_name)
    return SONG_INFO

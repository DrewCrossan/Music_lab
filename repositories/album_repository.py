from db.run_sql import run_sql
import repositories.artist_repository as artist_repository
from models.album import Album

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])

        album = Album(row['album_name'], row['genre'], artist, row['id'])
        albums.append(album)

    return albums

def save(album):
    sql = "INSERT INTO albums (album_name, genre, artist, artist_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [album.album_name, album.genre, album.artist.artist_name, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['album_name'], result['genre'], artist, result['id'])

    return album

def delete_all():
    sql = "DELETE FROM albums;"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)
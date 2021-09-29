import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository 
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Bring Me The Horizon")
artist_repository.save(artist1)
artist2 = Artist("Flume")
artist_repository.save(artist2)

album1 = Album("Pray for plagues", "Metal", artist1)
album_repository.save(album1)
album2 = Album("Suicide Season", "Metal", artist1)
album_repository.save(album2)
album3 = Album("Sempiternal", "Metal", artist1)
album_repository.save(album3)

album4 = Album("Flume (Deluxe Edition)", "Electronic", artist2)
album_repository.save(album4)
album5 = Album("Skin", "Electronic", artist2)
album_repository.save(album5)








pdb.set_trace()


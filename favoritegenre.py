def favoritegenre (userMap,genreMap):
    users={}
    for i in userMap:
        users[i]=[]
        for j in genreMap :
            for song in userMap[i] :
                if(song in genreMap[j] and j not in users[i]):   
                    users[i].append(j)
        # print(i)
    return users

user_map={
    "David":["song1","song2","song3","song4","song8"],
    "Emma": ["song5","song6","song7"]
}
genre_map = {
    "Rock": ["song1","song3"],
    "Dubstep":["song7"],
    "Techno":["song2","song4"],
    "Pop":["song5","song6"],
    "Jazz":["song8","song9"]
}
result = favoritegenre(user_map,genre_map)
print(result)
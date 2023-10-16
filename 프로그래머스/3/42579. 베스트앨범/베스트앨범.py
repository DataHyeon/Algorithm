def solution(genres, plays):
    answer = []
    
    # 장르별 총 재생 횟수 및 곡 정보 저장
    genre_total_play = {}
    genre_songs = {}
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_total_play:
            genre_total_play[genre] = 0
            genre_songs[genre] = []
        
        genre_total_play[genre] += play
        genre_songs[genre].append((play, idx))
    
    # 장르별 총 재생 횟수를 기준으로 내림차순 정렬
    sorted_genres = sorted(genre_total_play.keys(), key=lambda x: genre_total_play[x], reverse=True)
    
    for genre in sorted_genres:
        # 장르 내에서 노래를 재생 횟수와 고유 번호를 기준으로 정렬
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        
        # 최대 2곡 선택
        for song in sorted_songs[:2]:
            answer.append(song[1])
    
    return answer

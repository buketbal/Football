from football.core import TournamentScraper, LeagueScraper

# tournament_path = 'Tournaments.html'
tournament_url = 'http://www.goal.com/tr/ligler'
tc = TournamentScraper()
tc.open_from_url(url=tournament_url)
# tc.open_from_file(path=tournament_path)
tc_list = tc.get_popular_tournaments()
for i in tc_list:
    print(i)

# league_path = 'SuperLigPuanDurumu.html'
league_url = 'http://www.goal.com/tr/s%C3%BCper-lig/puan-durumu/482ofyysbdbeoxauk19yg7tdt'
lc = LeagueScraper()
lc.open_from_url(url=league_url)
# lc.open_from_file(path=league_path)
lc_list = lc.get_teams()
for i in lc_list:
    print(i)

'''OUTPUT
<Tournaments(name=Dünya Kupası, link=http://www.goal.com/tr/d%C3%BCnya-kupas%C4%B1/puan-durumu/70excpe1synn9kadnbppahdn7)>
<Tournaments(name=Süper Lig, link=http://www.goal.com/tr/s%C3%BCper-lig/puan-durumu/482ofyysbdbeoxauk19yg7tdt)>
<Tournaments(name=UEFA Şampiyonlar Ligi, link=http://www.goal.com/tr/uefa-%C5%9Fampiyonlar-ligi/puan-durumu/4oogyu6o156iphvdvphwpck10)>
<Tournaments(name=UEFA Avrupa Ligi, link=http://www.goal.com/tr/uefa-avrupa-ligi/puan-durumu/4c1nfi2j1m731hcay25fcgndq)>
<Tournaments(name=La Liga, link=http://www.goal.com/tr/la-liga/puan-durumu/34pl8szyvrbwcmfkuocjm3r6t)>
<Tournaments(name=Premier Lig, link=http://www.goal.com/tr/premier-lig/puan-durumu/2kwbbcootiqqgmrzs6o5inle5)>
<Tournaments(name=Serie A, link=http://www.goal.com/tr/serie-a/puan-durumu/1r097lpxe0xn03ihb7wi98kao)>
<Tournaments(name=Bundesliga, link=http://www.goal.com/tr/bundesliga/puan-durumu/6by3h89i2eykc341oz7lv1ddd)>
<Tournaments(name=Ligue 1, link=http://www.goal.com/tr/ligue-1/puan-durumu/dm5ka0os1e3dxcp3vh05kmp33)>
<Tournaments(name=1. Lig, link=http://www.goal.com/tr/1-lig/puan-durumu/2o9svokc5s7diish3ycrzk7jm)>
<Tournaments(name=Kupa, link=http://www.goal.com/tr/kupa/puan-durumu/7af85xa75vozt2l4hzi6ryts7)>
<Tournaments(name=Dünya Kupası Avrupa Elemeleri, link=http://www.goal.com/tr/d%C3%BCnya-kupas%C4%B1-avrupa-elemeleri/puan-durumu/39q1hq42hxjfylxb7xpe9bvf9)>
<Tournaments(name=Hazırlık Ülkeler, link=http://www.goal.com/tr/haz%C4%B1rl%C4%B1k-%C3%BClkeler/puan-durumu/cesdwwnxbc5fmajgroc0hqzy2)>
<Tournaments(name=Eredivisie, link=http://www.goal.com/tr/eredivisie/puan-durumu/akmkihra9ruad09ljapsm84b3)>
<Tournaments(name=İspanya Kral Kupası, link=http://www.goal.com/tr/ispanya-kral-kupas%C4%B1/puan-durumu/apdwh753fupxheygs8seahh7x)>
<Team(pos=1, name=İstanbul Başakşehir, om=30, g=19, b=5, m=6, a=+22, p=62)> 
<Team(pos=2, name=Galatasaray, om=29, g=19, b=3, m=7, a=+35, p=60)> 
<Team(pos=3, name=Beşiktaş, om=29, g=17, b=8, m=4, a=+32, p=59)> 
<Team(pos=4, name=Fenerbahçe, om=29, g=16, b=9, m=4, a=+27, p=57)> 
<Team(pos=5, name=Trabzonspor, om=29, g=12, b=10, m=7, a=+11, p=46)> 
<Team(pos=6, name=Kayserispor, om=30, g=12, b=8, m=10, a=-6, p=44)> 
<Team(pos=7, name=Göztepe, om=29, g=12, b=7, m=10, a=-5, p=43)> 
<Team(pos=8, name=Sivasspor, om=29, g=12, b=5, m=12, a=-7, p=41)> 
<Team(pos=9, name=Kasımpaşa, om=29, g=11, b=7, m=11, a=0, p=40)> 
<Team(pos=10, name=Yeni Malatyaspor, om=29, g=10, b=8, m=11, a=-4, p=38)> 
<Team(pos=11, name=Antalyaspor, om=29, g=9, b=8, m=12, a=-13, p=35)> 
<Team(pos=12, name=Akhisar Belediyespor, om=29, g=9, b=7, m=13, a=-10, p=34)> 
<Team(pos=13, name=Bursaspor, om=29, g=9, b=6, m=14, a=-5, p=33)> 
<Team(pos=14, name=Alanyaspor, om=29, g=9, b=5, m=15, a=-5, p=32)> 
<Team(pos=15, name=Gençlerbirliği, om=29, g=7, b=9, m=13, a=-11, p=30)> 
<Team(pos=16, name=Konyaspor, om=29, g=7, b=8, m=14, a=-5, p=29)> 
<Team(pos=17, name=Osmanlıspor, om=29, g=7, b=8, m=14, a=-9, p=29)> 
<Team(pos=18, name=Karabükspor, om=29, g=3, b=3, m=23, a=-47, p=12)>
'''

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import json
import math
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import statistics
import random




data = pd.read_json("metadata.json")

with open("C:\\Users\\tmp\\Desktop\\metadata.json","r") as file:
    raw = json.load(file)


rawYear = data['Year']
year = []
ageRating = data['Rated']
rawMonth = data['Released']
month = []
rawRunTime = data['Runtime']
runTime = []
rawGenre = data['Genre']
rawLanguage = data['Language']
language = []
rawCountry = data['Country']
country = []
rawImdbVotes = data['imdbVotes']
imdbVotes = []
rawBoxOffice = data['BoxOffice']
boxOffice = []
ratings = data['Ratings']
rawRotten = []
for entry in ratings:
    #ratingSize = len(entry)
    appendVal = 0.0
    for source in entry:
        if(source['Source'] == 'Rotten Tomatoes'):
            appendVal = (float(source['Value'][0:-1]))/10
        else:
            appendVal = 5.0
    rawRotten.append(appendVal)
print(rawRotten[0])
#print(type(rawRotten[0][0]))


rotten = []


rawDependent = data['imdbRating']
dependent = []
independent = []

valAgeRatings = []
valMonth = []
genre = []
valLanguage = []
valCountry = []


#FUNCTIONS =========================================================================================================================
def getAllNonStandard():
    
    for i in range (0,len(data)):
        #print(i)
        #print(raw[i])
        year.append(int(rawYear[i][0:3]))
       
        month.append(rawMonth[i][3:6])
        
        if(rawRunTime[i] == "N/A"):
            runTime.append(0)
        else:
            timeSplit = rawRunTime[i].split(" ")
            if(len(timeSplit[0])==3 and timeSplit[0][2]=='S'):
                runTime.append(0)
            else:
                runTime.append(int(timeSplit[0]))
        
        
        language.append(rawLanguage[i][0])
        
        country.append(rawCountry[i][0])
        
        stringVote = rawImdbVotes[i]
        if(stringVote != "N/A"):
            stripped = stringVote.replace(",","")
            imdbVotes.append(int(stripped))
        else:
            imdbVotes.append(0)
        
        stringBox = rawBoxOffice[i]
        if(stringBox != "N/A" and pd.isna(stringBox) == False):
            stripped = stringBox.replace(",","")
            stripped = stripped.replace("$","")
            boxOffice.append(int(stripped))
        else:
            boxOffice.append(0)
        
        if(rawDependent[i] == "N/A"):
            dependent.append(-1.0)
        else:
            dependent.append(float(rawDependent[i]))
        
        #rotten.append(rawRotten[i])
            
            
def valuefyData():
    
    ratingAxis = ['Unrated','Approved','All Ages', '12+', '13+','14+', '16+', '17+', '18+']
    monthAxis = ['Jan', 'Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Undisclosed']
    genreAxis = ['Action', 'Fantasy', 'Romance', 'Adventure', 'Drama', 'Thriller', 'Comedy', 'Music', 'Mystery', 'Horror', 'Sci-Fi', 'Family', 'Crime', 'Documentary', 'Sport', 'War', 'Biography', 'History', 'Animation', 'Western', 'Short', 'Musical', 'Film-Noir', 'Adult', 'Talk-Show', 'Reality-TV', 'News', 'Game-Show', 'N/A']
    languageAxis = ['N/A', 'Mandarin', 'English', 'Korean', 'Spanish', 'French', 'Danish', 'Turkish', 'Russian', 'Romanian', 'Swedish', 'Japanese', 'Persian', 'Italian', 'Cantonese', 'Czech', 'None', 'Bosnian', 'Finnish', 'Tibetan', 'Croatian', 'Polish', 'German', 'Serbian', 'Norwegian', 'Slovenian', 'Hindi', 'Macedonian', 'Vietnamese', 'Icelandic', 'Hungarian', 'Latin', 'Portuguese', 'Hawaiian', 'Thai', 'Tagalog', 'Greek', 'Bengali', 'Chinese', 'Marathi', 'Serbo-Croatian', 'Romany', 'Dutch', 'Estonian', 'American Sign ', 'Arabic', 'Slovak', 'Filipino', 'Mongolian', 'Malayalam', 'Lithuanian', 'Dzongkha', 'Ukrainian', 'Sanskrit', 'Maya', 'Catalan', 'Flemish', 'Swiss German', 'Neapolitan', 'Hebrew', 'Georgian', 'Irish Gaelic', 'Low German', 'Kru', 'Aramaic', 'Sicilian', 'Armenian', 'Urdu', 'Micmac', 'Tamil', 'Kazakh', 'Saami', 'Belarusian', 'Kurdish', 'Zulu', 'Aboriginal', 'Bulgarian', 'Amharic', 'Afrikaans', 'Indonesian', 'Wolof', 'Telugu', 'Bambara', 'Bable', 'Albanian', 'Algonquin', 'Scanian', 'Chechen', 'Basque', 'East-Greenlandic', 'Inuktitut', 'Maltese', 'American Sign Language', 'Sioux', 'Latvian', 'Sinhala', 'Nenets', 'Welsh', 'Pashtu', 'Malay', 'Kannada', 'Swahili', 'Punjabi', 'Panjabi', 'Scots', 'Chhattisgarhi', 'Kyrgyz', 'Maori', 'Nepali', 'Yiddish', 'Gallegan', 'Yakut', 'Sindhi', 'Central Khmer', 'Kikuyu', 'Min Nan', 'Guarani', 'Luxembourgish', 'Peul', 'Quechua', 'Wayuu', 'Akan', 'Crimean Tatar', 'Galician']
    countriesAxis = ['N/A', 'China', 'United States', 'South Korea', 'United Kingdom', 'France', 'UK', 'Mexico', 'Spain', 'Canada', 'Ireland', 'Denmark', 'Turkey', 'Russia', 'New Zealand', 'Taiwan', 'Romania', 'USA', 'Germany', 'Sweden', 'Yugoslavia', 'Hong Kong', 'Australia', 'Japan', 'Czech Republic', 'Finland', 'Peru', 'Aruba', 'Italy', 'Switzerland', 'Soviet Union', 'Serbia', 'Luxembourg', 'West Germany', 'Chile', 'Argentina', 'Federal Republic of Yugoslavia', 'Slovenia', 'India', 'Iceland', 'Netherlands', 'Monaco', 'Hungary', 'South Africa', 'Norway', 'Brazil', 'Thailand', 'Czechoslovakia', 'Philippines', 'Greece', 'Belgium', 'Estonia', 'Uruguay', 'Poland', 'Austria', 'Lithuania', 'Bosnia and Herzegovina', 'Bhutan', 'Portugal', 'North Macedonia', 'Algeria', 'Indonesia', 'Bulgaria', 'Serbia and Montenegro', 'Israel', 'Colombia', 'Zimbabwe', 'East Germany', 'Iran', 'Puerto Rico', 'Kazakhstan', 'Nigeria', 'Cuba', 'Croatia', 'Slovakia', 'Bangladesh', 'Belarus', 'Egypt', 'Paraguay', 'Senegal', 'Latvia', 'Lebanon', 'Georgia', 'Dominican Republic', 'United Arab Emirates', 'Malaysia', 'Singapore', 'Bahamas', 'Venezuela', 'Armenia', 'Jordan', 'Occupied Palestinian Territory', 'Saudi Arabia', 'Ghana', 'Vietnam', 'Sudan', 'Costa Rica', 'Ukraine', 'Panama', 'Ethiopia', 'Sri Lanka', 'Isle of Man', 'Qatar', 'Jamaica', 'Malta', 'Albania', 'Papua New Guinea', 'Mongolia', 'Kenya', 'Kyrgyzstan', 'Iraq', 'Morocco', 'Nepal', 'Chad', 'North Korea', 'Guatemala', 'Pakistan', 'Cambodia', 'Tunisia', 'Cyprus', 'Ecuador']
    
    for i in range (0, len(data)):
        #ageRating
        if(ageRating[i] == 'N/A' or ageRating[i] == 'Not Rated' or ageRating[i] == 'Unrated' or ageRating[i] == 'UNRATED' or ageRating[i] == 'NOT RATED'):
            valAgeRatings.append(0)
        elif(ageRating[i] == 'Approved' or ageRating[i] == 'Passed' or ageRating[i] == 'PASSED' or ageRating[i] == 'Open' or ageRating[i] == 'APPROVED'):
            valAgeRatings.append(1)
        elif(ageRating[i] == 'G' or ageRating[i] == 'TV-G' or ageRating[i] == 'GP' or ageRating[i] == 'TV-Y7' or ageRating[i] == 'TV-Y7-FV' or ageRating[i] == 'TV-Y'):
            valAgeRatings.append(2)
        elif(ageRating[i] == 'TV-PG' or ageRating[i] == 'PG' or ageRating[i] == '12'):
            valAgeRatings.append(3)
        elif(ageRating[i] == 'PG-13' or ageRating[i] == '13+' or ageRating[i] == 'TV-13'):
            valAgeRatings.append(4)
        elif(ageRating[i] == 'TV-14'):
            valAgeRatings.append(5)
        elif(ageRating[i] == '16+'):
            valAgeRatings.append(6)
        elif(ageRating[i] == 'R' or ageRating[i] == 'MA-17' or ageRating[i] == 'M/PG' or ageRating[i] == 'M' or ageRating[i] == 'MA' or ageRating[i] == 'TV-MA'):
            valAgeRatings.append(7)
        elif(ageRating[i] == 'NC-17' or ageRating[i] == '18+' or ageRating[i] == 'X' or ageRating[i] == 'AO'):
            valAgeRatings.append(8)        
            
        #month
        tmpStr = rawMonth[i][3:6]
        if(tmpStr == "Jan"):
            valMonth.append(1)
        elif(tmpStr == "Feb"):
            valMonth.append(2)
        elif(tmpStr == "Mar"):
            valMonth.append(3)
        elif(tmpStr == "Apr"):
            valMonth.append(4)
        elif(tmpStr == "May"):
            valMonth.append(5)
        elif(tmpStr == "Jun"):
            valMonth.append(6)
        elif(tmpStr == "Jul"):
            valMonth.append(7)
        elif(tmpStr == "Aug"):
            valMonth.append(8)
        elif(tmpStr == "Sep"):
            valMonth.append(9)    
        elif(tmpStr == "Oct"):
            valMonth.append(10)
        elif(tmpStr == "Nov"):
            valMonth.append(11)
        elif(tmpStr == "Dec"):
            valMonth.append(12) 
        else:
            valMonth.append(13)
        
        #genre
        tmpList = rawGenre[i].split(", ")
        value = tmpList[0]
        if(value == 'Action'):
            genre.append(1)
        elif(value == 'Fantasy'):
            genre.append(2)
        elif(value == 'Romance'):
            genre.append(3)
        elif(value == 'Adventure'):
            genre.append(4)
        elif(value == 'Drama'):
            genre.append(5)   
        elif(value == 'Thriller'):
            genre.append(6)
        elif(value == 'Comedy'):
            genre.append(7)
        elif(value == 'Music'):
            genre.append(8)
        elif(value == 'Mystery'):
            genre.append(9)
        elif(value == 'Horror'):
            genre.append(10)
        elif(value == 'Sci-Fi'):
            genre.append(11)
        elif(value == 'Family'):
            genre.append(12)
        elif(value == 'Crime'):
            genre.append(13)   
        elif(value == 'Documentary'):
            genre.append(14)
        elif(value == 'Sport'):
            genre.append(15)
        elif(value == 'War'):
            genre.append(16)
        elif(value == 'Biography'):
            genre.append(17)
        elif(value == 'History'):
            genre.append(18)
        elif(value == 'Animation'):
            genre.append(19)
        elif(value == 'Western'):
            genre.append(20)
        elif(value == 'Short'):
            genre.append(21)   
        elif(value == 'Musical'):
            genre.append(22)
        elif(value == 'Film-Noir'):
            genre.append(23)
        elif(value == 'Adult'):
            genre.append(24)
        elif(value == 'Talk-Show'):
            genre.append(25)
        elif(value == 'Reality-TV'):
            genre.append(26)
        elif(value == 'News'):
            genre.append(27)
        elif(value == 'Game-Show'):
            genre.append(28)
        elif(value == 'N/A'):
            genre.append(29)
            
            
        #Language
        tmpList1 = rawLanguage[i].split(", ")
        lang = tmpList1[0]
        
        if(lang == 'N/A'):
            valLanguage.append(0)
        elif(lang == 'Mandarin'):
            valLanguage.append(1)
        elif(lang == 'English'):
            valLanguage.append(2)
        elif(lang == 'Korean'):
            valLanguage.append(3)
        elif(lang == 'Spanish'):
            valLanguage.append(4)
        elif(lang == 'French'):
            valLanguage.append(5)
        elif(lang == 'Danish'):
            valLanguage.append(6)
        elif(lang == 'Turkish'):
            valLanguage.append(7)
        elif(lang == 'Russian'):
            valLanguage.append(8)
        elif(lang == 'Romanian'):
            valLanguage.append(9)
        elif(lang == 'Swedish'):
            valLanguage.append(10)
        elif(lang == 'Japanese'):
            valLanguage.append(11)
        elif(lang == 'Persian'):
            valLanguage.append(12)
        elif(lang == 'Italian'):
            valLanguage.append(13)
        elif(lang == 'Cantonese'):
            valLanguage.append(14)
        elif(lang == 'Czech'):
            valLanguage.append(15)
        elif(lang == 'None'):
            valLanguage.append(16)  
        elif(lang == 'Bosnian'):
            valLanguage.append(17)
        elif(lang == 'Finnish'):
            valLanguage.append(18)
        elif(lang == 'Tibetan'):
            valLanguage.append(19)
        elif(lang == 'Croatian'):
            valLanguage.append(20)
        elif(lang == 'Polish'):
            valLanguage.append(21)
        elif(lang == 'German'):
            valLanguage.append(22)
        elif(lang == 'Serbian'):
            valLanguage.append(23)
        elif(lang == 'Norwegian'):
            valLanguage.append(24)
        elif(lang == 'Slovenian'):
            valLanguage.append(25)
        elif(lang == 'Hindi'):
            valLanguage.append(26)
        elif(lang == 'Macedonian'):
            valLanguage.append(27)
        elif(lang == 'Vietnamese'):
            valLanguage.append(28)
        elif(lang == 'Icelandic'):
            valLanguage.append(29)
        elif(lang == 'Hungarian'):
            valLanguage.append(30)
        elif(lang == 'Latin'):
            valLanguage.append(31)
        elif(lang == 'Portuguese'):
            valLanguage.append(32)
        elif(lang == 'Hawaiian'):
            valLanguage.append(33)
        elif(lang == 'Thai'):
            valLanguage.append(34)
        elif(lang == 'Tagalog'):
            valLanguage.append(35)
        elif(lang == 'Greek'):
            valLanguage.append(36)
        elif(lang == 'Bengali'):
            valLanguage.append(37)
        elif(lang == 'Chinese'):
            valLanguage.append(38)
        elif(lang == 'Marathi'):
            valLanguage.append(39)
        elif(lang == 'Serbo-Croatian'):
            valLanguage.append(40)
        elif(lang == 'Romany'):
            valLanguage.append(41)
        elif(lang == 'Dutch'):
            valLanguage.append(42)
        elif(lang == 'Estonian'):
            valLanguage.append(43)
        elif(lang == 'American Sign '):
            valLanguage.append(44)
        elif(lang == 'Arabic'):
            valLanguage.append(45)
        elif(lang == 'Slovak'):
            valLanguage.append(46)
        elif(lang == 'Filipino'):
            valLanguage.append(47)
        elif(lang == 'Mongolian'):
            valLanguage.append(48)  
        elif(lang == 'Malayalam'):
            valLanguage.append(49)
        elif(lang == 'Lithuanian'):
            valLanguage.append(50)
        elif(lang == 'Dzongkha'):
            valLanguage.append(51)
        elif(lang == 'Ukrainian'):
            valLanguage.append(52)
        elif(lang == 'Sanskrit'):
            valLanguage.append(53)
        elif(lang == 'Maya'):
            valLanguage.append(54)
        elif(lang == 'Catalan'):
            valLanguage.append(55)
        elif(lang == 'Flemish'):
            valLanguage.append(56)
        elif(lang == 'Swiss German'):
            valLanguage.append(57)
        elif(lang == 'Neapolitan'):
            valLanguage.append(58)
        elif(lang == 'Hebrew'):
            valLanguage.append(59)
        elif(lang == 'Georgian'):
            valLanguage.append(60)
        elif(lang == 'Irish Gaelic'):
            valLanguage.append(61)
        elif(lang == 'Low German'):
            valLanguage.append(62)
        elif(lang == 'Kru'):
            valLanguage.append(63)
        elif(lang == 'Aramaic'):
            valLanguage.append(64)
        elif(lang == 'Sicilian'):
            valLanguage.append(65)
        elif(lang == 'Armenian'):
            valLanguage.append(66)
        elif(lang == 'Urdu'):
            valLanguage.append(67)
        elif(lang == 'Micmac'):
            valLanguage.append(68)
        elif(lang == 'Tamil'):
            valLanguage.append(69)
        elif(lang == 'Kazakh'):
            valLanguage.append(70)
        elif(lang == 'Saami'):
            valLanguage.append(71)
        elif(lang == 'Belarusian'):
            valLanguage.append(72)
        elif(lang == 'Kurdish'):
            valLanguage.append(73)
        elif(lang == 'Zulu'):
            valLanguage.append(74)
        elif(lang == 'Aboriginal'):
            valLanguage.append(75)
        elif(lang == 'Bulgarian'):
            valLanguage.append(76)
        elif(lang == 'Amharic'):
            valLanguage.append(77)
        elif(lang == 'Afrikaans'):
            valLanguage.append(78)
        elif(lang == 'Indonesian'):
            valLanguage.append(79)
        elif(lang == 'Wolof'):
            valLanguage.append(80)  
        elif(lang == 'Telugu'):
            valLanguage.append(81)
        elif(lang == 'Bambara'):
            valLanguage.append(82)
        elif(lang == 'Bable'):
            valLanguage.append(83)
        elif(lang == 'Albanian'):
            valLanguage.append(84)
        elif(lang == 'Algonquin'):
            valLanguage.append(85)
        elif(lang == 'Scanian'):
            valLanguage.append(86)
        elif(lang == 'Chechen'):
            valLanguage.append(87)
        elif(lang == 'Basque'):
            valLanguage.append(88)
        elif(lang == 'East-Greenlandic'):
            valLanguage.append(89)
        elif(lang == 'Inuktitut'):
            valLanguage.append(90)
        elif(lang == 'Maltese'):
            valLanguage.append(91)
        elif(lang == 'American Sign Language'):
            valLanguage.append(92)
        elif(lang == 'Sioux'):
            valLanguage.append(93)
        elif(lang == 'Latvian'):
            valLanguage.append(94)
        elif(lang == 'Sinhala'):
            valLanguage.append(95)
        elif(lang == 'Nenets'):
            valLanguage.append(96)
        elif(lang == 'Welsh'):
            valLanguage.append(97)
        elif(lang == 'Pashtu'):
            valLanguage.append(98)
        elif(lang == 'Malay'):
            valLanguage.append(99)
        elif(lang == 'Kannada'):
            valLanguage.append(100)
        elif(lang == 'Swahili'):
            valLanguage.append(101)
        elif(lang == 'Punjabi'):
            valLanguage.append(102)
        elif(lang == 'Panjabi'):
            valLanguage.append(103)
        elif(lang == 'Scots'):
            valLanguage.append(104)
        elif(lang == 'Chhattisgarhi'):
            valLanguage.append(105)
        elif(lang == 'Kyrgyz'):
            valLanguage.append(106)
        elif(lang == 'Maori'):
            valLanguage.append(107)
        elif(lang == 'Nepali'):
            valLanguage.append(108)
        elif(lang == 'Yiddish'):
            valLanguage.append(109)
        elif(lang == 'Gallegan'):
            valLanguage.append(110)
        elif(lang == 'Yakut'):
            valLanguage.append(111)
        elif(lang == 'Sindhi'):
            valLanguage.append(112)  
        elif(lang == 'Central Khmer'):
            valLanguage.append(113)
        elif(lang == 'Kikuyu'):
            valLanguage.append(114)
        elif(lang == 'Min Nan'):
            valLanguage.append(115)
        elif(lang == 'Guarani'):
            valLanguage.append(116)
        elif(lang == 'Luxembourgish'):
            valLanguage.append(117)
        elif(lang == 'Peul'):
            valLanguage.append(118)
        elif(lang == 'Quechua'):
            valLanguage.append(119)
        elif(lang == 'Wayuu'):
            valLanguage.append(120)
        elif(lang == 'Akan'):
            valLanguage.append(121)
        elif(lang == 'Crimean Tatar'):
            valLanguage.append(122)
        elif(lang == 'Galician'):
            valLanguage.append(123)
            
        
        #Country
        tmpList2 = rawCountry[i].split(", ")
        country = tmpList2[0]
        
        if(country == 'N/A'):
            valCountry.append(0)
        elif(country == 'China'):
            valCountry.append(1)
        elif(country == 'United States'):
            valCountry.append(2)
        elif(country == 'South Korea'):
            valCountry.append(3)
        elif(country == 'United Kingdom'):
            valCountry.append(4)
        elif(country == 'France'):
            valCountry.append(5)
        elif(country == 'UK'):
            valCountry.append(6)
        elif(country == 'Mexico'):
            valCountry.append(7)
        elif(country == 'Spain'):
            valCountry.append(8)
        elif(country == 'Canada'):
            valCountry.append(9)
        elif(country == 'Ireland'):
            valCountry.append(10)
        elif(country == 'Denmark'):
            valCountry.append(11)
        elif(country == 'Turkey'):
            valCountry.append(12)
        elif(country == 'Russia'):
            valCountry.append(13)
        elif(country == 'New Zealand'):
            valCountry.append(14)
        elif(country == 'Taiwan'):
            valCountry.append(15)
        elif(country == 'Romania'):
            valCountry.append(16)  
        elif(country == 'USA'):
            valCountry.append(17)
        elif(country == 'Germany'):
            valCountry.append(18)
        elif(country == 'Sweden'):
            valCountry.append(19)
        elif(country == 'Yugoslavia'):
            valCountry.append(20)
        elif(country == 'Hong Kong'):
            valCountry.append(21)
        elif(country == 'Australia'):
            valCountry.append(22)
        elif(country == 'Japan'):
            valCountry.append(23)
        elif(country == 'Czech Republic'):
            valCountry.append(24)
        elif(country == 'Finland'):
            valCountry.append(25)
        elif(country == 'Peru'):
            valCountry.append(26)
        elif(country == 'Aruba'):
            valCountry.append(27)
        elif(country == 'Italy'):
            valCountry.append(28)
        elif(country == 'Switzerland'):
            valCountry.append(29)
        elif(country == 'Soviet Union'):
            valCountry.append(30)
        elif(country == 'Serbia'):
            valCountry.append(31)
        elif(country == 'Luxembourg'):
            valCountry.append(32)
        elif(country == 'West Germany'):
            valCountry.append(33)
        elif(country == 'Chile'):
            valCountry.append(34)
        elif(country == 'Argentina'):
            valCountry.append(35)
        elif(country == 'Federal Republic of Yugoslavia'):
            valCountry.append(36)
        elif(country == 'Slovenia'):
            valCountry.append(37)
        elif(country == 'India'):
            valCountry.append(38)
        elif(country == 'Iceland'):
            valCountry.append(39)
        elif(country == 'Netherlands'):
            valCountry.append(40)
        elif(country == 'Monaco'):
            valCountry.append(41)
        elif(country == 'Hungary'):
            valCountry.append(42)
        elif(country == 'South Africa'):
            valCountry.append(43)
        elif(country == 'Norway'):
            valCountry.append(44)
        elif(country == 'Brazil'):
            valCountry.append(45)
        elif(country == 'Thailand'):
            valCountry.append(46)
        elif(country == 'Czechoslovakia'):
            valCountry.append(47)
        elif(country == 'Philippines'):
            valCountry.append(48)  
        elif(country == 'Greece'):
            valCountry.append(49)
        elif(country == 'Belgium'):
            valCountry.append(50)
        elif(country == 'Estonia'):
            valCountry.append(51)
        elif(country == 'Uruguay'):
            valCountry.append(52)
        elif(country == 'Poland'):
            valCountry.append(53)
        elif(country == 'Austria'):
            valCountry.append(54)
        elif(country == 'Lithuania'):
            valCountry.append(55)
        elif(country == 'Bosnia and Herzegovina'):
            valCountry.append(56)
        elif(country == 'Bhutan'):
            valCountry.append(57)
        elif(country == 'Portugal'):
            valCountry.append(58)
        elif(country == 'North Macedonia'):
            valCountry.append(59)
        elif(country == 'Algeria'):
            valCountry.append(60)
        elif(country == 'Indonesia'):
            valCountry.append(61)
        elif(country == 'Bulgaria'):
            valCountry.append(62)
        elif(country == 'Serbia and Montenegro'):
            valCountry.append(63)
        elif(country == 'Israel'):
            valCountry.append(64)
        elif(country == 'Colombia'):
            valCountry.append(65)
        elif(country == 'Zimbabwe'):
            valCountry.append(66)
        elif(country == 'East Germany'):
            valCountry.append(67)
        elif(country == 'Iran'):
            valCountry.append(68)
        elif(country == 'Puerto Rico'):
            valCountry.append(69)
        elif(country == 'Kazakhstan'):
            valCountry.append(70)
        elif(country == 'Nigeria'):
            valCountry.append(71)
        elif(country == 'Cuba'):
            valCountry.append(72)
        elif(country == 'Croatia'):
            valCountry.append(73)
        elif(country == 'Slovakia'):
            valCountry.append(74)
        elif(country == 'Bangladesh'):
            valCountry.append(75)
        elif(country == 'Belarus'):
            valCountry.append(76)
        elif(country == 'Egypt'):
            valCountry.append(77)
        elif(country == 'Paraguay'):
            valCountry.append(78)
        elif(country == 'Senegal'):
            valCountry.append(79)
        elif(country == 'Latvia'):
            valCountry.append(80)  
        elif(country == 'Lebanon'):
            valCountry.append(81)
        elif(country == 'Georgia'):
            valCountry.append(82)
        elif(country == 'Dominican Republic'):
            valCountry.append(83)
        elif(country == 'United Arab Emirates'):
            valCountry.append(84)
        elif(country == 'Malaysia'):
            valCountry.append(85)
        elif(country == 'Singapore'):
            valCountry.append(86)
        elif(country == 'Bahamas'):
            valCountry.append(87)
        elif(country == 'Venezuela'):
            valCountry.append(88)
        elif(country == 'Armenia'):
            valCountry.append(89)
        elif(country == 'Jordan'):
            valCountry.append(90)
        elif(country == 'Occupied Palestinian Territory'):
            valCountry.append(91)
        elif(country == 'Saudi Arabia'):
            valCountry.append(92)
        elif(country == 'Ghana'):
            valCountry.append(93)
        elif(country == 'Vietnam'):
            valCountry.append(94)
        elif(country == 'Sudan'):
            valCountry.append(95)
        elif(country == 'Costa Rica'):
            valCountry.append(96)
        elif(country == 'Ukraine'):
            valCountry.append(97)
        elif(country == 'Panama'):
            valCountry.append(98)
        elif(country == 'Ethiopia'):
            valCountry.append(99)
        elif(country == 'Sri Lanka'):
            valCountry.append(100)
        elif(country == 'Isle of Man'):
            valCountry.append(101)
        elif(country == 'Qatar'):
            valCountry.append(102)
        elif(country == 'Jamaica'):
            valCountry.append(103)
        elif(country == 'Malta'):
            valCountry.append(104)
        elif(country == 'Albania'):
            valCountry.append(105)
        elif(country == 'Papua New Guinea'):
            valCountry.append(106)
        elif(country == 'Mongolia'):
            valCountry.append(107)
        elif(country == 'Kenya'):
            valCountry.append(108)
        elif(country == 'Kyrgyzstan'):
            valCountry.append(109)
        elif(country == 'Iraq'):
            valCountry.append(110)
        elif(country == 'Morocco'):
            valCountry.append(111)
        elif(country == 'Nepal'):
            valCountry.append(112)  
        elif(country == 'Chad'):
            valCountry.append(113)
        elif(country == 'North Korea'):
            valCountry.append(114)
        elif(country == 'Guatemala'):
            valCountry.append(115)
        elif(country == 'Pakistan'):
            valCountry.append(116)
        elif(country == 'Cambodia'):
            valCountry.append(117)
        elif(country == 'Tunisia'):
            valCountry.append(118)
        elif(country == 'Cyprus'):
            valCountry.append(119)
        elif(country == 'Ecuador'):
            valCountry.append(120)        
                


            
def createIndependentList():
    for i in range (0,len(data)):
        tmpList = [year[i], valMonth[i], valAgeRatings[i],runTime[i],genre[i],valLanguage[i],valCountry[i],imdbVotes[i],boxOffice[i]]
        independent.append(tmpList)
    



#Main      =========================================================================================================================



getAllNonStandard()

valuefyData()

createIndependentList()

print("independent: " , len(independent))
print("dependent: " , len(dependent))
avg = statistics.mean(dependent)
print("avg imdb rating: ", avg)
med = statistics.median(dependent)
print("med imdb rating: ", med)

Xtrain,Xtest,ytrain,ytest,rawRot,yRot = train_test_split(independent, dependent, rawRotten, test_size=0.3, shuffle=True)




lr = LinearRegression()
lr.fit(Xtrain,ytrain)

yIntercept = lr.intercept_

coefs = lr.coef_

print(yIntercept)
print(coefs)




predictY = lr.predict(Xtest)
print("ytest")
print(ytest)
print("predictY")
print(predictY)

total = 0
mseTotal = 0
count = 0
randTotal = 0
rotTotal = 0
for i in range(0,len(ytest)):
    die = random.uniform(0.0,10.0)
    count += 1
    total += abs(ytest[i] - predictY[i]) 
    mseTotal += (ytest[i] - predictY[i])**2
    randTotal += abs(die - ytest[i])
    rotTotal += abs(yRot[i] - ytest[i])
    

print("total ", total)
print("count ", count)
print("linear regression mean absolute error: ",  total/count)
print("mean squared error: ",  mseTotal/count)
print("dice roller mean absolute error: ", randTotal/count)
print("rotten mean absolute error: ", rotTotal/count)

print("model: ", r2_score(ytest,predictY))
print("avg: ", r2_score(ytest,[avg]*len(ytest)))
print("med: ", r2_score(ytest,[med]*len(ytest)))


slope1, intercept1 = np.polyfit(year, dependent, 1)
x1 = np.linspace(188,203,10)
slope2, intercept2 = np.polyfit(valMonth, dependent, 1)
x2 = np.linspace(0,14,10)
slope3, intercept3 = np.polyfit(valAgeRatings, dependent, 1)
x3 = np.linspace(0,8,10)
slope4, intercept4 = np.polyfit(runTime, dependent, 1)
x4 = np.linspace(-1,240,10)
slope5, intercept5 = np.polyfit(genre, dependent, 1)
x5 = np.linspace(0,30,10)
slope6, intercept6 = np.polyfit(valLanguage, dependent, 1)
x6 = np.linspace(0,125,10)
slope7, intercept7 = np.polyfit(valCountry, dependent, 1)
x7 = np.linspace(0,125,10)
slope8, intercept8 = np.polyfit(imdbVotes, dependent, 1)
x8 = np.linspace(0,3000000,10)
slope9, intercept9 = np.polyfit(boxOffice, dependent, 1)
x9 = np.linspace(0,900000000,10)


plt.figure('Linear year',figsize=(16,10))
plt.scatter(year,dependent)
plt.plot(x1,slope1*x1 + intercept1)
plt.show()

plt.figure('Linear month',figsize=(16,10))
plt.scatter(valMonth,dependent)
plt.plot(x2,slope2*x2 + intercept2)
plt.show()

plt.figure('Linear valAgeRatings',figsize=(16,10))
plt.scatter(valAgeRatings,dependent)
plt.plot(x3,slope3*x3 + intercept3)
plt.show()

plt.figure('Linear runTime',figsize=(16,10))
plt.scatter(runTime,dependent)
#check this
plt.plot(x4,slope4*x4 + intercept4)
plt.xlim(0,240)
plt.ylim(0,10)
plt.show()

plt.figure('Linear genre',figsize=(16,10))
plt.scatter(genre,dependent)
plt.plot(x5,slope5*x5 + intercept5)
plt.show()

plt.figure('Linear valLanguage',figsize=(16,10))
plt.scatter(valLanguage,dependent)
plt.plot(x6,slope6*x6 + intercept6)
plt.show()

plt.figure('Linear valCountry',figsize=(16,10))
plt.scatter(valCountry,dependent)
plt.plot(x7,slope7*x7 + intercept7)
plt.show()

plt.figure('Linear imdbVotes',figsize=(16,10))
plt.scatter(imdbVotes,dependent)
plt.plot(x8,slope8*x8 + intercept8)
plt.show()

plt.figure('Linear boxOffice',figsize=(16,10))
plt.scatter(boxOffice,dependent)
plt.plot(x9,slope9*x9 + intercept9)
plt.show()




#Xtrain,Xtest,ytrain,ytest = train_test_split(X, y, test_size=0.0001)





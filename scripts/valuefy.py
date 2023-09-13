import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import json
import math
from sklearn.linear_model import LinearRegression


data = pd.read_json("metadata.json")

#age = data['Rated']
#allRatings = []

#flag = False
#count = 0
#for i in age:
    #if(i == 'N/A' or i == 'Not Rated' or i == 'Unrated' or i == 'UNRATED' or i == 'NOT RATED'):
        #allRatings.append(0)
    #elif(i == 'Approved' or i == 'Passed' or i == 'PASSED' or i == 'Open' or i == 'APPROVED'):
        #allRatings.append(1)
    #elif(i == 'G' or i == 'TV-G' or i == 'GP' or i == 'TV-Y7' or i == 'TV-Y7-FV' or i == 'TV-Y'):
        #allRatings.append(2)
    #elif(i == 'TV-PG' or i == 'PG' or i == '12'):
        #allRatings.append(3)
    #elif(i == 'PG-13' or i == '13+' or i == 'TV-13'):
        #allRatings.append(4)
    #elif(i == 'TV-14'):
        #allRatings.append(5)
    #elif(i == '16+'):
        #allRatings.append(6)
    #elif(i == 'R' or i == 'MA-17' or i == 'M/PG' or i == 'M' or i == 'MA' or i == 'TV-MA'):
        #allRatings.append(7)
    #elif(i == 'NC-17' or i == '18+' or i == 'X' or i == 'AO'):
        #allRatings.append(8)


#print(len(allRatings))

#rawMonth = data['Released']
#month = []


#count = 0
#for i in rawMonth:
    #tmpStr = i[3:6]
    #if(tmpStr == "Jan"):
        #month.append(1)
    #elif(tmpStr == "Feb"):
        #month.append(2)
    #elif(tmpStr == "Mar"):
        #month.append(3)
    #elif(tmpStr == "Apr"):
        #month.append(4)
    #elif(tmpStr == "May"):
        #month.append(5)
    #elif(tmpStr == "Jun"):
        #month.append(6)
    #elif(tmpStr == "Jul"):
        #month.append(7)
    #elif(tmpStr == "Aug"):
        #month.append(8)
    #elif(tmpStr == "Sep"):
        #month.append(9)    
    #elif(tmpStr == "Oct"):
        #month.append(10)
    #elif(tmpStr == "Nov"):
        #month.append(11)
    #elif(tmpStr == "Dec"):
        #month.append(12) 
    #else:
        #print(tmpStr)
        #month.append(13)

#print(len(month))

#rawGenre = data['Genre']
#g1Val = []

#for i in rawGenre:
    #tmpList = i.split(", ")
    #for j in tmpList:
        #flag = True
        #for k in genList:
            #if(j == k):
                #flag = False
        #if(flag):
            #genList.append(j)

#print(genList)
#print(len(genList))

#for i in rawGenre:
    #tmpList = i.split(", ")
    #value = tmpList[0]
    #if(value == 'Action'):
        #g1Val.append(1)
    #elif(value == 'Fantasy'):
        #g1Val.append(2)
    #elif(value == 'Romance'):
        #g1Val.append(3)
    #elif(value == 'Adventure'):
        #g1Val.append(4)
    #elif(value == 'Drama'):
        #g1Val.append(5)   
    #elif(value == 'Thriller'):
        #g1Val.append(6)
    #elif(value == 'Comedy'):
        #g1Val.append(7)
    #elif(value == 'Music'):
        #g1Val.append(8)
    #elif(value == 'Mystery'):
        #g1Val.append(9)
    #elif(value == 'Horror'):
        #g1Val.append(10)
    #elif(value == 'Sci-Fi'):
        #g1Val.append(11)
    #elif(value == 'Family'):
        #g1Val.append(12)
    #elif(value == 'Crime'):
        #g1Val.append(13)   
    #elif(value == 'Documentary'):
        #g1Val.append(14)
    #elif(value == 'Sport'):
        #g1Val.append(15)
    #elif(value == 'War'):
        #g1Val.append(16)
    #elif(value == 'Biography'):
        #g1Val.append(17)
    #elif(value == 'History'):
        #g1Val.append(18)
    #elif(value == 'Animation'):
        #g1Val.append(19)
    #elif(value == 'Western'):
        #g1Val.append(20)
    #elif(value == 'Short'):
        #g1Val.append(21)   
    #elif(value == 'Musical'):
        #g1Val.append(22)
    #elif(value == 'Film-Noir'):
        #g1Val.append(23)
    #elif(value == 'Adult'):
        #g1Val.append(24)
    #elif(value == 'Talk-Show'):
        #g1Val.append(25)
    #elif(value == 'Reality-TV'):
        #g1Val.append(26)
    #elif(value == 'News'):
        #g1Val.append(27)
    #elif(value == 'Game-Show'):
        #g1Val.append(28)
    #elif(value == 'N/A'):
        #g1Val.append(29)       
        
#rawLanguage = data['Language']
#langList = []

#for i in rawLanguage:
    #tmpList = i.split(", ")
    #lang = tmpList[0]
    #flag = True
    #for k in langList:
        #if(lang == k):
            #flag = False
    #if(flag):
        #langList.append(lang)
#print(langList)
        
        
        
        
        
        
        
        
#rawLanguage = data['Language']
#valLanguage = []

# for i in rawLanguage:
#     tmpList = i.split(", ")
#     lang = tmpList[0]
    
#     if(lang == 'N/A'):
#         langAxis.append(0)
#     elif(lang == 'Mandarin'):
#         langAxis.append(1)
#     elif(lang == 'English'):
#         langAxis.append(2)
#     elif(lang == 'Korean'):
#         langAxis.append(3)
#     elif(lang == 'Spanish'):
#         langAxis.append(4)
#     elif(lang == 'French'):
#         langAxis.append(5)
#     elif(lang == 'Danish'):
#         langAxis.append(6)
#     elif(lang == 'Turkish'):
#         langAxis.append(7)
#     elif(lang == 'Russian'):
#         langAxis.append(8)
#     elif(lang == 'Romanian'):
#         langAxis.append(9)
#     elif(lang == 'Swedish'):
#         langAxis.append(10)
#     elif(lang == 'Japanese'):
#         langAxis.append(11)
#     elif(lang == 'Persian'):
#         langAxis.append(12)
#     elif(lang == 'Italian'):
#         langAxis.append(13)
#     elif(lang == 'Cantonese'):
#         langAxis.append(14)
#     elif(lang == 'Czech'):
#         langAxis.append(15)
#     elif(lang == 'None'):
#         langAxis.append(16)  
#     elif(lang == 'Bosnian'):
#         langAxis.append(17)
#     elif(lang == 'Finnish'):
#         langAxis.append(18)
#     elif(lang == 'Tibetan'):
#         langAxis.append(19)
#     elif(lang == 'Croatian'):
#         langAxis.append(20)
#     elif(lang == 'Polish'):
#         langAxis.append(21)
#     elif(lang == 'German'):
#         langAxis.append(22)
#     elif(lang == 'Serbian'):
#         langAxis.append(23)
#     elif(lang == 'Norwegian'):
#         langAxis.append(24)
#     elif(lang == 'Slovenian'):
#         langAxis.append(25)
#     elif(lang == 'Hindi'):
#         langAxis.append(26)
#     elif(lang == 'Macedonian'):
#         langAxis.append(27)
#     elif(lang == 'Vietnamese'):
#         langAxis.append(28)
#     elif(lang == 'Icelandic'):
#         langAxis.append(29)
#     elif(lang == 'Hungarian'):
#         langAxis.append(30)
#     elif(lang == 'Latin'):
#         langAxis.append(31)
#     elif(lang == 'Portuguese'):
#         langAxis.append(32)
#     elif(lang == 'Hawaiian'):
#         langAxis.append(33)
#     elif(lang == 'Thai'):
#         langAxis.append(34)
#     elif(lang == 'Tagalog'):
#         langAxis.append(35)
#     elif(lang == 'Greek'):
#         langAxis.append(36)
#     elif(lang == 'Bengali'):
#         langAxis.append(37)
#     elif(lang == 'Chinese'):
#         langAxis.append(38)
#     elif(lang == 'Marathi'):
#         langAxis.append(39)
#     elif(lang == 'Serbo-Croatian'):
#         langAxis.append(40)
#     elif(lang == 'Romany'):
#         langAxis.append(41)
#     elif(lang == 'Dutch'):
#         langAxis.append(42)
#     elif(lang == 'Estonian'):
#         langAxis.append(43)
#     elif(lang == 'American Sign '):
#         langAxis.append(44)
#     elif(lang == 'Arabic'):
#         langAxis.append(45)
#     elif(lang == 'Slovak'):
#         langAxis.append(46)
#     elif(lang == 'Filipino'):
#         langAxis.append(47)
#     elif(lang == 'Mongolian'):
#         langAxis.append(48)  
#     elif(lang == 'Malayalam'):
#         langAxis.append(49)
#     elif(lang == 'Lithuanian'):
#         langAxis.append(50)
#     elif(lang == 'Dzongkha'):
#         langAxis.append(51)
#     elif(lang == 'Ukrainian'):
#         langAxis.append(52)
#     elif(lang == 'Sanskrit'):
#         langAxis.append(53)
#     elif(lang == 'Maya'):
#         langAxis.append(54)
#     elif(lang == 'Catalan'):
#         langAxis.append(55)
#     elif(lang == 'Flemish'):
#         langAxis.append(56)
#     elif(lang == 'Swiss German'):
#         langAxis.append(57)
#     elif(lang == 'Neapolitan'):
#         langAxis.append(58)
#     elif(lang == 'Hebrew'):
#         langAxis.append(59)
#     elif(lang == 'Georgian'):
#         langAxis.append(60)
#     elif(lang == 'Irish Gaelic'):
#         langAxis.append(61)
#     elif(lang == 'Low German'):
#         langAxis.append(62)
#     elif(lang == 'Kru'):
#         langAxis.append(63)
#     elif(lang == 'Aramaic'):
#         langAxis.append(64)
#     elif(lang == 'Sicilian'):
#         langAxis.append(65)
#     elif(lang == 'Armenian'):
#         langAxis.append(66)
#     elif(lang == 'Urdu'):
#         langAxis.append(67)
#     elif(lang == 'Micmac'):
#         langAxis.append(68)
#     elif(lang == 'Tamil'):
#         langAxis.append(69)
#     elif(lang == 'Kazakh'):
#         langAxis.append(70)
#     elif(lang == 'Saami'):
#         langAxis.append(71)
#     elif(lang == 'Belarusian'):
#         langAxis.append(72)
#     elif(lang == 'Kurdish'):
#         langAxis.append(73)
#     elif(lang == 'Zulu'):
#         langAxis.append(74)
#     elif(lang == 'Aboriginal'):
#         langAxis.append(75)
#     elif(lang == 'Bulgarian'):
#         langAxis.append(76)
#     elif(lang == 'Amharic'):
#         langAxis.append(77)
#     elif(lang == 'Afrikaans'):
#         langAxis.append(78)
#     elif(lang == 'Indonesian'):
#         langAxis.append(79)
#     elif(lang == 'Wolof'):
#         langAxis.append(80)  
#     elif(lang == 'Telugu'):
#         langAxis.append(81)
#     elif(lang == 'Bambara'):
#         langAxis.append(82)
#     elif(lang == 'Bable'):
#         langAxis.append(83)
#     elif(lang == 'Albanian'):
#         langAxis.append(84)
#     elif(lang == 'Algonquin'):
#         langAxis.append(85)
#     elif(lang == 'Scanian'):
#         langAxis.append(86)
#     elif(lang == 'Chechen'):
#         langAxis.append(87)
#     elif(lang == 'Basque'):
#         langAxis.append(88)
#     elif(lang == 'East-Greenlandic'):
#         langAxis.append(89)
#     elif(lang == 'Inuktitut'):
#         langAxis.append(90)
#     elif(lang == 'Maltese'):
#         langAxis.append(91)
#     elif(lang == 'American Sign Language'):
#         langAxis.append(92)
#     elif(lang == 'Sioux'):
#         langAxis.append(93)
#     elif(lang == 'Latvian'):
#         langAxis.append(94)
#     elif(lang == 'Sinhala'):
#         langAxis.append(95)
#     elif(lang == 'Nenets'):
#         langAxis.append(96)
#     elif(lang == 'Welsh'):
#         langAxis.append(97)
#     elif(lang == 'Pashtu'):
#         langAxis.append(98)
#     elif(lang == 'Malay'):
#         langAxis.append(99)
#     elif(lang == 'Kannada'):
#         langAxis.append(100)
#     elif(lang == 'Swahili'):
#         langAxis.append(101)
#     elif(lang == 'Punjabi'):
#         langAxis.append(102)
#     elif(lang == 'Panjabi'):
#         langAxis.append(103)
#     elif(lang == 'Scots'):
#         langAxis.append(104)
#     elif(lang == 'Chhattisgarhi'):
#         langAxis.append(105)
#     elif(lang == 'Kyrgyz'):
#         langAxis.append(106)
#     elif(lang == 'Maori'):
#         langAxis.append(107)
#     elif(lang == 'Nepali'):
#         langAxis.append(108)
#     elif(lang == 'Yiddish'):
#         langAxis.append(109)
#     elif(lang == 'Gallegan'):
#         langAxis.append(110)
#     elif(lang == 'Yakut'):
#         langAxis.append(111)
#     elif(lang == 'Sindhi'):
#         langAxis.append(112)  
#     elif(lang == 'Central Khmer'):
#         langAxis.append(113)
#     elif(lang == 'Kikuyu'):
#         langAxis.append(114)
#     elif(lang == 'Min Nan'):
#         langAxis.append(115)
#     elif(lang == 'Guarani'):
#         langAxis.append(116)
#     elif(lang == 'Luxembourgish'):
#         langAxis.append(117)
#     elif(lang == 'Peul'):
#         langAxis.append(118)
#     elif(lang == 'Quechua'):
#         langAxis.append(119)
#     elif(lang == 'Wayuu'):
#         langAxis.append(120)
#     elif(lang == 'Akan'):
#         langAxis.append(121)
#     elif(lang == 'Crimean Tatar'):
#         langAxis.append(122)
#     elif(lang == 'Galician'):
#         langAxis.append(123)

    

#print(langAxis)
#print(len(langAxis))


rawCountry = data['Country']
countryList = []

for i in rawCountry:
    tmpList = i.split(", ")
    country = tmpList[0]
    flag = True
    for k in countryList:
        if(country == k):
            flag = False
    if(flag):
        countryList.append(country)
print(countryList)

valCountry = []

for i in rawCountry:
    tmpList = i.split(", ")
    country = tmpList[0]
    
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
    else:
        print(country)
    

print(len(valCountry))

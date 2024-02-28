import data
import project

assert project.get_doubled_letter_countries() == ('Morocco', 'Greece', 'Marshall Islands', 'Seychelles', 'Cameroon', 'Philippines', 'Andorra', 'Sierra Leone', 'Guinea-Bissau', 'Russia', 'Saint Kitts and Nevis'), "error creating doubled-letters tuple"
assert project.get_funny_case_capital_cities('a') == ['KaBul', 'tiRaNa (tiRaNe)', 'aLgiers', 'aNdorRa La velLa', 'lUaNDa', "SaInt john's", 'buenos aIres', 'yereVaN', 'CaNberRa', 'vienNa', 'BaKu', 'NaSSaU', 'MaNaMa', 'dHaKa', 'belmoPaN', 'SaRaJevo', 'GaBorone', 'bRaSilIa', 'BaNDaR seri beGaWaN', 'sofIa', 'oUaGaDougou', 'giteGa', 'YaOunde', 'otTaWa', 'pRaIa', 'BaNgui', "n'dJaMeNa", 'SaNtIaGo', 'bogoTa', 'kinsHaSa', 'bRaZZaVille', 'SaN jose', 'YaMoussoukro', 'ZaGreb', 'HaVaNa', 'nicosIa', 'pRaGue', 'copenHaGen', 'rosEaU', 'SaNto domingo', 'CaIro', 'SaN SaLVaDor', 'MaLaBo', 'aSMaRa', 'TaLlinn', 'mBaBaNa', 'aDdis aBaBa', 'PaLikir', 'suVa', 'PaRis', 'BaNjul', 'aCcRa', 'aThens', "SaInt george's", 'gUaTeMaLa city', 'coNaKry', 'bisSaU', 'port aU prince', 'teguciGaLPa', 'buDaPest', 'reykJaVik', 'JaKaRTa', 'tehRaN', 'BaGhDaD', 'jeruSaLem', 'aMMaN', 'nur-sulTaN', 'NaIrobi', 'TaRaWa aToll', 'pristiNa', 'kuWaIt city', 'vientIaNe', 'riGa', 'MaSeru', 'monrovIa', 'VaDuz', 'aNTaNaNaRivo', 'kUaLa lumpur', 'MaLe', 'BaMaKo', 'VaLletTa', 'MaJuro', 'noUaKchott', 'chisiNaU', 'moNaCo', 'uLaaNBaaTaR', 'podgoriCa', 'RaBaT', 'MaPuto', 'NaY pyi TaW', 'no officIaL CaPiTaL', 'KaThMaNdu', 'aMsterDaM', 'MaNaGUa', 'nIaMey', 'aBuJa', 'pyongYaNg', 'belFaSt', 'musCaT', 'isLaMaBaD', 'PaNaMa city', 'aSuncion', 'liMa', 'MaNiLa', 'WaRSaW', 'doHa', 'bucHaRest', 'kiGaLi', 'BaSseterre', 'CaStries', 'aPIa', 'SaN MaRino', 'SaO tome', 'riYaDh', 'DaKaR', 'belgRaDe', 'victorIa', 'sinGaPore', 'bRaTisLaVa', 'ljublJaNa', 'honIaRa', 'moGaDishu', 'pretorIa, bloemfontein, CaPe town', 'juBa', 'MaDrid', 'kHaRtoum', 'PaRaMaRibo', 'DaMaScus', 'TaIpei', 'dusHaNbe', 'dodoMa', 'BaNgkok', "nuku'aLoFa", 'port of sPaIn', 'aNKaRa', 'aShGaBaT', 'fuNaFuti', 'KaMPaLa', 'aBu dHaBi', 'WaShington d.c.', 'TaShkent', 'port viLa', 'VaTiCaN city', 'CaRaCaS', 'HaNoi', 'CaRdiff', "SaNa'a", 'luSaKa', 'HaRaRe'], "error creating funny case using letter a"
assert project.get_funny_case_capital_cities('w') == ['bridgetOwN', 'bandar seri begAwAn', 'ottAwA', 'georgetOwN', 'nEw delhi', 'tarAwA atoll', 'kUwAit city', 'lilonGwE', 'nay pyi tAw', 'wIndhoek', 'wEllington', 'wArsAw', 'moscOw', 'kingstOwN', 'freetOwN', 'pretoria, bloemfontein, cape tOwN', 'wAshington d.c.'], "error creating funny case using letter w"
assert project.get_funny_case_capital_cities('t') == ['tIrana (tIrane)', "saiNt john's", 'bridgEtOwn', 'poRtO novo', 'tHimphu', 'gItEga', 'OttAwa', 'saNtIago', 'bogOtA', 'djiboUtI', 'saNtO domingo', 'quItO', 'tAllinn', 'tBilisi', 'AtHens', "saiNt george's", 'guAtEmala cItY', 'georgEtOwn', 'poRt au prince', 'tEgucigalpa', 'budapeSt', 'jakaRtA', 'tEhran', 'kingStOn', 'tOkyo', 'nur-suLtAn', 'tArawa AtOll', 'priStIna', 'kuwaIt cItY', 'vieNtIane', 'beirUt', 'tRipoli', 'aNtAnanarivo', 'vallEttA', 'nouakchOtt', 'poRt louis', 'mexico cItY', 'ulaanbaAtAr', 'rabAt', 'mapUtO', 'nay pyi tAw', 'no official capItAl', 'kAtHmandu', 'amStErdam', 'wellinGtOn', 'belfaSt', 'muscAt', 'panama cItY', 'poRt moresby', 'buchareSt', 'bassEtErre', 'caStRies', 'kingStOwn', 'sao tOme', 'viCtOria', 'freEtOwn', 'brAtIslava', 'prEtOria, bloemfoNtEin, cape tOwn', 'khaRtOum', 'StOckholm', 'tAipei', 'poRt of spain', 'tUnis', 'ashgabAt', 'funafUtI', 'washinGtOn d.c.', 'moNtEvideo', 'tAshkeNt', 'poRt vila', 'vAtIcan cItY'], "error creating funny case using letter t"
assert project.get_list_of_countries_whose_nth_letter_is(1, 'z') == ['Zambia', 'Zimbabwe'], "error creating countries whose letter 1 is z"
assert project.get_list_of_countries_whose_nth_letter_is(1, 'b') == ['Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi'], "error creating countries whose letter 1 is b"
assert project.get_list_of_countries_whose_nth_letter_is(3, 'c') == ['Nicaragua'], "error creating countries whose letter 3 is c"
assert project.get_list_of_countries_whose_nth_letter_is(3, 'e') == ['Azerbaijan', 'Czech Republic (Czechia)', 'Greece', 'Grenada', 'Iceland', 'Ireland', 'Liechtenstein', 'Sierra Leone', 'Sweden', 'Vietnam'], "error creating countries whose letter 3 is e"

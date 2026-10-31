# Smart GK - Marathi + English
# 100 GK questions | Python + Kivy | Pydroid 3

import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.clock import Clock

QUESTIONS = [
  [
    "भारताची राजधानी कोणती? / Capital of India?",
    [
      "मुंबई / Mumbai",
      "नवी दिल्ली / New Delhi",
      "पुणे / Pune",
      "चेन्नई / Chennai"
    ],
    1
  ],
  [
    "भारताचा राष्ट्रीय प्राणी कोणता? / National animal of India?",
    [
      "सिंह / Lion",
      "हत्ती / Elephant",
      "वाघ / Tiger",
      "बिबट्या / Leopard"
    ],
    2
  ],
  [
    "भारताचा राष्ट्रीय पक्षी कोणता? / National bird of India?",
    [
      "मोर / Peacock",
      "गरुड / Eagle",
      "पोपट / Parrot",
      "कावळा / Crow"
    ],
    0
  ],
  [
    "भारताचे राष्ट्रीय फूल कोणते? / National flower of India?",
    [
      "गुलाब / Rose",
      "कमळ / Lotus",
      "जाई / Jasmine",
      "सूर्यफूल / Sunflower"
    ],
    1
  ],
  [
    "भारताचा स्वातंत्र्यदिन कधी असतो? / Independence Day of India?",
    [
      "२६ जानेवारी / 26 January",
      "१५ ऑगस्ट / 15 August",
      "२ ऑक्टोबर / 2 October",
      "१४ नोव्हेंबर / 14 November"
    ],
    1
  ],
  [
    "भारताचा प्रजासत्ताक दिन कधी असतो? / Republic Day of India?",
    [
      "१५ ऑगस्ट / 15 August",
      "२६ जानेवारी / 26 January",
      "१ मे / 1 May",
      "५ सप्टेंबर / 5 September"
    ],
    1
  ],
  [
    "भारताचे चलन कोणते? / Currency of India?",
    [
      "डॉलर / Dollar",
      "रुपया / Rupee",
      "येन / Yen",
      "युरो / Euro"
    ],
    1
  ],
  [
    "भारताचे पहिले पंतप्रधान कोण होते? / First Prime Minister of India?",
    [
      "महात्मा गांधी / Mahatma Gandhi",
      "जवाहरलाल नेहरू / Jawaharlal Nehru",
      "सरदार पटेल / Sardar Patel",
      "डॉ. राजेंद्र प्रसाद / Dr. Rajendra Prasad"
    ],
    1
  ],
  [
    "भारताचे पहिले राष्ट्रपती कोण होते? / First President of India?",
    [
      "डॉ. राजेंद्र प्रसाद / Dr. Rajendra Prasad",
      "डॉ. ए. पी. जे. अब्दुल कलाम / Dr. A. P. J. Abdul Kalam",
      "डॉ. राधाकृष्णन / Dr. Radhakrishnan",
      "झाकीर हुसेन / Zakir Husain"
    ],
    0
  ],
  [
    "भारतीय संविधान कधी लागू झाले? / When did India's Constitution come into effect?",
    [
      "१५ ऑगस्ट १९४७ / 15 Aug 1947",
      "२६ जानेवारी १९५० / 26 Jan 1950",
      "२६ नोव्हेंबर १९४९ / 26 Nov 1949",
      "२ ऑक्टोबर १९५० / 2 Oct 1950"
    ],
    1
  ],
  [
    "भारताचे राष्ट्रीय गीत कोणते? / National song of India?",
    [
      "जन गण मन / Jana Gana Mana",
      "वंदे मातरम् / Vande Mataram",
      "सारे जहाँ से अच्छा / Sare Jahan Se Achha",
      "ऐ मेरे वतन / Ae Mere Watan"
    ],
    1
  ],
  [
    "भारताचे राष्ट्रगीत कोणते? / National anthem of India?",
    [
      "वंदे मातरम् / Vande Mataram",
      "जन गण मन / Jana Gana Mana",
      "विजयी विश्व तिरंगा / Vijayi Vishwa Tiranga",
      "सारे जहाँ से अच्छा / Sare Jahan Se Achha"
    ],
    1
  ],
  [
    "क्षेत्रफळानुसार भारतातील सर्वात मोठे राज्य कोणते? / Largest Indian state by area?",
    [
      "महाराष्ट्र / Maharashtra",
      "उत्तर प्रदेश / Uttar Pradesh",
      "राजस्थान / Rajasthan",
      "मध्य प्रदेश / Madhya Pradesh"
    ],
    2
  ],
  [
    "लोकसंख्येनुसार भारतातील सर्वात मोठे राज्य कोणते? / India's most populous state?",
    [
      "राजस्थान / Rajasthan",
      "उत्तर प्रदेश / Uttar Pradesh",
      "बिहार / Bihar",
      "गुजरात / Gujarat"
    ],
    1
  ],
  [
    "महाराष्ट्राची राजधानी कोणती? / Capital of Maharashtra?",
    [
      "नागपूर / Nagpur",
      "पुणे / Pune",
      "मुंबई / Mumbai",
      "नाशिक / Nashik"
    ],
    2
  ],
  [
    "भारताच्या संसदेत किती सभागृहे आहेत? / How many Houses are in India's Parliament?",
    [
      "एक / One",
      "दोन / Two",
      "तीन / Three",
      "चार / Four"
    ],
    1
  ],
  [
    "भारताचे सर्वोच्च न्यायालय कुठे आहे? / Where is India's Supreme Court?",
    [
      "मुंबई / Mumbai",
      "नवी दिल्ली / New Delhi",
      "कोलकाता / Kolkata",
      "चेन्नई / Chennai"
    ],
    1
  ],
  [
    "भारतीय संविधान मसुदा समितीचे अध्यक्ष कोण होते? / Who chaired the Constitution Drafting Committee?",
    [
      "डॉ. बी. आर. आंबेडकर / Dr. B. R. Ambedkar",
      "जवाहरलाल नेहरू / Jawaharlal Nehru",
      "राजेंद्र प्रसाद / Rajendra Prasad",
      "सरदार पटेल / Sardar Patel"
    ],
    0
  ],
  [
    "भारताचा राष्ट्रीय वृक्ष कोणता? / National tree of India?",
    [
      "आंबा / Mango",
      "वड / Banyan",
      "कडुलिंब / Neem",
      "पिंपळ / Peepal"
    ],
    1
  ],
  [
    "भारताचे पहिले उपराष्ट्रपती कोण होते? / First Vice-President of India?",
    [
      "डॉ. एस. राधाकृष्णन / Dr. S. Radhakrishnan",
      "डॉ. राजेंद्र प्रसाद / Dr. Rajendra Prasad",
      "व्ही. व्ही. गिरी / V. V. Giri",
      "झाकीर हुसेन / Zakir Husain"
    ],
    0
  ],
  [
    "जगातील सर्वात मोठा महासागर कोणता? / Largest ocean?",
    [
      "अटलांटिक / Atlantic",
      "हिंदी / Indian",
      "प्रशांत / Pacific",
      "आर्क्टिक / Arctic"
    ],
    2
  ],
  [
    "जगातील सर्वात मोठा खंड कोणता? / Largest continent?",
    [
      "आफ्रिका / Africa",
      "आशिया / Asia",
      "युरोप / Europe",
      "ऑस्ट्रेलिया / Australia"
    ],
    1
  ],
  [
    "जगातील सर्वात लहान खंड कोणता? / Smallest continent?",
    [
      "युरोप / Europe",
      "अंटार्क्टिका / Antarctica",
      "ऑस्ट्रेलिया / Australia",
      "दक्षिण अमेरिका / South America"
    ],
    2
  ],
  [
    "जपानची राजधानी कोणती? / Capital of Japan?",
    [
      "बीजिंग / Beijing",
      "टोकियो / Tokyo",
      "सोल / Seoul",
      "बँकॉक / Bangkok"
    ],
    1
  ],
  [
    "फ्रान्सची राजधानी कोणती? / Capital of France?",
    [
      "रोम / Rome",
      "माद्रिद / Madrid",
      "पॅरिस / Paris",
      "बर्लिन / Berlin"
    ],
    2
  ],
  [
    "इजिप्तमधून कोणती प्रसिद्ध नदी वाहते? / Famous river flowing through Egypt?",
    [
      "ॲमेझॉन / Amazon",
      "नाईल / Nile",
      "डॅन्यूब / Danube",
      "यांगत्से / Yangtze"
    ],
    1
  ],
  [
    "जगातील सर्वोच्च पर्वतशिखर कोणते? / Highest mountain peak?",
    [
      "K2",
      "कांचनजंगा / Kanchenjunga",
      "माउंट एव्हरेस्ट / Mount Everest",
      "मकालू / Makalu"
    ],
    2
  ],
  [
    "संयुक्त राष्ट्र संघाची स्थापना कोणत्या वर्षी झाली? / In which year was the UN founded?",
    [
      "१९१९ / 1919",
      "१९४५ / 1945",
      "१९५० / 1950",
      "१९६५ / 1965"
    ],
    1
  ],
  [
    "संयुक्त राष्ट्र संघाचे मुख्यालय कुठे आहे? / UN headquarters?",
    [
      "लंडन / London",
      "जिनेव्हा / Geneva",
      "न्यूयॉर्क / New York",
      "पॅरिस / Paris"
    ],
    2
  ],
  [
    "ऑस्ट्रेलियाची राजधानी कोणती? / Capital of Australia?",
    [
      "सिडनी / Sydney",
      "मेलबर्न / Melbourne",
      "कॅनबेरा / Canberra",
      "पर्थ / Perth"
    ],
    2
  ],
  [
    "ब्राझीलची राजधानी कोणती? / Capital of Brazil?",
    [
      "रिओ दि जानेरो / Rio de Janeiro",
      "ब्राझिलिया / Brasília",
      "साओ पाउलो / São Paulo",
      "लिमा / Lima"
    ],
    1
  ],
  [
    "सूर्यमालेतील सर्वात मोठा ग्रह कोणता? / Largest planet in the Solar System?",
    [
      "पृथ्वी / Earth",
      "शनी / Saturn",
      "गुरू / Jupiter",
      "मंगळ / Mars"
    ],
    2
  ],
  [
    "लाल ग्रह कोणता? / Which planet is called the Red Planet?",
    [
      "शुक्र / Venus",
      "मंगळ / Mars",
      "बुध / Mercury",
      "नेपच्यून / Neptune"
    ],
    1
  ],
  [
    "पृथ्वीचा नैसर्गिक उपग्रह कोणता? / Earth's natural satellite?",
    [
      "सूर्य / Sun",
      "चंद्र / Moon",
      "मंगळ / Mars",
      "टायटन / Titan"
    ],
    1
  ],
  [
    "जगातील सर्वात मोठे उष्ण वाळवंट कोणते? / Largest hot desert?",
    [
      "गोबी / Gobi",
      "सहारा / Sahara",
      "थार / Thar",
      "कालाहारी / Kalahari"
    ],
    1
  ],
  [
    "पिरॅमिडसाठी कोणता देश प्रसिद्ध आहे? / Which country is famous for pyramids?",
    [
      "ग्रीस / Greece",
      "इजिप्त / Egypt",
      "मेक्सिको / Mexico",
      "इराक / Iraq"
    ],
    1
  ],
  [
    "ग्रेट वॉल कोणत्या देशात आहे? / Great Wall is in which country?",
    [
      "भारत / India",
      "चीन / China",
      "जपान / Japan",
      "मंगोलिया / Mongolia"
    ],
    1
  ],
  [
    "जगातील सर्वात मोठे बेट कोणते? / Largest island?",
    [
      "मादागास्कर / Madagascar",
      "ग्रीनलँड / Greenland",
      "बोर्निओ / Borneo",
      "न्यू गिनी / New Guinea"
    ],
    1
  ],
  [
    "कॅनडाची राजधानी कोणती? / Capital of Canada?",
    [
      "टोरोंटो / Toronto",
      "व्हँकुव्हर / Vancouver",
      "ओटावा / Ottawa",
      "मॉन्ट्रियल / Montreal"
    ],
    2
  ],
  [
    "दक्षिण आफ्रिकेची प्रशासकीय राजधानी कोणती? / Executive capital of South Africa?",
    [
      "केपटाउन / Cape Town",
      "प्रिटोरिया / Pretoria",
      "डर्बन / Durban",
      "जोहान्सबर्ग / Johannesburg"
    ],
    1
  ],
  [
    "पाण्याचे रासायनिक सूत्र काय? / Chemical formula of water?",
    [
      "CO2",
      "H2O",
      "O2",
      "NaCl"
    ],
    1
  ],
  [
    "मानवी शरीरातील सर्वात मोठा अवयव कोणता? / Largest organ of human body?",
    [
      "हृदय / Heart",
      "यकृत / Liver",
      "त्वचा / Skin",
      "फुफ्फुस / Lung"
    ],
    2
  ],
  [
    "रक्ताचा लाल रंग कशामुळे असतो? / What makes blood red?",
    [
      "क्लोरोफिल / Chlorophyll",
      "हिमोग्लोबिन / Hemoglobin",
      "प्लाझ्मा / Plasma",
      "कॅल्शियम / Calcium"
    ],
    1
  ],
  [
    "वनस्पती अन्न तयार करण्याच्या प्रक्रियेला काय म्हणतात? / Process by which plants make food?",
    [
      "श्वसन / Respiration",
      "प्रकाशसंश्लेषण / Photosynthesis",
      "बाष्पीभवन / Evaporation",
      "पचन / Digestion"
    ],
    1
  ],
  [
    "सूर्यप्रकाशामुळे शरीरात कोणते जीवनसत्त्व तयार होण्यास मदत होते? / Sunlight helps the body make which vitamin?",
    [
      "Vitamin A",
      "Vitamin B12",
      "Vitamin C",
      "Vitamin D"
    ],
    3
  ],
  [
    "मानवी हृदयात किती कप्पे असतात? / How many chambers does the human heart have?",
    [
      "दोन / Two",
      "तीन / Three",
      "चार / Four",
      "पाच / Five"
    ],
    2
  ],
  [
    "पाण्याचा गोठणबिंदू किती °C आहे? / Freezing point of water?",
    [
      "०°C / 0°C",
      "१०°C / 10°C",
      "५०°C / 50°C",
      "१००°C / 100°C"
    ],
    0
  ],
  [
    "समुद्रसपाटीवर पाण्याचा उकळबिंदू किती °C असतो? / Boiling point of water at sea level?",
    [
      "५०°C / 50°C",
      "७५°C / 75°C",
      "१००°C / 100°C",
      "१२०°C / 120°C"
    ],
    2
  ],
  [
    "बलाचे SI एकक कोणते? / SI unit of force?",
    [
      "जूल / Joule",
      "न्यूटन / Newton",
      "वॅट / Watt",
      "पास्कल / Pascal"
    ],
    1
  ],
  [
    "विद्युत प्रवाहाचे SI एकक कोणते? / SI unit of electric current?",
    [
      "व्होल्ट / Volt",
      "ओहम / Ohm",
      "अँपिअर / Ampere",
      "वॅट / Watt"
    ],
    2
  ],
  [
    "ध्वनी कोणत्या माध्यमातून प्रवास करू शकत नाही? / Sound cannot travel through which medium?",
    [
      "पाणी / Water",
      "हवा / Air",
      "घन पदार्थ / Solids",
      "निर्वात / Vacuum"
    ],
    3
  ],
  [
    "मानवी शरीरात रक्त पंप करणारा अवयव कोणता? / Which organ pumps blood?",
    [
      "मेंदू / Brain",
      "हृदय / Heart",
      "मूत्रपिंड / Kidney",
      "पोट / Stomach"
    ],
    1
  ],
  [
    "श्वसनासाठी आवश्यक वायू कोणता? / Gas needed for respiration?",
    [
      "नायट्रोजन / Nitrogen",
      "ऑक्सिजन / Oxygen",
      "कार्बन डायऑक्साइड / Carbon dioxide",
      "हायड्रोजन / Hydrogen"
    ],
    1
  ],
  [
    "हवेत सर्वाधिक प्रमाणात कोणता वायू असतो? / Most abundant gas in air?",
    [
      "ऑक्सिजन / Oxygen",
      "कार्बन डायऑक्साइड / Carbon dioxide",
      "नायट्रोजन / Nitrogen",
      "हायड्रोजन / Hydrogen"
    ],
    2
  ],
  [
    "अणूच्या केंद्रकात कोणते कण असतात? / Which particles are in an atom's nucleus?",
    [
      "फक्त इलेक्ट्रॉन / Electrons only",
      "प्रोटॉन व न्यूट्रॉन / Protons and neutrons",
      "फक्त न्यूट्रॉन / Neutrons only",
      "फोटॉन / Photons"
    ],
    1
  ],
  [
    "मानवी शरीराचे सामान्य तापमान साधारण किती °C असते? / Approximate normal body temperature?",
    [
      "२७°C / 27°C",
      "३७°C / 37°C",
      "४२°C / 42°C",
      "५०°C / 50°C"
    ],
    1
  ],
  [
    "प्रकाशाचा वेग सर्वाधिक कोणत्या माध्यमात असतो? / Light travels fastest in which medium?",
    [
      "पाणी / Water",
      "काच / Glass",
      "निर्वात / Vacuum",
      "हवा / Air"
    ],
    2
  ],
  [
    "पृथ्वी सूर्याभोवती एक फेरी साधारण किती दिवसांत पूर्ण करते? / Approximate time Earth takes to orbit the Sun?",
    [
      "२४ तास / 24 hours",
      "३० दिवस / 30 days",
      "३६५.२५ दिवस / 365.25 days",
      "१०० दिवस / 100 days"
    ],
    2
  ],
  [
    "लिंबामध्ये मुख्यतः कोणते आम्ल असते? / Main acid in lemon?",
    [
      "लॅक्टिक आम्ल / Lactic acid",
      "सिट्रिक आम्ल / Citric acid",
      "अॅसिटिक आम्ल / Acetic acid",
      "सल्फ्युरिक आम्ल / Sulfuric acid"
    ],
    1
  ],
  [
    "पेशीचे नियंत्रण केंद्र कोणते? / Control center of a cell?",
    [
      "पेशीभित्तिका / Cell wall",
      "केंद्रक / Nucleus",
      "सायटोप्लाझम / Cytoplasm",
      "रिक्तिका / Vacuole"
    ],
    1
  ],
  [
    "छत्रपती शिवाजी महाराजांचा जन्म कोणत्या किल्ल्यावर झाला? / At which fort was Shivaji Maharaj born?",
    [
      "रायगड / Raigad",
      "शिवनेरी / Shivneri",
      "प्रतापगड / Pratapgad",
      "सिंहगड / Sinhagad"
    ],
    1
  ],
  [
    "छत्रपती शिवाजी महाराजांचा राज्याभिषेक कोणत्या वर्षी झाला? / In which year was Shivaji Maharaj crowned?",
    [
      "१६४५ / 1645",
      "१६७४ / 1674",
      "१६८० / 1680",
      "१७०७ / 1707"
    ],
    1
  ],
  [
    "भारत छोडो आंदोलन कोणत्या वर्षी सुरू झाले? / Quit India Movement began in which year?",
    [
      "१९१९ / 1919",
      "१९३० / 1930",
      "१९४२ / 1942",
      "१९४७ / 1947"
    ],
    2
  ],
  [
    "दांडी मार्च कोणत्या वर्षी झाला? / Dandi March took place in which year?",
    [
      "१९२० / 1920",
      "१९३० / 1930",
      "१९४२ / 1942",
      "१९४६ / 1946"
    ],
    1
  ],
  [
    "जालियनवाला बाग हत्याकांड कोणत्या वर्षी झाले? / Jallianwala Bagh massacre occurred in which year?",
    [
      "१९०५ / 1905",
      "१९१९ / 1919",
      "१९२८ / 1928",
      "१९४२ / 1942"
    ],
    1
  ],
  [
    "भारतीय राष्ट्रीय काँग्रेसची स्थापना कोणत्या वर्षी झाली? / Indian National Congress was founded in which year?",
    [
      "१८५७ / 1857",
      "१८८५ / 1885",
      "१९०५ / 1905",
      "१९२० / 1920"
    ],
    1
  ],
  [
    "'स्वराज्य हा माझा जन्मसिद्ध हक्क आहे' असे कोणी म्हटले? / Who said 'Swaraj is my birthright'?",
    [
      "महात्मा गांधी / Mahatma Gandhi",
      "लोकमान्य टिळक / Lokmanya Tilak",
      "नेहरू / Nehru",
      "सुभाषचंद्र बोस / Subhas Chandra Bose"
    ],
    1
  ],
  [
    "आझाद हिंद सेनेशी कोणाचे नाव जोडलेले आहे? / Who is associated with Azad Hind Fauj?",
    [
      "भगतसिंग / Bhagat Singh",
      "सुभाषचंद्र बोस / Subhas Chandra Bose",
      "लाला लजपतराय / Lala Lajpat Rai",
      "गोखले / Gokhale"
    ],
    1
  ],
  [
    "'महात्मा' म्हणून कोण ओळखले जातात? / Who is popularly known as Mahatma?",
    [
      "जवाहरलाल नेहरू / Jawaharlal Nehru",
      "मोहनदास गांधी / Mohandas Gandhi",
      "सरदार पटेल / Sardar Patel",
      "रवींद्रनाथ टागोर / Rabindranath Tagore"
    ],
    1
  ],
  [
    "भारताला स्वातंत्र्य कोणत्या वर्षी मिळाले? / India gained independence in which year?",
    [
      "१९४२ / 1942",
      "१९४५ / 1945",
      "१९४७ / 1947",
      "१९५० / 1950"
    ],
    2
  ],
  [
    "पहिले पानिपतचे युद्ध कोणत्या वर्षी झाले? / First Battle of Panipat was fought in which year?",
    [
      "१५२६ / 1526",
      "१५५६ / 1556",
      "१७६१ / 1761",
      "१७५७ / 1757"
    ],
    0
  ],
  [
    "प्लासीची लढाई कोणत्या वर्षी झाली? / Battle of Plassey took place in which year?",
    [
      "१७५७ / 1757",
      "१७६४ / 1764",
      "१८५७ / 1857",
      "१७०७ / 1707"
    ],
    0
  ],
  [
    "सम्राट अशोक कोणत्या राजवंशातील होता? / Emperor Ashoka belonged to which dynasty?",
    [
      "गुप्त / Gupta",
      "मौर्य / Maurya",
      "मुघल / Mughal",
      "चोल / Chola"
    ],
    1
  ],
  [
    "ताजमहाल कोणी बांधला? / Who commissioned the Taj Mahal?",
    [
      "अकबर / Akbar",
      "शाहजहान / Shah Jahan",
      "जहांगीर / Jahangir",
      "औरंगजेब / Aurangzeb"
    ],
    1
  ],
  [
    "कुतुबमिनार कुठे आहे? / Where is Qutub Minar located?",
    [
      "आग्रा / Agra",
      "दिल्ली / Delhi",
      "जयपूर / Jaipur",
      "लखनौ / Lucknow"
    ],
    1
  ],
  [
    "अजिंठा लेणी कोणत्या राज्यात आहेत? / Ajanta Caves are in which state?",
    [
      "गुजरात / Gujarat",
      "महाराष्ट्र / Maharashtra",
      "मध्य प्रदेश / Madhya Pradesh",
      "कर्नाटक / Karnataka"
    ],
    1
  ],
  [
    "भारतीय संविधान सभेचे अध्यक्ष कोण होते? / Who was President of the Constituent Assembly?",
    [
      "डॉ. राजेंद्र प्रसाद / Dr. Rajendra Prasad",
      "डॉ. आंबेडकर / Dr. Ambedkar",
      "नेहरू / Nehru",
      "सरदार पटेल / Sardar Patel"
    ],
    0
  ],
  [
    "'गीतांजली' या पुस्तकाचे लेखक कोण? / Who wrote Gitanjali?",
    [
      "बंकिमचंद्र चट्टोपाध्याय / Bankim Chandra",
      "रवींद्रनाथ टागोर / Rabindranath Tagore",
      "प्रेमचंद / Premchand",
      "सरोजिनी नायडू / Sarojini Naidu"
    ],
    1
  ],
  [
    "ISRO ची स्थापना कोणत्या वर्षी झाली? / In which year was ISRO established?",
    [
      "१९४७ / 1947",
      "१९६९ / 1969",
      "१९७५ / 1975",
      "१९८४ / 1984"
    ],
    1
  ],
  [
    "सत्यशोधक समाजाची स्थापना कोणी केली? / Who founded the Satyashodhak Samaj?",
    [
      "महात्मा फुले / Mahatma Phule",
      "डॉ. आंबेडकर / Dr. Ambedkar",
      "लोकमान्य टिळक / Lokmanya Tilak",
      "गोपाळ गणेश आगरकर / G. G. Agarkar"
    ],
    0
  ],
  [
    "मालिका पूर्ण करा: २, ४, ६, ८, __ / Complete: 2, 4, 6, 8, __",
    [
      "९ / 9",
      "१० / 10",
      "११ / 11",
      "१२ / 12"
    ],
    1
  ],
  [
    "मालिका पूर्ण करा: ५, १०, १५, २०, __ / Complete: 5, 10, 15, 20, __",
    [
      "२२ / 22",
      "२५ / 25",
      "३० / 30",
      "३५ / 35"
    ],
    1
  ],
  [
    "वेगळा शब्द ओळखा: सफरचंद, आंबा, गाजर, केळी / Odd one: Apple, Mango, Carrot, Banana",
    [
      "सफरचंद / Apple",
      "आंबा / Mango",
      "गाजर / Carrot",
      "केळी / Banana"
    ],
    2
  ],
  [
    "एका आठवड्यात किती दिवस असतात? / How many days are in a week?",
    [
      "५ / 5",
      "६ / 6",
      "७ / 7",
      "८ / 8"
    ],
    2
  ],
  [
    "एका तासात किती मिनिटे असतात? / How many minutes are in an hour?",
    [
      "३० / 30",
      "४५ / 45",
      "६० / 60",
      "९० / 90"
    ],
    2
  ],
  [
    "१२ चा दुप्पट किती? / Double of 12?",
    [
      "१८ / 18",
      "२० / 20",
      "२४ / 24",
      "२६ / 26"
    ],
    2
  ],
  [
    "१०० मधून २५ वजा केल्यास किती? / What is 100 minus 25?",
    [
      "६५ / 65",
      "७० / 70",
      "७५ / 75",
      "८५ / 85"
    ],
    2
  ],
  [
    "३, ६, ९, १२, __ पुढील संख्या कोणती? / Next number: 3, 6, 9, 12, __",
    [
      "१३ / 13",
      "१४ / 14",
      "१५ / 15",
      "१८ / 18"
    ],
    2
  ],
  [
    "आज सोमवार असेल तर दोन दिवसांनी कोणता वार? / If today is Monday, what day in two days?",
    [
      "मंगळवार / Tuesday",
      "बुधवार / Wednesday",
      "गुरुवार / Thursday",
      "शुक्रवार / Friday"
    ],
    1
  ],
  [
    "एका डझनमध्ये किती वस्तू असतात? / How many items in a dozen?",
    [
      "१० / 10",
      "१२ / 12",
      "१५ / 15",
      "२० / 20"
    ],
    1
  ],
  [
    "वेगळा आकार कोणता: त्रिकोण, चौकोन, वर्तुळ, आंबा? / Odd one: Triangle, Square, Circle, Mango",
    [
      "त्रिकोण / Triangle",
      "चौकोन / Square",
      "वर्तुळ / Circle",
      "आंबा / Mango"
    ],
    3
  ],
  [
    "जर A=1, B=2, तर D किती? / If A=1 and B=2, what is D?",
    [
      "३ / 3",
      "४ / 4",
      "५ / 5",
      "६ / 6"
    ],
    1
  ],
  [
    "२० चा अर्धा किती? / Half of 20?",
    [
      "५ / 5",
      "१० / 10",
      "१५ / 15",
      "२० / 20"
    ],
    1
  ],
  [
    "२, ४, ८, १६, __ पुढील संख्या कोणती? / Next number: 2, 4, 8, 16, __",
    [
      "१८ / 18",
      "२४ / 24",
      "३० / 30",
      "३२ / 32"
    ],
    3
  ],
  [
    "एका त्रिकोणाला किती बाजू असतात? / How many sides does a triangle have?",
    [
      "२ / 2",
      "३ / 3",
      "४ / 4",
      "५ / 5"
    ],
    1
  ],
  [
    "एका वर्षात किती महिने असतात? / How many months are in a year?",
    [
      "१० / 10",
      "११ / 11",
      "१२ / 12",
      "१३ / 13"
    ],
    2
  ],
  [
    "८ + ७ × २ = किती? / What is 8 + 7 × 2?",
    [
      "३० / 30",
      "२२ / 22",
      "२४ / 24",
      "२८ / 28"
    ],
    1
  ],
  [
    "वेगळा अंक ओळखा: २, ४, ६, ९, ८ / Find the odd number: 2, 4, 6, 9, 8",
    [
      "२ / 2",
      "४ / 4",
      "९ / 9",
      "८ / 8"
    ],
    2
  ],
  [
    "एका चौकोनाला किती कोन असतात? / How many angles does a square have?",
    [
      "२ / 2",
      "३ / 3",
      "४ / 4",
      "५ / 5"
    ],
    2
  ],
  [
    "मालिका पूर्ण करा: १, ४, ९, १६, __ / Complete: 1, 4, 9, 16, __",
    [
      "२० / 20",
      "२५ / 25",
      "३० / 30",
      "३६ / 36"
    ],
    1
  ]
]

class SmartGK(App):
    def build(self):
        from kivy.core.window import Window
        from kivy.graphics import Color, Rectangle
        Window.clearcolor = (0.94, 0.97, 1, 1)  # pale blue background
        self.title = "Smart GK"
        self.questions = QUESTIONS[:]
        random.shuffle(self.questions)
        self.index = 0
        self.score = 0
        self.timer_seconds = 15
        self.timer_event = None
        self.answer_locked = False
        self.root_box = BoxLayout(orientation="vertical", padding=dp(18), spacing=dp(12))
        with self.root_box.canvas.before:
            Color(0.94, 0.97, 1, 1)
            self.bg_rect = Rectangle(pos=self.root_box.pos, size=self.root_box.size)
        self.root_box.bind(pos=self._update_bg, size=self._update_bg)
        self.show_home()
        return self.root_box

    def _update_bg(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def clear(self):
        self.root_box.clear_widgets()

    def label(self, text, size=20, height=dp(120), color=(0.08, 0.18, 0.34, 1)):
        item = Label(text=text, font_size=dp(size), color=color,
                     bold=True, halign="center", valign="middle",
                     size_hint_y=None, height=height)
        item.bind(size=lambda obj, value: setattr(obj, "text_size", value))
        self.root_box.add_widget(item)

    def button(self, text, callback, height=dp(58), primary=False):
        bg = (0.08, 0.35, 0.78, 1) if primary else (0.82, 0.90, 1, 1)
        fg = (1, 1, 1, 1) if primary else (0.05, 0.20, 0.43, 1)
        item = Button(text=text, font_size=dp(17), bold=True,
                      color=fg, background_normal="", background_down="",
                      background_color=bg, size_hint_y=None, height=height)
        item.bind(on_press=callback)
        self.root_box.add_widget(item)

    def show_home(self):
        self.clear()
        self.label("SMART GK", 36, dp(110), (0.04, 0.25, 0.58, 1))
        self.label("Learn • Practice • Improve", 17, dp(45), (0.25, 0.38, 0.55, 1))
        self.label("मराठी + English\nएकूण प्रश्न: 100", 22, dp(130))
        self.button("START QUIZ  |  प्रश्नमंजुषा सुरू करा", self.start_quiz, dp(66), True)
        self.label("ज्ञान वाढवा, आत्मविश्वास जिंका!", 16, dp(70), (0.25, 0.38, 0.55, 1))

    def start_quiz(self, instance):
        self.index = 0
        self.score = 0
        self.questions = QUESTIONS[:]
        random.shuffle(self.questions)
        self.show_question()

    def stop_timer(self):
        if self.timer_event is not None:
            self.timer_event.cancel()
            self.timer_event = None

    def show_question(self):
        self.stop_timer()
        self.answer_locked = False
        self.timer_seconds = 15
        self.clear()
        q, options, answer = self.questions[self.index]
        self.label("SMART GK  •  QUIZ", 18, dp(42), (0.04, 0.25, 0.58, 1))
        self.label("प्रश्न / Question " + str(self.index + 1) + " / 100", 18, dp(48))
        self.timer_label = Label(
            text="वेळ / Time: 15 सेकंद",
            font_size=dp(20), bold=True,
            color=(0.78, 0.12, 0.12, 1),
            size_hint_y=None, height=dp(48)
        )
        self.root_box.add_widget(self.timer_label)
        self.label(q, 20, dp(130))
        for i, option in enumerate(options):
            self.button(option, lambda btn, choice=i: self.check_answer(choice), dp(58))
        self.label("गुण / Score: " + str(self.score), 17, dp(48), (0.04, 0.25, 0.58, 1))
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        if self.answer_locked:
            return False
        self.timer_seconds -= 1
        if self.timer_seconds <= 0:
            self.timer_label.text = "वेळ संपली! / Time's up!"
            self.answer_locked = True
            self.stop_timer()
            self.show_answer_result(timed_out=True)
            return False
        self.timer_label.text = "वेळ / Time: " + str(self.timer_seconds) + " सेकंद"
        return True

    def check_answer(self, choice):
        if self.answer_locked:
            return
        self.answer_locked = True
        self.stop_timer()
        self.show_answer_result(choice=choice)

    def show_answer_result(self, choice=None, timed_out=False):
        q, options, answer = self.questions[self.index]
        self.clear()
        if timed_out:
            self.label("वेळ संपली! / Time's up!", 25, dp(90), (0.78, 0.12, 0.12, 1))
            self.label("योग्य उत्तर / Correct answer:\n" + options[answer], 19, dp(110))
        elif choice == answer:
            self.score += 10
            self.label("बरोबर! / Correct! +10", 25, dp(100), (0.05, 0.55, 0.28, 1))
        else:
            self.label("चुकीचे / Incorrect", 25, dp(85), (0.78, 0.12, 0.12, 1))
            self.label("योग्य उत्तर / Correct answer:\n" + options[answer], 19, dp(110))
        self.label("सध्याचे गुण / Current score: " + str(self.score), 18, dp(70))
        self.button("NEXT  |  पुढचा प्रश्न", self.next_question, dp(62), True)

    def next_question(self, instance):
        self.index += 1
        if self.index < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.stop_timer()
        self.clear()
        self.label("QUIZ COMPLETED!\nअभिनंदन!", 29, dp(130), (0.04, 0.25, 0.58, 1))
        self.label("तुझे गुण / Your score:\n" + str(self.score) + " / 1000", 25, dp(140))
        self.button("PLAY AGAIN  |  पुन्हा खेळा", self.start_quiz, dp(62), True)
        self.button("HOME  |  मुख्य पान", self.go_home, dp(58))

    def go_home(self, instance):
        self.stop_timer()
        self.show_home()

SmartGK().run()

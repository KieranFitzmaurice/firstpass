# User defined module to store options for charfield choices

def country_options():
    choices = [('Afghanistan','Afghanistan'),
    ('Åland Islands','Åland Islands'),
    ('Albania','Albania'),
    ('Algeria','Algeria'),
    ('American Samoa','American Samoa'),
    ('Andorra','Andorra'),
    ('Angola','Angola'),
    ('Anguilla','Anguilla'),
    ('Antarctica','Antarctica'),
    ('Antigua and Barbuda','Antigua and Barbuda'),
    ('Argentina','Argentina'),
    ('Armenia','Armenia'),
    ('Aruba','Aruba'),
    ('Australia','Australia'),
    ('Austria','Austria'),
    ('Azerbaijan','Azerbaijan'),
    ('Bahamas','Bahamas'),
    ('Bahrain','Bahrain'),
    ('Bangladesh','Bangladesh'),
    ('Barbados','Barbados'),
    ('Belarus','Belarus'),
    ('Belgium','Belgium'),
    ('Belize','Belize'),
    ('Benin','Benin'),
    ('Bermuda','Bermuda'),
    ('Bhutan','Bhutan'),
    ('Bolivia','Bolivia'),
    ('Bosnia and Herzegovina','Bosnia and Herzegovina'),
    ('Botswana','Botswana'),
    ('Bouvet Island','Bouvet Island'),
    ('Brazil','Brazil'),
    ('British Indian Ocean Territory','British Indian Ocean Territory'),
    ('Brunei Darussalam','Brunei Darussalam'),
    ('Bulgaria','Bulgaria'),
    ('Burkina Faso','Burkina Faso'),
    ('Burundi','Burundi'),
    ('Cambodia','Cambodia'),
    ('Cameroon','Cameroon'),
    ('Canada','Canada'),
    ('Cape Verde','Cape Verde'),
    ('Caribbean Netherlands ','Caribbean Netherlands '),
    ('Cayman Islands','Cayman Islands'),
    ('Central African Republic','Central African Republic'),
    ('Chad','Chad'),
    ('Chile','Chile'),
    ('China','China'),
    ('Christmas Island','Christmas Island'),
    ('Cocos (Keeling) Islands','Cocos (Keeling) Islands'),
    ('Colombia','Colombia'),
    ('Comoros','Comoros'),
    ('Congo','Congo'),
    ('Congo, Democratic Republic of','Congo, Democratic Republic of'),
    ('Cook Islands','Cook Islands'),
    ('Costa Rica','Costa Rica'),
    ('Côte d\'Ivoire','Côte d\'Ivoire'),
    ('Croatia','Croatia'),
    ('Cuba','Cuba'),
    ('Curaçao','Curaçao'),
    ('Cyprus','Cyprus'),
    ('Czech Republic','Czech Republic'),
    ('Denmark','Denmark'),
    ('Djibouti','Djibouti'),
    ('Dominica','Dominica'),
    ('Dominican Republic','Dominican Republic'),
    ('Ecuador','Ecuador'),
    ('Egypt','Egypt'),
    ('El Salvador','El Salvador'),
    ('Equatorial Guinea','Equatorial Guinea'),
    ('Eritrea','Eritrea'),
    ('Estonia','Estonia'),
    ('Ethiopia','Ethiopia'),
    ('Falkland Islands','Falkland Islands'),
    ('Faroe Islands','Faroe Islands'),
    ('Fiji','Fiji'),
    ('Finland','Finland'),
    ('France','France'),
    ('French Guiana','French Guiana'),
    ('French Polynesia','French Polynesia'),
    ('French Southern Territories','French Southern Territories'),
    ('Gabon','Gabon'),
    ('Gambia','Gambia'),
    ('Georgia','Georgia'),
    ('Germany','Germany'),
    ('Ghana','Ghana'),
    ('Gibraltar','Gibraltar'),
    ('Greece','Greece'),
    ('Greenland','Greenland'),
    ('Grenada','Grenada'),
    ('Guadeloupe','Guadeloupe'),
    ('Guam','Guam'),
    ('Guatemala','Guatemala'),
    ('Guernsey','Guernsey'),
    ('Guinea','Guinea'),
    ('Guinea-Bissau','Guinea-Bissau'),
    ('Guyana','Guyana'),
    ('Haiti','Haiti'),
    ('Heard and McDonald Islands','Heard and McDonald Islands'),
    ('Honduras','Honduras'),
    ('Hong Kong','Hong Kong'),
    ('Hungary','Hungary'),
    ('Iceland','Iceland'),
    ('India','India'),
    ('Indonesia','Indonesia'),
    ('Iran','Iran'),
    ('Iraq','Iraq'),
    ('Ireland','Ireland'),
    ('Isle of Man','Isle of Man'),
    ('Israel','Israel'),
    ('Italy','Italy'),
    ('Jamaica','Jamaica'),
    ('Japan','Japan'),
    ('Jersey','Jersey'),
    ('Jordan','Jordan'),
    ('Kazakhstan','Kazakhstan'),
    ('Kenya','Kenya'),
    ('Kiribati','Kiribati'),
    ('Kuwait','Kuwait'),
    ('Kyrgyzstan','Kyrgyzstan'),
    ('Lao People\'s Democratic Republic','Lao People\'s Democratic Republic'),
    ('Latvia','Latvia'),
    ('Lebanon','Lebanon'),
    ('Lesotho','Lesotho'),
    ('Liberia','Liberia'),
    ('Libya','Libya'),
    ('Liechtenstein','Liechtenstein'),
    ('Lithuania','Lithuania'),
    ('Luxembourg','Luxembourg'),
    ('Macau','Macau'),
    ('Macedonia','Macedonia'),
    ('Madagascar','Madagascar'),
    ('Malawi','Malawi'),
    ('Malaysia','Malaysia'),
    ('Maldives','Maldives'),
    ('Mali','Mali'),
    ('Malta','Malta'),
    ('Marshall Islands','Marshall Islands'),
    ('Martinique','Martinique'),
    ('Mauritania','Mauritania'),
    ('Mauritius','Mauritius'),
    ('Mayotte','Mayotte'),
    ('Mexico','Mexico'),
    ('Micronesia, Federated States of','Micronesia, Federated States of'),
    ('Moldova','Moldova'),
    ('Monaco','Monaco'),
    ('Mongolia','Mongolia'),
    ('Montenegro','Montenegro'),
    ('Montserrat','Montserrat'),
    ('Morocco','Morocco'),
    ('Mozambique','Mozambique'),
    ('Myanmar','Myanmar'),
    ('Namibia','Namibia'),
    ('Nauru','Nauru'),
    ('Nepal','Nepal'),
    ('New Caledonia','New Caledonia'),
    ('New Zealand','New Zealand'),
    ('Nicaragua','Nicaragua'),
    ('Niger','Niger'),
    ('Nigeria','Nigeria'),
    ('Niue','Niue'),
    ('Norfolk Island','Norfolk Island'),
    ('North Korea','North Korea'),
    ('Northern Mariana Islands','Northern Mariana Islands'),
    ('Norway','Norway'),
    ('Oman','Oman'),
    ('Pakistan','Pakistan'),
    ('Palau','Palau'),
    ('Palestine, State of','Palestine, State of'),
    ('Panama','Panama'),
    ('Papua New Guinea','Papua New Guinea'),
    ('Paraguay','Paraguay'),
    ('Peru','Peru'),
    ('Philippines','Philippines'),
    ('Pitcairn','Pitcairn'),
    ('Poland','Poland'),
    ('Portugal','Portugal'),
    ('Puerto Rico','Puerto Rico'),
    ('Qatar','Qatar'),
    ('Réunion','Réunion'),
    ('Romania','Romania'),
    ('Russian Federation','Russian Federation'),
    ('Rwanda','Rwanda'),
    ('Saint-Martin (France)','Saint-Martin (France)'),
    ('Saint Barthélemy','Saint Barthélemy'),
    ('Saint Helena','Saint Helena'),
    ('Saint Kitts and Nevis','Saint Kitts and Nevis'),
    ('Saint Lucia','Saint Lucia'),
    ('Saint Vincent and the Grenadines','Saint Vincent and the Grenadines'),
    ('Samoa','Samoa'),
    ('San Marino','San Marino'),
    ('Sao Tome and Principe','Sao Tome and Principe'),
    ('Saudi Arabia','Saudi Arabia'),
    ('Senegal','Senegal'),
    ('Serbia','Serbia'),
    ('Seychelles','Seychelles'),
    ('Sierra Leone','Sierra Leone'),
    ('Singapore','Singapore'),
    ('Sint Maarten (Dutch part)','Sint Maarten (Dutch part)'),
    ('Slovakia','Slovakia'),
    ('Slovenia','Slovenia'),
    ('Solomon Islands','Solomon Islands'),
    ('Somalia','Somalia'),
    ('South Africa','South Africa'),
    ('South Georgia and the South Sandwich Islands','South Georgia and the South Sandwich Islands'),
    ('South Korea','South Korea'),
    ('South Sudan','South Sudan'),
    ('Spain','Spain'),
    ('Sri Lanka','Sri Lanka'),
    ('St. Pierre and Miquelon','St. Pierre and Miquelon'),
    ('Sudan','Sudan'),
    ('Suriname','Suriname'),
    ('Svalbard and Jan Mayen Islands','Svalbard and Jan Mayen Islands'),
    ('Swaziland','Swaziland'),
    ('Sweden','Sweden'),
    ('Switzerland','Switzerland'),
    ('Syria','Syria'),
    ('Taiwan','Taiwan'),
    ('Tajikistan','Tajikistan'),
    ('Tanzania','Tanzania'),
    ('Thailand','Thailand'),
    ('The Netherlands','The Netherlands'),
    ('Timor-Leste','Timor-Leste'),
    ('Togo','Togo'),
    ('Tokelau','Tokelau'),
    ('Tonga','Tonga'),
    ('Trinidad and Tobago','Trinidad and Tobago'),
    ('Tunisia','Tunisia'),
    ('Turkey','Turkey'),
    ('Turkmenistan','Turkmenistan'),
    ('Turks and Caicos Islands','Turks and Caicos Islands'),
    ('Tuvalu','Tuvalu'),
    ('Uganda','Uganda'),
    ('Ukraine','Ukraine'),
    ('United Arab Emirates','United Arab Emirates'),
    ('United Kingdom','United Kingdom'),
    ('United States','United States'),
    ('United States Minor Outlying Islands','United States Minor Outlying Islands'),
    ('Uruguay','Uruguay'),
    ('Uzbekistan','Uzbekistan'),
    ('Vanuatu','Vanuatu'),
    ('Vatican','Vatican'),
    ('Venezuela','Venezuela'),
    ('Vietnam','Vietnam'),
    ('Virgin Islands (British)','Virgin Islands (British)'),
    ('Virgin Islands (U.S.)','Virgin Islands (U.S.)'),
    ('Wallis and Futuna Islands','Wallis and Futuna Islands'),
    ('Western Sahara','Western Sahara'),
    ('Yemen','Yemen'),
    ('Zambia','Zambia'),
    ('Zimbabwe','Zimbabwe')]
    return choices

def get_short_code(country_name):
    code_dict = {'Afghanistan':'af',
    'Åland Islands':'ax',
    'Albania':'al',
    'Algeria':'dz',
    'American Samoa':'as',
    'Andorra':'ad',
    'Angola':'ao',
    'Anguilla':'ai',
    'Antarctica':'aq',
    'Antigua and Barbuda':'ag',
    'Argentina':'ar',
    'Armenia':'am',
    'Aruba':'aw',
    'Australia':'au',
    'Austria':'at',
    'Azerbaijan':'az',
    'Bahamas':'bs',
    'Bahrain':'bh',
    'Bangladesh':'bd',
    'Barbados':'bb',
    'Belarus':'by',
    'Belgium':'be',
    'Belize':'bz',
    'Benin':'bj',
    'Bermuda':'bm',
    'Bhutan':'bt',
    'Bolivia':'bo',
    'Bosnia and Herzegovina':'ba',
    'Botswana':'bw',
    'Bouvet Island':'bv',
    'Brazil':'br',
    'British Indian Ocean Territory':'io',
    'Brunei Darussalam':'bn',
    'Bulgaria':'bg',
    'Burkina Faso':'bf',
    'Burundi':'bi',
    'Cambodia':'kh',
    'Cameroon':'cm',
    'Canada':'ca',
    'Cape Verde':'cv',
    'Caribbean Netherlands ':'bq',
    'Cayman Islands':'ky',
    'Central African Republic':'cf',
    'Chad':'td',
    'Chile':'cl',
    'China':'cn',
    'Christmas Island':'cx',
    'Cocos (Keeling) Islands':'cc',
    'Colombia':'co',
    'Comoros':'km',
    'Congo':'cg',
    'Congo, Democratic Republic of':'cd',
    'Cook Islands':'ck',
    'Costa Rica':'cr',
    'Côte d\'Ivoire':'ci',
    'Croatia':'hr',
    'Cuba':'cu',
    'Curaçao':'cw',
    'Cyprus':'cy',
    'Czech Republic':'cz',
    'Denmark':'dk',
    'Djibouti':'dj',
    'Dominica':'dm',
    'Dominican Republic':'do',
    'Ecuador':'ec',
    'Egypt':'eg',
    'El Salvador':'sv',
    'Equatorial Guinea':'gq',
    'Eritrea':'er',
    'Estonia':'ee',
    'Ethiopia':'et',
    'Falkland Islands':'fk',
    'Faroe Islands':'fo',
    'Fiji':'fj',
    'Finland':'fi',
    'France':'fr',
    'French Guiana':'gf',
    'French Polynesia':'pf',
    'French Southern Territories':'tf',
    'Gabon':'ga',
    'Gambia':'gm',
    'Georgia':'ge',
    'Germany':'de',
    'Ghana':'gh',
    'Gibraltar':'gi',
    'Greece':'gr',
    'Greenland':'gl',
    'Grenada':'gd',
    'Guadeloupe':'gp',
    'Guam':'gu',
    'Guatemala':'gt',
    'Guernsey':'gg',
    'Guinea':'gn',
    'Guinea-Bissau':'gw',
    'Guyana':'gy',
    'Haiti':'ht',
    'Heard and McDonald Islands':'hm',
    'Honduras':'hn',
    'Hong Kong':'hk',
    'Hungary':'hu',
    'Iceland':'is',
    'India':'in',
    'Indonesia':'id',
    'Iran':'ir',
    'Iraq':'iq',
    'Ireland':'ie',
    'Isle of Man':'im',
    'Israel':'il',
    'Italy':'it',
    'Jamaica':'jm',
    'Japan':'jp',
    'Jersey':'je',
    'Jordan':'jo',
    'Kazakhstan':'kz',
    'Kenya':'ke',
    'Kiribati':'ki',
    'Kuwait':'kw',
    'Kyrgyzstan':'kg',
    'Lao People\'s Democratic Republic':'la',
    'Latvia':'lv',
    'Lebanon':'lb',
    'Lesotho':'ls',
    'Liberia':'lr',
    'Libya':'ly',
    'Liechtenstein':'li',
    'Lithuania':'lt',
    'Luxembourg':'lu',
    'Macau':'mo',
    'Macedonia':'mk',
    'Madagascar':'mg',
    'Malawi':'mw',
    'Malaysia':'my',
    'Maldives':'mv',
    'Mali':'ml',
    'Malta':'mt',
    'Marshall Islands':'mh',
    'Martinique':'mq',
    'Mauritania':'mr',
    'Mauritius':'mu',
    'Mayotte':'yt',
    'Mexico':'mx',
    'Micronesia, Federated States of':'fm',
    'Moldova':'md',
    'Monaco':'mc',
    'Mongolia':'mn',
    'Montenegro':'me',
    'Montserrat':'ms',
    'Morocco':'ma',
    'Mozambique':'mz',
    'Myanmar':'mm',
    'Namibia':'NA',
    'Nauru':'nr',
    'Nepal':'np',
    'New Caledonia':'nc',
    'New Zealand':'nz',
    'Nicaragua':'ni',
    'Niger':'ne',
    'Nigeria':'ng',
    'Niue':'nu',
    'Norfolk Island':'nf',
    'North Korea':'kp',
    'Northern Mariana Islands':'mp',
    'Norway':'no',
    'Oman':'om',
    'Pakistan':'pk',
    'Palau':'pw',
    'Palestine, State of':'ps',
    'Panama':'pa',
    'Papua New Guinea':'pg',
    'Paraguay':'py',
    'Peru':'pe',
    'Philippines':'ph',
    'Pitcairn':'pn',
    'Poland':'pl',
    'Portugal':'pt',
    'Puerto Rico':'pr',
    'Qatar':'qa',
    'Réunion':'re',
    'Romania':'ro',
    'Russian Federation':'ru',
    'Rwanda':'rw',
    'Saint-Martin (France)':'mf',
    'Saint Barthélemy':'bl',
    'Saint Helena':'sh',
    'Saint Kitts and Nevis':'kn',
    'Saint Lucia':'lc',
    'Saint Vincent and the Grenadines':'vc',
    'Samoa':'ws',
    'San Marino':'sm',
    'Sao Tome and Principe':'st',
    'Saudi Arabia':'sa',
    'Senegal':'sn',
    'Serbia':'rs',
    'Seychelles':'sc',
    'Sierra Leone':'sl',
    'Singapore':'sg',
    'Sint Maarten (Dutch part)':'sx',
    'Slovakia':'sk',
    'Slovenia':'si',
    'Solomon Islands':'sb',
    'Somalia':'so',
    'South Africa':'za',
    'South Georgia and the South Sandwich Islands':'gs',
    'South Korea':'kr',
    'South Sudan':'ss',
    'Spain':'es',
    'Sri Lanka':'lk',
    'St. Pierre and Miquelon':'pm',
    'Sudan':'sd',
    'Suriname':'sr',
    'Svalbard and Jan Mayen Islands':'sj',
    'Swaziland':'sz',
    'Sweden':'se',
    'Switzerland':'ch',
    'Syria':'sy',
    'Taiwan':'tw',
    'Tajikistan':'tj',
    'Tanzania':'tz',
    'Thailand':'th',
    'The Netherlands':'nl',
    'Timor-Leste':'tl',
    'Togo':'tg',
    'Tokelau':'tk',
    'Tonga':'to',
    'Trinidad and Tobago':'tt',
    'Tunisia':'tn',
    'Turkey':'tr',
    'Turkmenistan':'tm',
    'Turks and Caicos Islands':'tc',
    'Tuvalu':'tv',
    'Uganda':'ug',
    'Ukraine':'ua',
    'United Arab Emirates':'ae',
    'United Kingdom':'gb',
    'United States':'us',
    'United States Minor Outlying Islands':'um',
    'Uruguay':'uy',
    'Uzbekistan':'uz',
    'Vanuatu':'vu',
    'Vatican':'va',
    'Venezuela':'ve',
    'Vietnam':'vn',
    'Virgin Islands (British)':'vg',
    'Virgin Islands (U.S.)':'vi',
    'Wallis and Futuna Islands':'wf',
    'Western Sahara':'eh',
    'Yemen':'ye',
    'Zambia':'zm',
    'Zimbabwe':'zw'
    }

    short_code = code_dict[country_name]

    return(short_code)

def publication_options():
    choices = [('Journal article','Journal article'),
    ('Pre-print','Pre-print'),
    ('Website','Website'),
    ('Government report','Government report'),
    ('NGO report','NGO report'),
    ('Other','Other')]
    return choices

def match_vtds(df):
    '''Change df GEOIDs to match vtd(dataframe) GEOIDs'''

    # Adams
    df.loc[df['GEOID10']=='4201912', 'GEOID10'] = "42019PR85"
    df.loc[df['GEOID10']=='4201914', 'GEOID10'] = "42019PR86"
    df.loc[df['GEOID10']=='4201916', 'GEOID10'] = "42019PR87"

    # Aliquippa
    df.loc[df['GEOID10']=='4200795', 'GEOID10'] = "4200756"

    # Amity
    df.loc[df['GEOID10']=='4201154', 'GEOID10'] = "4201140A"
    df.loc[df['GEOID10']=='4201156', 'GEOID10'] = "4201150A"
    df.loc[df['GEOID10']=='4201152', 'GEOID10'] = "4201150B"
    df.loc[df['GEOID10']=='4201158', 'GEOID10'] = "4201140B"
    df.loc[df['GEOID10']=='4201151', 'GEOID10'] = "4201150"

    # Apollo
    df.loc[df['GEOID10']=='4200515', 'GEOID10'] = "4200510"   #MGGG joined with 4200520 - Apollo D 2

    # Archbald
    df.loc[df['GEOID10']=='4206955', 'GEOID10'] = "4206950"
    df.loc[df['GEOID10']=='4206922', 'GEOID10'] = "4206920"

    # Ashland
    df.loc[df['GEOID10']=='4210725', 'GEOID10'] = "4210720"
    df.loc[df['GEOID10']=='4210715', 'GEOID10'] = "4210710"

    # Ashley
    df.loc[df['GEOID10']=='4207925', 'GEOID10'] = "4207940"

    # Barr
    # df.loc[df['GEOID10']=='420210', 'GEOID10'] = "42021130"    #Northern Cambria? #mismatch

    # Bensalem
    df.loc[df['GEOID10']=='42017165', 'GEOID10'] = "42017160"

    #Berwick
    df.loc[df['GEOID10']=='4203795', 'GEOID10'] = "4203790"
    df.loc[df['GEOID10']=='4203755', 'GEOID10'] = "4203745"
    df.loc[df['GEOID10']=='42037115', 'GEOID10'] = "42037110"

    # Bethel
    df.loc[df['GEOID10']=='42045108', 'GEOID10'] = "42045106"
    df.loc[df['GEOID10']=='42045112', 'GEOID10'] = "4204520037"
    # No BETHEL P 6

    # Bethlehem
    # df.loc[df['GEOID10']=='42095366']  #W 3 D 4
    df.loc[df['GEOID10']=='42095343', 'GEOID10'] = "42095340"
    df.loc[df['GEOID10']=='42095346', 'GEOID10'] = "42095345"
    df.loc[df['GEOID10']=='42095348', 'GEOID10'] = "42095348"
    df.loc[df['GEOID10']=='42095338', 'GEOID10'] = "42095337"
    # df.loc[df['GEOID10']=='420950'] #W 17 B (Cong 17)
    df.loc[df['GEOID10']=='4209565', 'GEOID10'] = "4209580"
    df.loc[df['GEOID10']=='42095363', 'GEOID10'] = "42095367"
    # No BETHEL P 6

    # Blakely
    df.loc[df['GEOID10']=='42069115', 'GEOID10'] = "42069110"
    df.loc[df['GEOID10']=='42069135', 'GEOID10'] = "42069130"

    # Bloomsburg
    df.loc[df['GEOID10']=='42037172', 'GEOID10'] = "42037180"

    # Blythe
    df.loc[df['GEOID10']=='4210785', 'GEOID10'] = "4210790"

    # Brady's Bend
    df.loc[df['GEOID10']=='4200575', 'GEOID10'] = "4200570"

    # Branch
    df.loc[df['GEOID10']=='42107105', 'GEOID10'] = "42107100"

    # Briar Creek
    df.loc[df['GEOID10']=='42037232', 'GEOID10'] = "42037235"

    # Bristol
    df.loc[df['GEOID10']=='42017655', 'GEOID10'] = "42017650"
    df.loc[df['GEOID10']=='42017598', 'GEOID10'] = "42017590"
    df.loc[df['GEOID10']=='42017585', 'GEOID10'] = "42017580"
    df.loc[df['GEOID10']=='42017575', 'GEOID10'] = "42017570"
    df.loc[df['GEOID10']=='42017545', 'GEOID10'] = "42017540"
    df.loc[df['GEOID10']=='42017535', 'GEOID10'] = "42017530"
    df.loc[df['GEOID10']=='42017515', 'GEOID10'] = "42017510"
    df.loc[df['GEOID10']=='42017435', 'GEOID10'] = "42017430"
    df.loc[df['GEOID10']=='42017445', 'GEOID10'] = "42017440"
    df.loc[df['GEOID10']=='42017645', 'GEOID10'] = "42017640"
    df.loc[df['GEOID10']=='42017505', 'GEOID10'] = "42017500"

    # Buckingham
    df.loc[df['GEOID10']=='42017817', 'GEOID10'] = "42017818"
    df.loc[df['GEOID10']=='42017813', 'GEOID10'] = "42017815"

    #Buffalo
    df.loc[df['GEOID10']=='4201960', 'GEOID10'] = "4201951"
    df.loc[df['GEOID10']=='4201965', 'GEOID10'] = "4201952"

    # Butler
    df.loc[df['GEOID10']=='42019135', 'GEOID10'] = "42019130"
    df.loc[df['GEOID10']=='42079155', 'GEOID10'] = "42079160"
    df.loc[df['GEOID10']=='4201975', 'GEOID10'] = "4201980"

    # Caernarvon
    df.loc[df['GEOID10']=='42011192', 'GEOID10'] = "42011195" #misspelled as CARENARVON
    df.loc[df['GEOID10']=='42011188', 'GEOID10'] = "42011190"

    # Carbondale
    df.loc[df['GEOID10']=='42069275', 'GEOID10'] = "42069270"
    df.loc[df['GEOID10']=='42069305', 'GEOID10'] = "42069300"
    df.loc[df['GEOID10']=='42069315', 'GEOID10'] = "42069310"
    df.loc[df['GEOID10']=='42069355', 'GEOID10'] = "42069350"
    df.loc[df['GEOID10']=='42069250', 'GEOID10'] = "420692040"
    df.loc[df['GEOID10']=='42069175', 'GEOID10'] = "42069170"

    # Carrol Valley
    df.loc[df['GEOID10']=='4200178', 'GEOID10'] = "4200180A"
    df.loc[df['GEOID10']=='4200182', 'GEOID10'] = "4200180"

    # Cass
    df.loc[df['GEOID10']=='42107175', 'GEOID10'] = "42107170"

    # Catawissa
    df.loc[df['GEOID10']=='42037275', 'GEOID10'] = "42037270"

    # Center
    df.loc[df['GEOID10']=='42019248', 'GEOID10'] = "42019250"
    df.loc[df['GEOID10']=='42019242', 'GEOID10'] = "42019240"
    df.loc[df['GEOID10']=='42019254', 'GEOID10'] = "42019255"
    df.loc[df['GEOID10']=='42011208', 'GEOID10'] = "42011210A"
    df.loc[df['GEOID10']=='42011212', 'GEOID10'] = "42011210"

    # Chadds
    df.loc[df['GEOID10']=='42045174', 'GEOID10'] = "42045175" #only one Chadds VTD (split?)

    # Chambersburg
    df.loc[df['GEOID10']=='42055105', 'GEOID10'] = "42055100"

    # Clay
    df.loc[df['GEOID10']=='4207192', 'GEOID10'] = "4207190"
    df.loc[df['GEOID10']=='4207188', 'GEOID10'] = "4207195"

    # Coaldale
    df.loc[df['GEOID10']=='42107205', 'GEOID10'] = "42107200"
    df.loc[df['GEOID10']=='42107225', 'GEOID10'] = "42107220"

    # COLLEGEVILLE
    # df.loc[df['GEOID10']=='42091732', 'GEOID10'] = "42091730"         #mismatch
    df.loc[df['GEOID10']=='42091728', 'GEOID10'] = "42091723"

    # Columbia
    df.loc[df['GEOID10']=='42071155', 'GEOID10'] = "42071150"
    df.loc[df['GEOID10']=='42071115', 'GEOID10'] = "42071110"

    # Conewago
    df.loc[df['GEOID10']=='4204323', 'GEOID10'] = "4204320"

    #Connellsville
    df.loc[df['GEOID10']=='42051155', 'GEOID10'] = "42051150"

    # Conyngham
    df.loc[df['GEOID10']=='42079165', 'GEOID10'] = "42079170"
    df.loc[df['GEOID10']=='42037340', 'GEOID10'] = "42037330"

    # Cranberry
    # df.loc[df['GEOID10']=='42019379', 'GEOID10'] = "42019356"         #mismatch

    #Cresson
    df.loc[df['GEOID10']=='42021330', 'GEOID10'] = "42021311"

    #Cressona
    df.loc[df['GEOID10']=='42107235', 'GEOID10'] = "42107230"

    #Cumru
    df.loc[df['GEOID10']=='42011295', 'GEOID10'] = "42011263"
    df.loc[df['GEOID10']=='42011292', 'GEOID10'] = "42011290"
    # No CUMRU D 1 B (Cong 16) to join

    # Dallas
    df.loc[df['GEOID10']=='42079205', 'GEOID10'] = "42079210"
    df.loc[df['GEOID10']=='42079225', 'GEOID10'] = "42079220"
    df.loc[df['GEOID10']=='42079215', 'GEOID10'] = "42079200"

    # Delaware
    df.loc[df['GEOID10']=='4210315', 'GEOID10'] = "4210320"
    df.loc[df['GEOID10']=='4210322', 'GEOID10'] = "4210321"

    # Derry
    # df.loc[df['GEOID10']=='42043147', 'GEOID10'] = "42043143"         #mismatch
    df.loc[df['GEOID10']=='42043112', 'GEOID10'] = "42043111"

    # Dickson City
    df.loc[df['GEOID10']=='42069525', 'GEOID10'] = "42069520"
    df.loc[df['GEOID10']=='42069495', 'GEOID10'] = "42069490"
    df.loc[df['GEOID10']=='42069565', 'GEOID10'] = "42069570"

    # Doylestown
    df.loc[df['GEOID10']=='42017832', 'GEOID10'] = "42017830"
    df.loc[df['GEOID10']=='42017887', 'GEOID10'] = "420172202"

    # Dunmore
    df.loc[df['GEOID10']=='4209965', 'GEOID10'] = "4209960"
    df.loc[df['GEOID10']=='42069670', 'GEOID10'] = "420692043"
    df.loc[df['GEOID10']=='42069665', 'GEOID10'] = "42069660"
    df.loc[df['GEOID10']=='42069635', 'GEOID10'] = "420692041"
    df.loc[df['GEOID10']=='42069595', 'GEOID10'] = "42069590"
    df.loc[df['GEOID10']=='42069745', 'GEOID10'] = "42069740"
    df.loc[df['GEOID10']=='42069585', 'GEOID10'] = "42069580"

    # Dupont
    df.loc[df['GEOID10']=='42079275', 'GEOID10'] = "42079270"

    # Duryea
    df.loc[df['GEOID10']=='42079325', 'GEOID10'] = "42079330"
    df.loc[df['GEOID10']=='42079310', 'GEOID10'] = "42079320"

    # East Bradford
    df.loc[df['GEOID10']=='42029185', 'GEOID10'] = "42029180"

    # East Calin
    df.loc[df['GEOID10']=='42029222', 'GEOID10'] = "42029220"
    # NO East Calin X 2

    # East Cocalico
    df.loc[df['GEOID10']=='42071272', 'GEOID10'] = "42071270"

    # East Goshen
    df.loc[df['GEOID10']=='42029295', 'GEOID10'] = "42029280"
    df.loc[df['GEOID10']=='42029347', 'GEOID10'] = "420292050"

    # East Lampeter
    df.loc[df['GEOID10']=='42071433', 'GEOID10'] = "42071430"
    df.loc[df['GEOID10']=='42071427', 'GEOID10'] = "42071424"
    df.loc[df['GEOID10']=='42071402', 'GEOID10'] = "42071405"
    df.loc[df['GEOID10']=='42071429', 'GEOID10'] = "42071400"


    #East Marlborough
    df.loc[df['GEOID10']=='42029334', 'GEOID10'] = "42029330"

    # Easy Norwegian
    df.loc[df['GEOID10']=='42107285', 'GEOID10'] = "42107290"

    # East Penn
    df.loc[df['GEOID10']=='4202562', 'GEOID10'] = "4202566"
    df.loc[df['GEOID10']=='4202558', 'GEOID10'] = "4202565"

    # EAST PENNSBORO
    df.loc[df['GEOID10']=='42041191', 'GEOID10'] = "42041180"
    df.loc[df['GEOID10']=='42041175', 'GEOID10'] = "42041195"
    df.loc[df['GEOID10']=='42041194', 'GEOID10'] = "42041184"
    df.loc[df['GEOID10']=='42041198', 'GEOID10'] = "42041185"
    df.loc[df['GEOID10']=='42041202', 'GEOID10'] = "42041186"
    df.loc[df['GEOID10']=='42041211', 'GEOID10'] = "42041200"
    df.loc[df['GEOID10']=='42041179', 'GEOID10'] = "42041210"
    df.loc[df['GEOID10']=='42041183', 'GEOID10'] = "42041190"

    # East Union
    df.loc[df['GEOID10']=='42107305', 'GEOID10'] = "42107300"

    # Edwardsville
    df.loc[df['GEOID10']=='42079365', 'GEOID10'] = "42079360"
    df.loc[df['GEOID10']=='42079375', 'GEOID10'] = "42079370"


    # Elizabeth
    df.loc[df['GEOID10']=='420032000', 'GEOID10'] = "420032001"
    df.loc[df['GEOID10']=='420032022', 'GEOID10'] = "420032020"
    df.loc[df['GEOID10']=='420032032', 'GEOID10'] = "420032030"
    df.loc[df['GEOID10']=='420032042', 'GEOID10'] = "420032040"
    df.loc[df['GEOID10']=='420032025', 'GEOID10'] = "420032020"
    df.loc[df['GEOID10']=='420032035', 'GEOID10'] = "420032030"
    # No WD 7
    # No WD 8 D 1
    # No WD 8 D 2
    # No WD 9

    # Edgmont
    df.loc[df['GEOID10']=='420451005', 'GEOID10'] = "420451030"
    df.loc[df['GEOID10']=='4207375', 'GEOID10'] = "4207360"
    df.loc[df['GEOID10']=='4207335', 'GEOID10'] = "4207340"

    # Exter
    df.loc[df['GEOID10']=='42011397', 'GEOID10'] = "42011362"
    df.loc[df['GEOID10']=='42011395', 'GEOID10'] = "42011386"
    df.loc[df['GEOID10']=='42011384', 'GEOID10'] = "42011385"
    df.loc[df['GEOID10']=='42011358', 'GEOID10'] = "42011360"

    # Ferguson
    df.loc[df['GEOID10']=='42027205', 'GEOID10'] = "42027PR87"
    df.loc[df['GEOID10']=='42027235', 'GEOID10'] = "42027PR86"

    # Fishing Creek
    df.loc[df['GEOID10']=='42037372', 'GEOID10'] = "42037370"

    # Fleetwood
    df.loc[df['GEOID10']=='42011406', 'GEOID10'] = "42011400A"
    df.loc[df['GEOID10']=='42011402', 'GEOID10'] = "42011400"

    # Forty Fort
    df.loc[df['GEOID10']=='42079515', 'GEOID10'] = "42079510"
    df.loc[df['GEOID10']=='42079535', 'GEOID10'] = "42079530"
    df.loc[df['GEOID10']=='42079495', 'GEOID10'] = "42079490"

    # Foster
    df.loc[df['GEOID10']=='42079555', 'GEOID10'] = "42079550"
    df.loc[df['GEOID10']=='42079565', 'GEOID10'] = "42079560"
    # Frankville
    df.loc[df['GEOID10']=='42107385', 'GEOID10'] = "42107380"


    # Franconia
    df.loc[df['GEOID10']=='42091914', 'GEOID10'] = "42091905"
    df.loc[df['GEOID10']=='42091917', 'GEOID10'] = "42091911"
    df.loc[df['GEOID10']=='42091919', 'GEOID10'] = "42091913"
    df.loc[df['GEOID10']=='42091924', 'GEOID10'] = "42091916"
    df.loc[df['GEOID10']=='42091927', 'GEOID10'] = "42091918"
    df.loc[df['GEOID10']=='42091931', 'GEOID10'] = "42091923"
    df.loc[df['GEOID10']=='42091933', 'GEOID10'] = "42091926"
    df.loc[df['GEOID10']=='42091936', 'GEOID10'] = "42091928"
    #FRANCONIA P 3, FRANCONIA P 4, FRANCONIA P 6, FRANCONIA P 7 joined to
    #FRANCONIA TWP VTD NORTH ED EAST, FRANCONIA TWP VTD NORTH ED WEST,
    #FRANCONIA TWP VTD SOUTH ED EAST, RANCONIA TWP VTD SOUTH ED WEST, respectively

    # Franklin
    df.loc[df['GEOID10']=='42121195', 'GEOID10'] = "42121250"

    # Freeland
    df.loc[df['GEOID10']=='42079595', 'GEOID10'] = "42079590"
    df.loc[df['GEOID10']=='42079605', 'GEOID10'] = "42079600"

    # Giestown
    df.loc[df['GEOID10']=='42021670', 'GEOID10'] = "42021675"

    # Gilpin
    # df.loc[df['GEOID10']=='42005265', 'GEOID10'] = "42005260"      #mismatch

    # German
    df.loc[df['GEOID10']=='42051365', 'GEOID10'] = "42051360"

    # Gettysberg
    df.loc[df['GEOID10']=='42001210', 'GEOID10'] = "42001220"

    # Gilberton
    df.loc[df['GEOID10']=='42107415', 'GEOID10'] = "42107410"

    # Girardvill
    df.loc[df['GEOID10']=='42107435', 'GEOID10'] = "42107430"

    # Halifax
    df.loc[df['GEOID10']=='42043191', 'GEOID10'] = "42043PR151"
    df.loc[df['GEOID10']=='42043194', 'GEOID10'] = "42043192"

    # Hanover
    df.loc[df['GEOID10']=='42079702', 'GEOID10'] = "42079695"
    df.loc[df['GEOID10']=='42079665', 'GEOID10'] = "42079660"
    df.loc[df['GEOID10']=='42079765', 'GEOID10'] = "42079760"
    df.loc[df['GEOID10']=='42079725', 'GEOID10'] = "42079720"
    df.loc[df['GEOID10']=='42079680', 'GEOID10'] = "42079670"

    # Hatfield
    df.loc[df['GEOID10']=='42091992', 'GEOID10'] = "42091991"
    df.loc[df['GEOID10']=='420911016', 'GEOID10'] = "420911020"
    df.loc[df['GEOID10']=='420911012', 'GEOID10'] = "420911011"
    # df.loc[df['GEOID10']=='420910', 'GEOID10'] = "420911010"          #mismatch
    df.loc[df['GEOID10']=='420911006', 'GEOID10'] = "42091990"
    df.loc[df['GEOID10']=='420911026', 'GEOID10'] = "420911021"
    df.loc[df['GEOID10']=='42091996', 'GEOID10'] = "420911000"
    df.loc[df['GEOID10']=='420911032', 'GEOID10'] = "420911023"
    df.loc[df['GEOID10']=='420911036', 'GEOID10'] = "420911030"
    # df.loc[df['GEOID10']=='420911002', 'GEOID10'] = "420911010"        #mismatch

    # Hazle
    df.loc[df['GEOID10']=='42079845', 'GEOID10'] = "42079800"
    df.loc[df['GEOID10']=='42079835', 'GEOID10'] = "42079870"
    df.loc[df['GEOID10']=='42079825', 'GEOID10'] = "42079810"
    df.loc[df['GEOID10']=='42079815', 'GEOID10'] = "42079890"
    df.loc[df['GEOID10']=='42079805', 'GEOID10'] = "42079880"

    # Hazleton
    df.loc[df['GEOID10']=='42079985', 'GEOID10'] = "42079980"
    df.loc[df['GEOID10']=='42079995', 'GEOID10'] = "42079990"
    df.loc[df['GEOID10']=='42079965', 'GEOID10'] = "42079960"
    df.loc[df['GEOID10']=='42079955', 'GEOID10'] = "42079950"
    df.loc[df['GEOID10']=='420791025', 'GEOID10'] = "420791020"
    df.loc[df['GEOID10']=='420791035', 'GEOID10'] = "420791080"
    df.loc[df['GEOID10']=='42079975', 'GEOID10'] = "42079970"
    df.loc[df['GEOID10']=='420791005', 'GEOID10'] = "420791050"

    # Hemlock
    df.loc[df['GEOID10']=='42037422', 'GEOID10'] = "42037420"

    # Hilltown
    df.loc[df['GEOID10']=='420171187', 'GEOID10'] = "420172203"
    df.loc[df['GEOID10']=='420171184', 'GEOID10'] = "420171185"

    # Honesdale
    df.loc[df['GEOID10']=='42127165', 'GEOID10'] = "42127160"
    df.loc[df['GEOID10']=='42127155', 'GEOID10'] = "42127150"
    df.loc[df['GEOID10']=='42127145', 'GEOID10'] = "42127140"

    # Horsham
    df.loc[df['GEOID10']=='420911145', 'GEOID10'] = "420911132"
    df.loc[df['GEOID10']=='420911150', 'GEOID10'] = "420911133"
    df.loc[df['GEOID10']=='420911135', 'GEOID10'] = "420911130"
    df.loc[df['GEOID10']=='420911072', 'GEOID10'] = "420911067"
    df.loc[df['GEOID10']=='420911142', 'GEOID10'] = "420911131"

    # Hughestown
    df.loc[df['GEOID10']=='420791165', 'GEOID10'] = "420791160"

    # Irwin
    df.loc[df['GEOID10']=='421291020', 'GEOID10'] = "421291015"
    df.loc[df['GEOID10']=='42129970', 'GEOID10'] = "421291005"

    # Jenkins
    df.loc[df['GEOID10']=='420791245', 'GEOID10'] = "420791230"
    df.loc[df['GEOID10']=='420791225', 'GEOID10'] = "420791220"
    df.loc[df['GEOID10']=='420791235', 'GEOID10'] = "420791250"

    # Jessup
    df.loc[df['GEOID10']=='42069875', 'GEOID10'] = "42069870"
    df.loc[df['GEOID10']=='42069895', 'GEOID10'] = "42069890"
    df.loc[df['GEOID10']=='42069925', 'GEOID10'] = "42069920"

    # Johnstown
    df.loc[df['GEOID10']=='420211040', 'GEOID10'] = "420211045"

    # Kennett
    df.loc[df['GEOID10']=='42029622', 'GEOID10'] = "420292051"
    df.loc[df['GEOID10']=='42029602', 'GEOID10'] = "42029600"

    # Kingston
    df.loc[df['GEOID10']=='420791295', 'GEOID10'] = "420791290"
    df.loc[df['GEOID10']=='420791285', 'GEOID10'] = "420791280"
    df.loc[df['GEOID10']=='420791375', 'GEOID10'] = "420791370"
    df.loc[df['GEOID10']=='420791355', 'GEOID10'] = "420791360"
    df.loc[df['GEOID10']=='420791305', 'GEOID10'] = "420791300"
    df.loc[df['GEOID10']=='420791340', 'GEOID10'] = "420791350"

    # Kline
    df.loc[df['GEOID10']=='42107505', 'GEOID10'] = "42107500"

    # Lackawaxen
    df.loc[df['GEOID10']=='4210352', 'GEOID10'] = "4210351"
    df.loc[df['GEOID10']=='4210345', 'GEOID10'] = "4210350"

    # Larksville
    df.loc[df['GEOID10']=='420791445', 'GEOID10'] = "420791440"

    # Lehman
    df.loc[df['GEOID10']=='420791353', 'GEOID10'] = "420791530"
    df.loc[df['GEOID10']=='420791525', 'GEOID10'] = "420791520"
    df.loc[df['GEOID10']=='420791515', 'GEOID10'] = "420791540"

    # Londonderry
    df.loc[df['GEOID10']=='42043551', 'GEOID10'] = "42043550"
    df.loc[df['GEOID10']=='42043565', 'GEOID10'] = "42043561"

    # Lower Heidelberg
    df.loc[df['GEOID10']=='42011618', 'GEOID10'] = "42011620"
    df.loc[df['GEOID10']=='42011623', 'GEOID10'] = "42011630"
    df.loc[df['GEOID10']=='42011628', 'GEOID10'] = "42011625"

    # Lower Macungie
    df.loc[df['GEOID10']=='42077892', 'GEOID10'] = "42077890"
    df.loc[df['GEOID10']=='42077926', 'GEOID10'] = "42077891"
    df.loc[df['GEOID10']=='42077928', 'GEOID10'] = "42077901"
    df.loc[df['GEOID10']=='42077922', 'GEOID10'] = "42077911"

    # Lower Merion
    df.loc[df['GEOID10']=='420911698', 'GEOID10'] = "420911700"


    # Lower Paxton
    df.loc[df['GEOID10']=='42043761', 'GEOID10'] = "42043PR152"
    df.loc[df['GEOID10']=='42043766', 'GEOID10'] = "42043PR154"
    df.loc[df['GEOID10']=='42043768', 'GEOID10'] = "42043PR202"
    df.loc[df['GEOID10']=='42043767', 'GEOID10'] = "42043PR201"
    df.loc[df['GEOID10']=='42043764', 'GEOID10'] = "42043PR200"
    df.loc[df['GEOID10']=='42043763', 'GEOID10'] = "42043PR157"
    df.loc[df['GEOID10']=='42043762', 'GEOID10'] = "42043PR156"
    df.loc[df['GEOID10']=='42043651', 'GEOID10'] = "42043650"
    df.loc[df['GEOID10']=='42043681', 'GEOID10'] = "42043680"
    df.loc[df['GEOID10']=='42043711', 'GEOID10'] = "42043710"
    df.loc[df['GEOID10']=='42043731', 'GEOID10'] = "42043730"
    df.loc[df['GEOID10']=='42043751', 'GEOID10'] = "42043750"

    # Lower Providence
    df.loc[df['GEOID10']=='420911944', 'GEOID10'] = "420911930"
    df.loc[df['GEOID10']=='420911950', 'GEOID10'] = "420911940"
    df.loc[df['GEOID10']=='420911956', 'GEOID10'] = "420911945"
    df.loc[df['GEOID10']=='420911938', 'GEOID10'] = "420911920"

    # lower Towamensing
    df.loc[df['GEOID10']=='42025262', 'GEOID10'] = "42025265"
    df.loc[df['GEOID10']=='42025258', 'GEOID10'] = "42025260"

    # Luzerne
    df.loc[df['GEOID10']=='420791565', 'GEOID10'] = "420791560"

    # Mahoning
    df.loc[df['GEOID10']=='42005425', 'GEOID10'] = "42005260"

    # Mahonoy
    # df.loc[df['GEOID10']=='42107535', 'GEOID10'] = "42107530"             #mismatch

    # Mahonoy City
    df.loc[df['GEOID10']=='42107575', 'GEOID10'] = "42107570"
    df.loc[df['GEOID10']=='42107565', 'GEOID10'] = "42107560"
    df.loc[df['GEOID10']=='42107585', 'GEOID10'] = "42107580"

    # Maidencreek
    df.loc[df['GEOID10']=='42011652', 'GEOID10'] = "42011645"
    df.loc[df['GEOID10']=='42011654', 'GEOID10'] = "42011655"
    df.loc[df['GEOID10']=='42011662', 'GEOID10'] = "42011665"
    df.loc[df['GEOID10']=='42011646', 'GEOID10'] = "42011635"

    # Manheim
    df.loc[df['GEOID10']=='420711344', 'GEOID10'] = "42071PR244"
    df.loc[df['GEOID10']=='420711332', 'GEOID10'] = "420711330"
    df.loc[df['GEOID10']=='420711155', 'GEOID10'] = "420711150"
    df.loc[df['GEOID10']=='420711337', 'GEOID10'] = "42071PR243"
    df.loc[df['GEOID10']=='420711335', 'GEOID10'] = "42071PR245"

    # Manor
    df.loc[df['GEOID10']=='420711405', 'GEOID10'] = "42071PR246"
    df.loc[df['GEOID10']=='420711402', 'GEOID10'] = "420711400"

    # Marlborough
    df.loc[df['GEOID10']=='420911995', 'GEOID10'] = "420911990"

    # Marshall
    df.loc[df['GEOID10']=='420033232', 'GEOID10'] = "420033231"
    df.loc[df['GEOID10']=='420033233', 'GEOID10'] = "420032091"
    df.loc[df['GEOID10']=='420033235', 'GEOID10'] = "42003PR1310"
    df.loc[df['GEOID10']=='420033235', 'GEOID10'] = "42003PR1311"
    df.loc[df['GEOID10']=='420033237', 'GEOID10'] = "42003PR1311"

    # Masontown
    df.loc[df['GEOID10']=='42051545', 'GEOID10'] = "42051540"
    df.loc[df['GEOID10']=='42051535', 'GEOID10'] = "42051530"

    # Middletown
    df.loc[df['GEOID10']=='420171652', 'GEOID10'] = "420171650"
    df.loc[df['GEOID10']=='420171708', 'GEOID10'] = "420171707"

    # Millcreek
    df.loc[df['GEOID10']=='420491317', 'GEOID10'] = "42049PR155"
    df.loc[df['GEOID10']=='420491125', 'GEOID10'] = "420491120"

    # Millersville
    df.loc[df['GEOID10']=='420711465', 'GEOID10'] = "420711460"

    # Moosic
    df.loc[df['GEOID10']=='420691005', 'GEOID10'] = "420691000"
    df.loc[df['GEOID10']=='420691010', 'GEOID10'] = "420691040"

    #Muhlenberg
    df.loc[df['GEOID10']=='42011771', 'GEOID10'] = "42011773"
    df.loc[df['GEOID10']=='42011776', 'GEOID10'] = "42011768"
    df.loc[df['GEOID10']=='42011779', 'GEOID10'] = "42011774"

    # Nanticoke
    df.loc[df['GEOID10']=='420791605', 'GEOID10'] = "420791600"
    df.loc[df['GEOID10']=='420791615', 'GEOID10'] = "420791610"
    df.loc[df['GEOID10']=='420791625', 'GEOID10'] = "420791620"
    df.loc[df['GEOID10']=='420791630', 'GEOID10'] = "420791720"
    df.loc[df['GEOID10']=='420791640', 'GEOID10'] = "420791650"
    # Nanty Glo
    df.loc[df['GEOID10']=='420211320', 'GEOID10'] = "420211311"
    # Nether Providence
    df.loc[df['GEOID10']=='420452052', 'GEOID10'] = "420452050"
    df.loc[df['GEOID10']=='420452042', 'GEOID10'] = "420452040"
    df.loc[df['GEOID10']=='420452091', 'GEOID10'] = "420452090"
    df.loc[df['GEOID10']=='420452062', 'GEOID10'] = "420452060"
    df.loc[df['GEOID10']=='420452082', 'GEOID10'] = "420452080"
    df.loc[df['GEOID10']=='420452072', 'GEOID10'] = "420452070"
    # New Beaver
    df.loc[df['GEOID10']=='42073255', 'GEOID10'] = "42073250"
    # New Castle
    df.loc[df['GEOID10']=='42073625', 'GEOID10'] = "42073650"
    df.loc[df['GEOID10']=='42073565', 'GEOID10'] = "42073560"
    df.loc[df['GEOID10']=='42073595', 'GEOID10'] = "42073590"
    df.loc[df['GEOID10']=='42073665', 'GEOID10'] = "42073660"
    df.loc[df['GEOID10']=='42073555', 'GEOID10'] = "42073550"
    df.loc[df['GEOID10']=='42073355', 'GEOID10'] = "42073350"
    df.loc[df['GEOID10']=='42073485', 'GEOID10'] = "42073480"
    df.loc[df['GEOID10']=='42073475', 'GEOID10'] = "42073470"
    df.loc[df['GEOID10']=='42073495', 'GEOID10'] = "42073490"
    df.loc[df['GEOID10']=='42073315', 'GEOID10'] = "42073310"
    df.loc[df['GEOID10']=='42073325', 'GEOID10'] = "42073320"
    df.loc[df['GEOID10']=='42073425', 'GEOID10'] = "42073420"
    df.loc[df['GEOID10']=='42073415', 'GEOID10'] = "42073410"
    df.loc[df['GEOID10']=='42073345', 'GEOID10'] = "42073340"
    df.loc[df['GEOID10']=='42073335', 'GEOID10'] = "42073330"
    # New Garden
    df.loc[df['GEOID10']=='42029752', 'GEOID10'] = "42029750"
    # New Holland
    df.loc[df['GEOID10']=='420711576', 'GEOID10'] = "42071PR248"
    df.loc[df['GEOID10']=='420711574', 'GEOID10'] = "42071PR247"
    df.loc[df['GEOID10']=='420711572', 'GEOID10'] = "420711570"
    # Newport
    df.loc[df['GEOID10']=='420791785', 'GEOID10'] = "420791775"
    df.loc[df['GEOID10']=='420791805', 'GEOID10'] = "420791800"
    df.loc[df['GEOID10']=='420791795', 'GEOID10'] = "420791790"
    # North Manheim
    df.loc[df['GEOID10']=='42107802', 'GEOID10'] = "42107790"
    df.loc[df['GEOID10']=='42107796', 'GEOID10'] = "42107801"
    df.loc[df['GEOID10']=='42107792', 'GEOID10'] = "42107800"
    # North Strabane
    df.loc[df['GEOID10']=='421251365', 'GEOID10'] = "421251360"
    # Northhampton
    df.loc[df['GEOID10']=='420172115', 'GEOID10'] = "420172112"
    df.loc[df['GEOID10']=='420172025', 'GEOID10'] = "420172020"
    # Nottingham
    df.loc[df['GEOID10']=='421251375', 'GEOID10'] = "421251380"

    # Ohio
    df.loc[df['GEOID10']=='420035378', 'GEOID10'] = "420035381"
    df.loc[df['GEOID10']=='420035382', 'GEOID10'] = "420035385"
    df.loc[df['GEOID10']=='420035386', 'GEOID10'] = "42003PR1312"
    # Oliver
    df.loc[df['GEOID10']=='420691175', 'GEOID10'] = "42099220"
    # Olyphant
    df.loc[df['GEOID10']=='420691205', 'GEOID10'] = "420692044"
    # df.loc[df['GEOID10']=='420691209', 'GEOID10'] = "420691200"       #mismatch
    df.loc[df['GEOID10']=='420690', 'GEOID10'] = "420692045"
    # df.loc[df['GEOID10']=='420610', 'GEOID10'] = "420691200"          #mismatch


    # Penn
    df.loc[df['GEOID10']=='421292295', 'GEOID10'] = "421292270"
    df.loc[df['GEOID10']=='42109165', 'GEOID10'] = "42109PR26"
    df.loc[df['GEOID10']=='42109155', 'GEOID10'] = "42109PR28"
    # Penn Forest
    df.loc[df['GEOID10']=='42025367', 'GEOID10'] = "42025374"
    df.loc[df['GEOID10']=='42025363', 'GEOID10'] = "42025379"
    df.loc[df['GEOID10']=='42025371', 'GEOID10'] = "42025377"
    # Perry
    df.loc[df['GEOID10']=='42051692', 'GEOID10'] = "42051690"
    # Philadelphia
    df.loc[df['GEOID10']=='421014870', 'GEOID10'] = "421014902"
    df.loc[df['GEOID10']=='421011077', 'GEOID10'] = "421011075"
    df.loc[df['GEOID10']=='421011057', 'GEOID10'] = "421011055"
    # df.loc[df['GEOID10']=='421014890', 'GEOID10'] = "421014913"       #mismatch
    df.loc[df['GEOID10']=='421014895', 'GEOID10'] = "421014915"
    df.loc[df['GEOID10']=='42101560', 'GEOID10'] = "421011142"
    df.loc[df['GEOID10']=='42101562', 'GEOID10'] = "421011143"
    df.loc[df['GEOID10']=='42101564', 'GEOID10'] = "421011145"
    df.loc[df['GEOID10']=='42101566', 'GEOID10'] = "421011146"
    df.loc[df['GEOID10']=='42101568', 'GEOID10'] = "421011147"
    df.loc[df['GEOID10']=='42101570', 'GEOID10'] = "421011148"
    df.loc[df['GEOID10']=='42101534', 'GEOID10'] = "42101513"
    df.loc[df['GEOID10']=='421014875', 'GEOID10'] = "421014903"
    # Pine
    df.loc[df['GEOID10']=='420035785', 'GEOID10'] = "420035790"
    df.loc[df['GEOID10']=='420035788', 'GEOID10'] = "420035800"
    df.loc[df['GEOID10']=='420035791', 'GEOID10'] = "420035810"
    df.loc[df['GEOID10']=='420035795', 'GEOID10'] = "420031187"
    df.loc[df['GEOID10']=='420035805', 'GEOID10'] = "420031189"
    df.loc[df['GEOID10']=='420035808', 'GEOID10'] = "42003PN1190"
    df.loc[df['GEOID10']=='420035812', 'GEOID10'] = "420031188"
    df.loc[df['GEOID10']=='420035815', 'GEOID10'] = "420031191"

    # Pine Grove
    # df.loc[df['GEOID10']=='42107922', 'GEOID10'] = "42107930"         # mismatch
    # df.loc[df['GEOID10']=='42107912', 'GEOID10'] = "42107915"         # mismatch
    # Pittston
    df.loc[df['GEOID10']=='420792005', 'GEOID10'] = "420792000"
    df.loc[df['GEOID10']=='420791875', 'GEOID10'] = "420791870"
    df.loc[df['GEOID10']=='420791885', 'GEOID10'] = "420791880"
    df.loc[df['GEOID10']=='420791895', 'GEOID10'] = "420791890"
    df.loc[df['GEOID10']=='420791905', 'GEOID10'] = "420791970"
    df.loc[df['GEOID10']=='420791995', 'GEOID10'] = "420791990"
    # Plains
    df.loc[df['GEOID10']=='420792035', 'GEOID10'] = "420792020"
    df.loc[df['GEOID10']=='420792035', 'GEOID10'] = "420792040"
    df.loc[df['GEOID10']=='420792045', 'GEOID10'] = "420792050"
    df.loc[df['GEOID10']=='420792055', 'GEOID10'] = "420792100"
    df.loc[df['GEOID10']=='420792065', 'GEOID10'] = "420792060"
    # Plumstead
    df.loc[df['GEOID10']=='420172198', 'GEOID10'] = "420172196"
    df.loc[df['GEOID10']=='420172183', 'GEOID10'] = "420172185"
    df.loc[df['GEOID10']=='420172173', 'GEOID10'] = "420172175"
    # Plymouth
    df.loc[df['GEOID10']=='420792155', 'GEOID10'] = "420792150"
    df.loc[df['GEOID10']=='420792175', 'GEOID10'] = "420792170"
    df.loc[df['GEOID10']=='420912492', 'GEOID10'] = "420912490"
    df.loc[df['GEOID10']=='420792165', 'GEOID10'] = "420792160"
    # Pottstown
    df.loc[df['GEOID10']=='420912590', 'GEOID10'] = "420912610"
    df.loc[df['GEOID10']=='420912605', 'GEOID10'] = "420912600"
    df.loc[df['GEOID10']=='420912648', 'GEOID10'] = "42091PR415"
    df.loc[df['GEOID10']=='420912652', 'GEOID10'] = "42091PR416"
    # Pottsville
    df.loc[df['GEOID10']=='421071145', 'GEOID10'] = "421071150"
    df.loc[df['GEOID10']=='421071165', 'GEOID10'] = "421071170"
    df.loc[df['GEOID10']=='421071175', 'GEOID10'] = "421071190"
    df.loc[df['GEOID10']=='421071075', 'GEOID10'] = "421071070"
    df.loc[df['GEOID10']=='421071055', 'GEOID10'] = "421071060"
    df.loc[df['GEOID10']=='421071035', 'GEOID10'] = "421071050"
    df.loc[df['GEOID10']=='421071115', 'GEOID10'] = "421071120"
    df.loc[df['GEOID10']=='421071015', 'GEOID10'] = "421071020"
    df.loc[df['GEOID10']=='421071105', 'GEOID10'] = "421071100"
    df.loc[df['GEOID10']=='42107995', 'GEOID10'] = "42107990"
    # Pringle
    df.loc[df['GEOID10']=='420792275', 'GEOID10'] = "420792270"

    # Reading
    df.loc[df['GEOID10']=='420111095', 'GEOID10'] = "420111100"
    df.loc[df['GEOID10']=='420111185', 'GEOID10'] = "420111180"
    df.loc[df['GEOID10']=='420111285', 'GEOID10'] = "420111280"
    df.loc[df['GEOID10']=='420111305', 'GEOID10'] = "420111300"
    # Redbank
    df.loc[df['GEOID10']=='42005605', 'GEOID10'] = "42005600"
    # Richland
    df.loc[df['GEOID10']=='420172255', 'GEOID10'] = "420211500"
    # Robeson
    df.loc[df['GEOID10']=='420111398', 'GEOID10'] = "420111400"
    df.loc[df['GEOID10']=='420111412', 'GEOID10'] = "420111420"
    # Rockland
    df.loc[df['GEOID10']=='420111442', 'GEOID10'] = "420111140B"
    df.loc[df['GEOID10']=='420111438', 'GEOID10'] = "420111440"
    # Ruscombmanor
    df.loc[df['GEOID10']=='420111448', 'GEOID10'] = "420111450A"
    df.loc[df['GEOID10']=='420111452', 'GEOID10'] = "420111450"
    # Rush
    df.loc[df['GEOID10']=='421071225', 'GEOID10'] = "421071220"
    df.loc[df['GEOID10']=='421071235', 'GEOID10'] = "421071250"
    df.loc[df['GEOID10']=='421071255', 'GEOID10'] = "421071240"

    # Salem
    df.loc[df['GEOID10']=='420792315', 'GEOID10'] = "420792310"
    df.loc[df['GEOID10']=='420792325', 'GEOID10'] = "420792330"
    # Salisbury
    df.loc[df['GEOID10']=='420771052', 'GEOID10'] = "420771061"
    df.loc[df['GEOID10']=='420771015', 'GEOID10'] = "420771051"
    # Schuylkill
    df.loc[df['GEOID10']=='421071275', 'GEOID10'] = "421071270"
    # Scott East
    df.loc[df['GEOID10']=='42037595', 'GEOID10'] = ""
    # Scranton
    df.loc[df['GEOID10']=='420692205', 'GEOID10'] = "420692200"
    df.loc[df['GEOID10']=='420691675', 'GEOID10'] = "420691670"
    df.loc[df['GEOID10']=='420691665', 'GEOID10'] = "420691660"
    df.loc[df['GEOID10']=='420691625', 'GEOID10'] = "420691620"
    df.loc[df['GEOID10']=='420691615', 'GEOID10'] = "420691610"
    df.loc[df['GEOID10']=='420691575', 'GEOID10'] = "420691570"
    df.loc[df['GEOID10']=='420691535', 'GEOID10'] = "420691530"
    df.loc[df['GEOID10']=='420691435', 'GEOID10'] = "420691430"
    df.loc[df['GEOID10']=='420691455', 'GEOID10'] = "420691450"
    df.loc[df['GEOID10']=='420691385', 'GEOID10'] = "420691380"
    df.loc[df['GEOID10']=='420691365', 'GEOID10'] = "420691360"
    df.loc[df['GEOID10']=='420691325', 'GEOID10'] = "420691320"
    df.loc[df['GEOID10']=='420691315', 'GEOID10'] = "420691310"
    df.loc[df['GEOID10']=='420691525', 'GEOID10'] = "420691520"
    df.loc[df['GEOID10']=='420691725', 'GEOID10'] = "420691720"
    df.loc[df['GEOID10']=='420691605', 'GEOID10'] = "420691600"
    df.loc[df['GEOID10']=='420691775', 'GEOID10'] = "420691770"
    df.loc[df['GEOID10']=='420692195', 'GEOID10'] = "420692190"
    df.loc[df['GEOID10']=='420692125', 'GEOID10'] = "420692120"
    df.loc[df['GEOID10']=='420692085', 'GEOID10'] = "420692080"
    df.loc[df['GEOID10']=='420692025', 'GEOID10'] = "420692020"
    df.loc[df['GEOID10']=='420691935', 'GEOID10'] = "420691930"
    df.loc[df['GEOID10']=='420691925', 'GEOID10'] = "420692100"
    df.loc[df['GEOID10']=='420691875', 'GEOID10'] = "420691870"
    df.loc[df['GEOID10']=='420691865', 'GEOID10'] = "420691860"
    df.loc[df['GEOID10']=='420692005', 'GEOID10'] = "420692000"
    df.loc[df['GEOID10']=='420691845', 'GEOID10'] = "420691840"
    df.loc[df['GEOID10']=='420691820', 'GEOID10'] = "420691800"
    # Shaler
    df.loc[df['GEOID10']=='42003F150', 'GEOID10'] = "42003F142"
    # Shenandoah
    df.loc[df['GEOID10']=='421071375', 'GEOID10'] = "421071370"
    df.loc[df['GEOID10']=='421071355', 'GEOID10'] = "421071350"
    df.loc[df['GEOID10']=='421071345', 'GEOID10'] = "421071340"
    df.loc[df['GEOID10']=='421071365', 'GEOID10'] = "421071360"
    df.loc[df['GEOID10']=='421071335', 'GEOID10'] = "421071330"
    # Shickshinny
    df.loc[df['GEOID10']=='420792345', 'GEOID10'] = "420792350"
    # Silver Spring  (joined with North)
    # df.loc[df['GEOID10']=='420410', 'GEOID10'] = "42041700"          #mismatch
    # Sinking Spring
    df.loc[df['GEOID10']=='420111502', 'GEOID10'] = "420111502"
    # Skippack
    df.loc[df['GEOID10']=='420912762', 'GEOID10'] = "42091PR417"
    df.loc[df['GEOID10']=='420912748', 'GEOID10'] = "420912750"
    df.loc[df['GEOID10']=='420912755', 'GEOID10'] = "420912760"
    # Solebury
    df.loc[df['GEOID10']=='420172327', 'GEOID10'] = "420172325"
    df.loc[df['GEOID10']=='420172323', 'GEOID10'] = "420172320"
    # South Abington
    df.loc[df['GEOID10']=='420692275', 'GEOID10'] = "420692132"
    df.loc[df['GEOID10']=='420692255', 'GEOID10'] = "420692131"
    df.loc[df['GEOID10']=='420692252', 'GEOID10'] = "420692139"
    # South Hampton
    df.loc[df['GEOID10']=='42055546', 'GEOID10'] = "42055551"
    df.loc[df['GEOID10']=='42009355', 'GEOID10'] = "42009350"
    # South Heidelberg
    df.loc[df['GEOID10']=='420111477', 'GEOID10'] = "420111475"
    # Southhampton
    df.loc[df['GEOID10']=='42041795', 'GEOID10'] = "42041790"
    df.loc[df['GEOID10']=='42055546', 'GEOID10'] = "42055551"
    df.loc[df['GEOID10']=='42055543', 'GEOID10'] = "42055540"
    # South Fayette
    df.loc[df['GEOID10']=='42003F392', 'GEOID10'] = "42003F391"
    df.loc[df['GEOID10']=='42003F395', 'GEOID10'] = "42003F401"
    df.loc[df['GEOID10']=='42003F397', 'GEOID10'] = "42003F411"
    df.loc[df['GEOID10']=='42003F405', 'GEOID10'] = "42003F421"
    df.loc[df['GEOID10']=='42003F408', 'GEOID10'] = "42003F431"
    df.loc[df['GEOID10']=='42003F415', 'GEOID10'] = "42003F441"
    df.loc[df['GEOID10']=='42003F417', 'GEOID10'] = "42003PR1319"
    df.loc[df['GEOID10']=='42003F425', 'GEOID10'] = "42003PR1330"
    df.loc[df['GEOID10']=='42003F427', 'GEOID10'] = "42003PR1321"
    df.loc[df['GEOID10']=='42003F435', 'GEOID10'] = "42003F442"
    df.loc[df['GEOID10']=='42003F437', 'GEOID10'] = "42003PR1318"
    df.loc[df['GEOID10']=='42003F445', 'GEOID10'] = "42003PR1320"
    # Spring
    df.loc[df['GEOID10']=='420111557', 'GEOID10'] = "420111555"
    df.loc[df['GEOID10']=='42027595', 'GEOID10'] = "42027PR88"
    df.loc[df['GEOID10']=='42027605', 'GEOID10'] = "42027PR89"
    df.loc[df['GEOID10']=='420111574', 'GEOID10'] = "420111510B"
    df.loc[df['GEOID10']=='420111576', 'GEOID10'] = "420111511"
    df.loc[df['GEOID10']=='420111578', 'GEOID10'] = "420111512"
    df.loc[df['GEOID10']=='42027582', 'GEOID10'] = "42027580"
    df.loc[df['GEOID10']=='42047295', 'GEOID10'] = "42047290"
    # St. Clair
    df.loc[df['GEOID10']=='421071475', 'GEOID10'] = "421071470"
    df.loc[df['GEOID10']=='421071465', 'GEOID10'] = "421071490"
    df.loc[df['GEOID10']=='421071455', 'GEOID10'] = "421071450"
    # Strasburg
    df.loc[df['GEOID10']=='420711735', 'GEOID10'] = "420711730"
    # Swoyersville
    df.loc[df['GEOID10']=='420792445', 'GEOID10'] = "420792440"
    df.loc[df['GEOID10']=='420792425', 'GEOID10'] = "420792420"
    # Tamaqua
    df.loc[df['GEOID10']=='421071525', 'GEOID10'] = "421071540" #north
    df.loc[df['GEOID10']=='421071535', 'GEOID10'] = "421071550" #south
    df.loc[df['GEOID10']=='421071515', 'GEOID10'] = "421071510"
    df.loc[df['GEOID10']=='421071505', 'GEOID10'] = "421071500"
    # Taylor
    df.loc[df['GEOID10']=='420692295', 'GEOID10'] = "420692290"
    df.loc[df['GEOID10']=='420692315', 'GEOID10'] = "420692310"
    # Thornbury
    df.loc[df['GEOID10']=='420452912', 'GEOID10'] = "420292059"
    df.loc[df['GEOID10']=='420291136', 'GEOID10'] = "420452925"
    df.loc[df['GEOID10']=='420291133', 'GEOID10'] = "420452915"
    df.loc[df['GEOID10']=='420452916', 'GEOID10'] = "420292060"
    # Towamenchin
    df.loc[df['GEOID10']=='420913001', 'GEOID10'] = "420913000"
    df.loc[df['GEOID10']=='420912973', 'GEOID10'] = "420913012"
    df.loc[df['GEOID10']=='420913025', 'GEOID10'] = "420913010"
    # Towamensing
    df.loc[df['GEOID10']=='42025432', 'GEOID10'] = "42025436"
    df.loc[df['GEOID10']=='42025428', 'GEOID10'] = "42025435"
    # Tower City
    df.loc[df['GEOID10']=='421071565', 'GEOID10'] = "421071560"
    # Union
    df.loc[df['GEOID10']=='421251745', 'GEOID10'] = "421251740"
    # Upper Allen
    df.loc[df['GEOID10']=='42041838', 'GEOID10'] = "42041826"
    df.loc[df['GEOID10']=='42041823', 'GEOID10'] = "42041800"
    df.loc[df['GEOID10']=='42041819', 'GEOID10'] = "42041810"
    df.loc[df['GEOID10']=='42041803', 'GEOID10'] = "42041805"
    # Upper Darby
    df.loc[df['GEOID10']=='420453365', 'GEOID10'] = "3--11"
    df.loc[df['GEOID10']=='420453362', 'GEOID10'] = "420453360"
    df.loc[df['GEOID10']=='420453810', 'GEOID10'] = "7--12"
    df.loc[df['GEOID10']=='420912815', 'GEOID10'] = "5--3"
    df.loc[df['GEOID10']=='420913078', 'GEOID10'] = "420913080"
    df.loc[df['GEOID10']=='420912873', 'GEOID10'] = "420912875"
    # Upper Macungie
    df.loc[df['GEOID10']=='420771255', 'GEOID10'] = "D--5"
    df.loc[df['GEOID10']=='420771222', 'GEOID10'] = "420771220"
    # Upper Mahantongo
    df.loc[df['GEOID10']=='421071625', 'GEOID10'] = "421071620"
    # Upper Paxton
    df.loc[df['GEOID10']=='420431311', 'GEOID10'] = "42043PR160"
    df.loc[df['GEOID10']=='420431313', 'GEOID10'] = "42043PR159"
    # Upper Tyrone
    df.loc[df['GEOID10']=='420511045', 'GEOID10'] = "420511050"
    # Upper Uwchlan
    df.loc[df['GEOID10']=='420291316', 'GEOID10'] = "420292053"
    df.loc[df['GEOID10']=='420291312', 'GEOID10'] = "420291315"
    df.loc[df['GEOID10']=='420291308', 'GEOID10'] = "420291310"
    # Warrington
    df.loc[df['GEOID10']=='420172742', 'GEOID10'] = "420172740"
    df.loc[df['GEOID10']=='420172783', 'GEOID10'] = "420172782"
    df.loc[df['GEOID10']=='420172785', 'GEOID10'] = "420172784"
    df.loc[df['GEOID10']=='420172787', 'GEOID10'] = "420172786"
    # Warwick
    df.loc[df['GEOID10']=='420172812', 'GEOID10'] = "420172815"
    df.loc[df['GEOID10']=='420172827', 'GEOID10'] = "420172801"
    # Washington
    df.loc[df['GEOID10']=='420511082', 'GEOID10'] = "420511080"
    # Wayne
    df.loc[df['GEOID10']=='421071672', 'GEOID10'] = "421071670"
    df.loc[df['GEOID10']=='421071678', 'GEOID10'] = "421071683"
    df.loc[df['GEOID10']=='421071682', 'GEOID10'] = "421071671"
    # West Bradford
    df.loc[df['GEOID10']=='420291431', 'GEOID10'] = "420291430"
    df.loc[df['GEOID10']=='420291465', 'GEOID10'] = "420292057"
    # West Hazleton
    df.loc[df['GEOID10']=='420792517', 'GEOID10'] = "420792525"
    df.loc[df['GEOID10']=='420792497', 'GEOID10'] = "420792495"
    df.loc[df['GEOID10']=='420792477', 'GEOID10'] = "420792485"
    # West Lampeter
    df.loc[df['GEOID10']=='420711987', 'GEOID10'] = "420711990"
    # West Mahonoy
    df.loc[df['GEOID10']=='421071725', 'GEOID10'] = "421071730"
    # West Penn
    df.loc[df['GEOID10']=='421071772', 'GEOID10'] = "421071775"
    df.loc[df['GEOID10']=='421071766', 'GEOID10'] = "421071760"
    df.loc[df['GEOID10']=='421071762', 'GEOID10'] = "421071770"

    # West Pittston
    df.loc[df['GEOID10']=='420792555', 'GEOID10'] = "420792550"
    df.loc[df['GEOID10']=='420792565', 'GEOID10'] = "420792560"
    # West Wyoming
    df.loc[df['GEOID10']=='420792595', 'GEOID10'] = "420792590"
    # Westfield
    df.loc[df['GEOID10']=='42117445', 'GEOID10'] = "42117440"
    # White
    # df.loc[df['GEOID10']=='42063702', 'GEOID10'] = "42063680"         #mismatch
    # Whitehall
    df.loc[df['GEOID10']=='420771425', 'GEOID10'] = "420771420"
    # Whitpain
    df.loc[df['GEOID10']=='420913865', 'GEOID10'] = "420913643"
    df.loc[df['GEOID10']=='420913812', 'GEOID10'] = "420913811"
    # Wilkes-Barre City
    df.loc[df['GEOID10']=='420792885', 'GEOID10'] = "420792810"
    df.loc[df['GEOID10']=='420793045', 'GEOID10'] = "420792890"
    df.loc[df['GEOID10']=='420793020', 'GEOID10'] = "420792940"
    df.loc[df['GEOID10']=='420793015', 'GEOID10'] = "420792960"
    df.loc[df['GEOID10']=='420792685', 'GEOID10'] = "420793010"
    df.loc[df['GEOID10']=='420792935', 'GEOID10'] = "420792830"
    df.loc[df['GEOID10']=='420792700', 'GEOID10'] = "420793090"
    df.loc[df['GEOID10']=='420792725', 'GEOID10'] = "420792630"
    df.loc[df['GEOID10']=='420792745', 'GEOID10'] = "420792710"
    df.loc[df['GEOID10']=='420792985', 'GEOID10'] = "420792950"
    df.loc[df['GEOID10']=='420792765', 'GEOID10'] = "420792740"
    df.loc[df['GEOID10']=='420792787', 'GEOID10'] = "420792760"
    df.loc[df['GEOID10']=='420792805', 'GEOID10'] = "420792860"
    df.loc[df['GEOID10']=='420792815', 'GEOID10'] = "420792840"
    df.loc[df['GEOID10']=='420792845', 'GEOID10'] = "420792785"
    df.loc[df['GEOID10']=='420792715', 'GEOID10'] = "420792990"
    df.loc[df['GEOID10']=='420792755', 'GEOID10'] = "420792680"

    return(df)

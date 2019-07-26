import sys
import csv
import re

with open(sys.argv[1]) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	list_rows = list()
	for row in readCSV:
		list_rows.append(row)

	domain = (re.search("@[\w.]+", list_rows[1][0])).group()
	domain = domain[1:-4]
	print("The client is {}".format(domain.upper()))

	if domain == 'pinnacleag':
		print('AVAILABLE CLIENT IDs:')
		

	elif domain == 'teasdalefoods':
		print('AVAILABLE CLIENT IDs:')
		print("TEAS01	TEASDALE LATIN FOODS	RICK PIKE")

	elif domain == 'rexelusa':
		print('AVAILABLE CLIENT IDs:')
		print("REXL01	MD, OH, NC, VA, PA, NY")
		print("REXL02	AL, GA, MO, KY, IL, TN, FL, FY, LA, MS")
		print("REXL03	AR, CT, OR, AZ, LA, TX, MA, CA, ME, WA, NH, CT, CO , OK, Capitol Light")

	elif domain == 'cerner':
		print('AVAILABLE CLIENT IDs:')
		print("CERN01	CERNER, INC 	EXTENDED CARE		JEFF O'HAIR		Robert Bart")
		print("CERN02	CERNER, INC 	HEALTH SERVICE		KATHY ZROWKA")
		print("CERN03	CERNER 			PHYSICIAN PRACTICE	JEFF O'HAIR")
		print("CERN04	CERNER 			CLIENT DEVELOPMENT	JEFF O'HAIR")
		print("CERN05	CERNER INC 		RETAIL PHARMACY		JEFF O'HAIR")
		print("CERN07	CERNER 			CANADA				JEFF O'HAIR 	Kathy.hopkins@cerner.com")
		print("CERN08	CERNER 			NON-PROVIDER")

	elif domain == 'pioneer':
		print('AVAILABLE CLIENT IDs:')
		print("PINN01	PINNACLE AG	LAMAR TAYLOR")
		print("PINN02	PINNACLE AG	MIKE CLEVELAND")
		print("PINN03	PINNACLE AG	LAMAR TAYLOR")
		print("PINN04	PINNACLE AG	LAMAR TAYLOR")
		print("PINN05	PINNACLE AG	LAMAR TAYLOR")
		print("PINN06	PINNACLE AG	LAMAR TAYLOR")
		print("PINN07	PINNACLE AG	MIKE CLEVELAND		Nick Koski, Sandy Litchfield")

	elif domain == 'landolakes':
		print('AVAILABLE CLIENT IDs:')
		print("LOLI01	LAND O LAKES, INC - PURINA		TERRY LEFEVRE		Donna Arnone, Lori Roursseau")
		print("LOLI03	LAND O LAKES, INC - WINFIELD	CONNIE WEILAND		Ann Bickelhaupt")
		print("LOLI04	LAND O LAKES, INC - INT'L		ANGIE VANEK")
		print("LOLI05	LAND O LAKES, INC - PURINA		SANDY STEARNS")
		print("LOLI07	LAND O LAKES, INC - DOMESTIC	ANGIE VANEK")
		print("LOLI09	LAND O LAKES, INC - WINFIELD	Hausladen-Hess, Marcy")
		print("LOLI10	LAND O LAKES, INC - WINFIELD	DAVID BOUCHER")
		print("LOLI11	LAND O LAKES, INC - WINFIELD	LISA ROTH")
		print("LOLI13	NUTRA BLEND LLC					DARREN SWISHER")
		print("LOLI14	LAND O LAKES, INC				DEB CABALLERO")
		print("LOLI15	NUTRA BLEND LLC					CHRISTINA VALER")
		print("LOLI16	LAND O LAKES, INC - WINFIELD	NATALIE ERICKSON")
		print("LOLI17	LAND O LAKES, INC - PURINA		RICHARD CALL")
		print("LOLI18	LAND O LAKES, INC EMPLOYEE		BARB HALL")
		print("LOLI20	LAND O LAKES - WINFIELD			TERRY LEFEVRE")
		print("LOLI21	LAND O LAKES - WINFIELD			TERRY LAFEVRE")
		print("LOLI22	LAND O LAKES, INC - WINFIELD	SANDY STEARNS")
		print("LOLI23	LAND O LAKES - WINFIELD			RICHARD CALL")
		print("LOLI24	LAND O LAKES - DAIRY FOODS		RON KNUTSON")
		print("LOLI25	LAND O LAKES - WINFIELD			TERRY LAFEVRE")
		print("LOLI26	LAND O LAKES - DAIRY FOODS		Todd Paskett")
		print("LOLI27	LAND O LAKES, INC PURINA		ANGIE VANEK")
		print("LOLI28	LAND O LAKES, INC - PURINA		ANDREA SPARROW")
		print("LOLI29	LAND O LAKES - WINFIELD			ANDREA SPARROW")
		print("LOLI30	LAND O LAKES - PURINA			CONNIE WEILAND		Ann Bickelhaupt")
		print("LOLI31	LAND O LAKES - WINFIELD			Angie Vanek")
		print("LOLI32	LAND O LAKES, INC - PURINA		LISA ROTH")
		print("LOLI33	LAND O LAKES, INC - PURINA		Hausladen-Hess, Marcy")
		print("LOLI34	LAND O LAKES - WINFIELD			JAMES WEITBRECHT")
		print("LOLI35	LAND O LAKES - WINFIELD			JEREMY STAHL")
		print("LOLI36	LAND O LAKES, INC PURINA		JEREMY STAHL")
		print("LOLI37	LAND O LAKES, INC - PURINA		JENNA GRIFFITHS")
		print("LOLI38	LAND O LAKES - WINFIELD			JENNA GRIFFITHS")
		print("LOLI39	LAND O LAKES, INC - PURINA		SUE COYLE-AVARITT")
		print("LOLI40	LAND O LAKES - WINFIELD			SUE COYLE-AVARITT")

	client_id = str(raw_input("\nThe client ID will be: "))
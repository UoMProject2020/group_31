import json

count=0
#Hashtags of interest
interested_text = ['accidents' , 'roadaccident' , 'fatality' , 'carcrash' , 'roadrage' , 'speedkills' , 'roadinjury' , 'roadsafety' , 'rashdriving','accident','caraccident','distracteddriving','drivesafe','car_accident','road_safety','distracted_driving','car_driving','rash_driving','speedingkills','speeding_kills']
with open('Enter path of data file',encoding='utf-8') as f:
	for line in f:
			count = count+1
			line  = line.strip()
			if line.endswith(','):
				try:
					tweet=json.loads(line[:-1],strict=False)
				except:
					print("Invalid json")
			elif line[-2:]=='}}':
				try:
					tweet=json.loads(line,strict=False)
				except:
					print("Invalid json")
			elif line[-2]==']}' and len(line)>2:
				try:
					tweet=json.loads(line[:-2],strict=False)
				except:
					print("Invalid json")
			else:
				continue
			if len(tweet['doc']['entities']['hashtags'])>0:
				for i in tweet['doc']['entities']['hashtags']:
					if i['text'].lower() in interested_text:
						print("\n")
						print(tweet['doc']['entities']['hashtags'])
						with open('filtered_twitter-melb.json', 'a+', encoding='utf8') as of: #Writing tweets of interest in a file
							of.write(str(tweet))
							of.write("\n")			
	print(count) #Number of tweets


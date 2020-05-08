import json
import sys
import getopt 

def filter(input_file):
	count=0
	#Hashtags of interest
	interested_text = ['auspol']
	with open(input_file,encoding='utf-8') as f:
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

def main(argv):
	input_file = ''
	try:
		opts, args = getopt.getopt(argv,"i:")
	except getopt.GetoptError as error:
		print(error)
		print_usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-i"):
		#Retrieving the path of data file
			input_file = arg        
	filter(input_file)

# Run the code
if __name__ == "__main__":
	main(sys.argv[1:])  
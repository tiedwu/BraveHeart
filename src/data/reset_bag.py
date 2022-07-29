# reset bag item
import json

def main():
	file = 'profile.json'
	with open(file, 'r') as f:
		data = json.load(f)

	print(data)
	data['bag'] = []
	with open(file, 'w', encoding='utf-8') as f:
		json.dump(data, f, indent=4, ensure_ascii=False)
	print('Done')

if __name__ == '__main__':
	main()

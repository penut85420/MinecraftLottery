import json

def json_formatting():
    with open('./rewards.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)

    with open('./rewards.json', 'w', encoding='UTF-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    json_formatting()

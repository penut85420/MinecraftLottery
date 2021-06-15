import json

def main():
    with open('./REWARDS.md', 'w', encoding='UTF-8') as fout:
        with open('./rewards.json', 'r', encoding='UTF-8') as finn:
            reward_table = json.load(finn)
            for reward in reward_table['tiers']:
                print(f"## {reward['display'][4:]}", file=fout)
                for reward_list in reward_table[reward['name']]:
                    item = reward_list['item']
                    item = item.split('{')[0]
                    item = item.split(' ')[0]
                    item = item.replace('minecraft:', '')
                    print(f"+ {reward_list['name'][2:]} ({item})", file=fout)
                    # print(f'/give @p {n["item"]}')
                print(file=fout)

    with open('./REWARDS.md', 'r', encoding='UTF-8') as finn:
        txt = f'# 大歐派麥塊一番賞獎勵表\n\n{finn.read().strip()}\n'

    with open('./REWARDS.md', 'w', encoding='UTF-8') as fout:
        fout.write(txt)

if __name__ == '__main__':
    main()

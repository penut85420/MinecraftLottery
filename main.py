import re
import json
import random
from collections import Counter

with open('./rewards.json', 'r', encoding='UTF-8') as f:
    rewards_table = json.load(f)
    reward_weights = [tier['weight'] for tier in rewards_table['tiers']]
    reward_level = [tier['name'] for tier in rewards_table['tiers']]
    reward_show = {tier['name']: tier['display'] for tier in rewards_table['tiers']}

def get_reward():
    level = random.choices(reward_level, weights=reward_weights)[0]
    return random.choice(rewards_table[level]), reward_show[level]

with open('rewards.log', 'w', encoding='UTF-8') as f:
    f.write(str(Counter([get_reward()[1] for _ in range(1000)])))

while True:
    inn = input()
    m = re.search(r'^\[\d+:\d+:\d+\] \[Server thread/INFO\]: \[@\] (.+) 戳了一下歐派!', inn)
    m10 = re.search(r'^\[\d+:\d+:\d+\] \[Server thread/INFO\]: \[@\] (.+) 戳了十下歐派!', inn)
    if m:
        name = m.group(1)
        print(f'clear {name} minecraft:emerald 1')
        reward, show = get_reward()
        reward_name, reward_item = reward['name'], reward['item']
        print(f'give {name} {reward_item}')
        print(f'say {name} 獲得{show}{reward_name}§f!')
    elif m10:
        name = m10.group(1)
        print(f'clear {name} minecraft:emerald_block 1')
        rewards = [get_reward() for _ in range(10)]
        for reward, _ in rewards:
            reward_item = reward['item']
            print(f'give {name} {reward_item}')

        reward_names = sorted([f"{show}{reward['name']}" for reward, show in rewards])
        reward_names = '§f、'.join(reward_names)

        print(f'say {name} 獲得{reward_names}§f!')

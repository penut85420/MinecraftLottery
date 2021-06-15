import json

"""
Color Formatting
§0	black	    §9	blue
§1	dark_blue	§a	green
§2	dark_green	§b	aqua
§3	dark_aqua	§c	red
§4	dark_red	§d	light_purple
§5	dark_purple	§e	yellow
§6	gold	    §f	white
§7	gray	    §g	minecoin_gold
§8	dark_gray
"""

def gen_item():
    name = '§d超究極大歐派黑金宝鐘マリン'
    item = r"""/give @p netherite_hoe{Damage:0,AttributeModifiers:[{AttributeName:"generic.attack_damage",Amount:12,Slot:mainhand,Name:"generic.attack_damage",UUID:[I;-121515,6561,203740,-13122]},{AttributeName:"generic.attack_speed",Amount:2,Slot:mainhand,Name:"generic.attack_speed",UUID:[I;-121515,6661,203740,-13322]}],display:{Name:'[{"text":" ","italic":false},{"text":"超究極大歐派黑金宝鐘マリン","color":"yellow"}]',Lore:['[{"text":"","italic":false}]','[{"text":"海賊なら Yo-Ho! 踊れ叫べ Yo-Ho!","italic":false,"color":"red"}]','[{"text":"さぁ今旗のもとへ","italic":false,"color":"red"}]','[{"text":"宝鐘海賊団「出航～！」","italic":false,"color":"red"}]','[{"text":"Ahoy! Ahoy! Ahoy! Ahoy!","italic":false,"color":"red"}]','[{"text":"踊る Ahoy! に見る Ahoy! ホイホーイ！","italic":false,"color":"red"}]','[{"text":"Ahoy! Ahoy! Ahoy! ホイホイホーイ！","italic":false,"color":"red"}]','[{"text":"「全速前進だ〜！」","italic":false,"color":"red"}]']},Enchantments:[{id:efficiency,lvl:10},{id:fortune,lvl:10},{id:sharpness,lvl:10},{id:unbreaking,lvl:10},{id:mending,lvl:1}]} 1"""

    item = item.replace('/give @p ', '')

    full = {
        'name': name,
        'item': item
    }

    with open('item.json', 'w', encoding='UTF-8') as f:
        json.dump(full, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    gen_item()

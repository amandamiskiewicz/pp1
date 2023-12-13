import re

text = "Forests cover about 30,5% of Poland's land area based on international standards. Its overall percentage is still increasing. Forests of Poland are managed by the national program of reforestation (KPZL), aiming at an increase of forest-cover to 33% in 2050. The richness of Polish forest (per SoEF 2011 statistics) is more than twice as high as European average (with Germany and France at the top), containing 2.304 billion cubic meters of trees. The largest forest complex in Poland is Lower Silesian Wilderness. More than 1% of Poland's territory, 3,145 square kilometers (1,214 sq mi), is protected within 23 Polish national parks. Three more national parks are projected for Masuria, the Polish Jura, and the eastern Beskids. In addition, wetlands along lakes and rivers in central Poland are legally protected, as are coastal areas in the north. There are over 120 areas designated as landscape parks, along with numerous nature reserves and other protected areas (e.g. Natura 2000)."

numbers = re.findall(r'\b\d+?\b', text)

print(numbers)
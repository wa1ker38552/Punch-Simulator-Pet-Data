# Punch-Simulator-Pet-Data
Statistics for pet hatching in Punch Simulator

Made a script to check egg hatching statistics for FOREST 1 EGG in punch simulator. I had a feeling luck boosts did jack shit so I made a script to check by hatching eggs hundreds of times and getting the statistics for the probability of hatching each pet. The program uses pixel colors to locate and detect which pet was hatched. This script will not work on your computer. You have to edit the ratios so that they match the ones on you screen.

Standard error =  `sqrt[p * (1 - p) / n]` <br>
Margin of error =  `z * standard_error` <br>
Trials = `n = (z^2 * p * (1 - p)) / margin_of_error^2`<br>
where `p` is probability, `n` is number of trials, `z` is accuracy. You can subtract accuracy from 1 to find margin of error. <br>
To test legendary pet hatch chances, you only need to run 801 trials to determine probability with 90% accuracy or 10% margin of error

## RESULTS
**FOREST EGG** <br>
Original stats are 30% Uncommon, 40% Rare, 29% Mythic, 1% Legendary

**96% Luck** <br>
1455 eggs <br>

437 Uncommon (30%) <br>
558 Rare (40%) <br>
410 Mythic (28%) <br>
20 Legendary (1%) <br>

**401% Luck** <br>
721 eggs <br>

225 Uncommon (31%) <br>
279 Rare (39%) <br> 
215 Mythic (30%) <br>
2 Legendary (<1%) <br>

**156% +x2 Luck** <br>
910 eggs <br>

261 Uncommon (29%) <br>
372 Rare (41%) <br> 
262 Mythic (29%) <br>
14 Legendary (2%) <br>

**CAVE EGG** <br>
Original stats are 45% Common, 37% Uncommon, 15% Rare, 2% Mythic, 1% Legendary

**116% Luck**<br>
1370 eggs <br>

575 Common (42%) <br>
540 Uncommon (39%) <br>
212 Rare (15%) <br>
27 Mythic (2%) <br>
16 Legendary (1%) <br>

**421% Luck**<br>
3650 eggs <br>

1668 Common (46%) <br>
1316 Uncommon (36%) <br>
550 Rare (15%) <br>
78 Mythic (2%) <br>
38 Legendary (1%) <br>



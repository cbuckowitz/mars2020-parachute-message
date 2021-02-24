# NASA Mars 2020 Perseverance Rover Parachute Riddle

[NASA's Mars 2020 Perseverance rover](https://mars.nasa.gov/mars2020/) used a parachute during landing on mars. That parachute featured an intricate design, which I did not pay any attention to, when I first watched the [video of the descent and touchdown](https://www.youtube.com/watch?v=4czjS9h4Fpg). Some time later, during some press conference, NASA gave a hint, there would be a secret message on the parachute. Picked this up in some news article about the parachute code and how it was solved within hours. So that did pick my interest and looking at the [NASA coverage](https://mars.nasa.gov/news/8870/nasas-mars-perseverance-rover-provides-front-row-seat-to-landing-first-audio-recording-of-red-planet/), armed with the spoilers from the news, I started my attempt at decoding that unresistable secret.

## What does the parachute look like anyway

NASA thankfully puts a lot of [raw images](https://mars.nasa.gov/mars2020/multimedia/raw-images/) on their mission site. The chute is visible in the video coverage as well, but well, I grabbed some of those raws.

<img src="https://mars.nasa.gov/mars2020-raw-images/pub/ods/surface/sol/00002/ids/edr/browse/edl/EAF_0002_0667110409_242ECV_N0010052EDLC00002_0010LUJ01_1200.jpg" alt="drawing" width="200"/>

<img src="https://mars.nasa.gov/mars2020-raw-images/pub/ods/surface/sol/00002/ids/edr/browse/edl/EAF_0002_0667110403_243ECV_N0010052EDLC00002_0010LUJ01_1200.jpg" alt="drawing" width="200"/>

<img src="https://mars.nasa.gov/mars2020-raw-images/pub/ods/surface/sol/00002/ids/edr/browse/edl/EAF_0002_0667110418_707ECV_N0010052EDLC00002_0010LUJ01_1200.jpg" alt="drawing" width="200"/>

The pattern of the chute is clearly visible, but some part of the chute gets obscured. Fortunately the chute is turning and i photoshopped a bit to get a view of the complete parachute.

![complete parachute](Overlay.png)

 Getting all giddy looking at the parachute and counting colors, I moved on to draw some lines and numbers on that.

![sketched parachute](Sketched.png)

The chute consists of 80 segments and the pattern is divided into 4 circular stretches. Well, I picked the top for starting the numbering by random choice.

Going with the news article spoilers, taking the pattern and colors as bits, doing some tedious counting, gives the following data block.

```
seg    00000000011111111112222222222333333333344444444445555555555666666666677777777778
seg    12345678901234567890123456789012345678901234567890123456789012345678901234567890

rings inner to outer (W)hite, (R)ed
ring 0 WWWWWWWRWWWWWWWWWWWRWWWWWRWWRWWWWWWWWRWRWWWRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
ring 1 WWWWWRWRWWWWWWWRRWWRWWWRRRRRRRRRRRRRRRRRWWWWWWRRWRWWWWWWRWWRWWWWWWWRRRWWWWWWRWWW
ring 2 WWWRRRRRRRRRRRRRRRRRWWWWWRWRWWWWWWWWRWWWWWWWWWRWWRWWWWWWRRRWWWWWWWWRRRWWWWWRWWRR
outer  WWWWRWWWRWWWWWWWRWRRWWWWRRRWRWWWWWWWRRRWWWWRRRWRRWWWWWWWRWRWWWWWWRRRRRWWWWWRWRRR


rings inner to outer White(0), Red(1)
1ing 0 00000001000000000001000001001000000001010001111111111111111111111111111111111111
1ing 1 00000101000000011001000111111111111111110000001101000000100100000001110000001000
1ing 2 00011111111111111111000001010000000010000000001001000000111000000001110000010011
oute1  00001000100000001011000011101000000011100001110110000000101000000111110000010111
```



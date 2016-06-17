
### Web Application Architecture

En stor del af internettet idag, handler om at give de rigtige brugere adgang til det rigtige data, og dertil undgå at de forkerte brugere kan få adgang til andres private data.

Når et HTTP request rammer en server, vil forskellige komponenter bliver kaldt for at samle en respons, disse komponenter vil tage en varierende mængde af tid, alt efter mængden af den data der berøres, altså mere data = højere responstid.

Dette betyder at sårbare sidder konsekvent vil leake privat information om mængden af data der berøres, every time.

Artiklen beskriver hvordan de undersøgte ting som Content-Length eller Chunked Encoding var at foretrække, det viste sig at sider som var sårbare leakede information i begge tilfælde.

Kort sagt vil den underliggende struktur på web-arkitektur idag, leake privat data, fordi det offentligt tilgængelige HTTP respons vil i nogle tilfælde være baseret på privat data.



### Direct Timing Attacks

Når man tager tjekker tiden det tager fra et request er sendt, til en respons begynder at blive modtaget, kan det gøres overraskende nøjagtigt, faktisk i del-millisecond.

Der er kun to store faktorer man skal tage højde for, hvoraf det første er netværks tilstanden, og det andet er server-load.

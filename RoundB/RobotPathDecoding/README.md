# Robot Path Decoding 

Your country's space agency has just landed a rover on a new planet, which can be thought of as a grid of squares containing 109 columns (numbered starting from 1 from west to east) and 109 rows (numbered starting from 1 from north to south). Let (w, h) denote the square in the w-th column and the h-th row. The rover begins on the square (1, 1).

The rover can be maneuvered around on the surface of the planet by sending it a program, which is a string of characters representing movements in the four cardinal directions. The robot executes each character of the string in order:

- N: Move one unit north.

- S: Move one unit south.

- E: Move one unit east.

- W: Move one unit west

## Testcases 


    SSSEEE -> 4 4
    
    N -> 1 1000000000
    
    N3(S)N2(E)N -> 3 1
    
    2(3(NW)2(W2(EE)W)) -> 3 999999995
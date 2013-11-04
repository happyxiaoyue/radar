#!/usr/bin/env python3
# -*- coding: utf-8 -*-

gEchoLineCountAFrame = 2048
gPI = 3.1415926

gRangeTable = {
    "50m":      (50,    0.12),
    "75m":      (75,    0.18),  
    "100m":     (100,   0.24),  
    "1/8nm":    (231.5, 0.73),  
    "1/4nm":    (463.0, 0.85),  
    "1/2nm":    (926,   1.69),  
    "3/4nm":    (1389,  1.69),  
    "1nm":      (1852,  1.69),  
    "1.5nm":    (2778,  2.44),  
    "2nm":      (3704,  2.44),  
    "3nm":      (5556,  7.93),  
    "4nm":      (7408,  8.55),  
    "6nm":      (11112, 8.55),  
    "8nm":      (14816, 12.82), 
    "12nm":     (22224, 12.82), 
    "16nm":     (29632, 12.82), 
    "24nm":     (44448, 12.82), 
    "32nm":     (59264, 12.82) 
}

def PrintVal():
    print("gRangeTable:", end = "")
    print(gRangeTable)
    print("gEchoLineCountAFrame:", end = "")
    print(gEchoLineCountAFrame)
    print("gPI", end = "")
    print(gPI)

if __name__ == '__main__':
    PrintVal()





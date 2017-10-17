import helper
import math

def JitMaker(mode, numberN, angleZX, angleZY):
    jit = 'N'+ str(numberN);
    f = open('jit.txt', 'w')
    X = 15;
    Y= 16;
    Z= 17;
    cosZX = math.cos(helper.DegToRad(angleZX));
    sinZX = math.sin(helper.DegToRad(angleZX));
    cosZY = math.cos(helper.DegToRad(angleZY));
    sinZY = math.sin(helper.DegToRad(angleZY));
    for case in helper.switch(mode):
        if case('U'): jit = (jit + ' G01' + ' X=' + str(X) +
                    ' Y=' + str(Y)+ ' Z=' + str(Z) +
                    ' A=45 B=0 C=90 F10000 \n' )
        numberN +=10
        jit = (jit + 'N'+ str(numberN) + ' G01' + ' X=' + str(X)
               + ' Y-' + str(Y)+ ' Z=' + str(Z) +
               ' A=45 B=0 C=90 F10000 \n')
        numberN +=10
        jit = (jit + 'N'+ str(numberN) + ' G01' + ' X=' + str(X) +
               ' Y=' + str(Y)+ ' Z=' + str(Z) +
               ' A=45 B=0 C=90 F10000 \n')
        break
        if case('D'): pass
        break
        if case('DU'): pass
        break
        if case():  print('Exeption') # default

    f.write(jit);
    f.close();
    return jit



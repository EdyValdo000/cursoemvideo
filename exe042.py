lineSegment1 = float(input('1º segmento: '))
lineSegment2 = float(input('2º segmento: '))
lineSegment3 = float(input('3º segmento: '))

if lineSegment1 + lineSegment2 > lineSegment3 and lineSegment3 + lineSegment2 > lineSegment1 and lineSegment1 + lineSegment3 > lineSegment2:
    print('Com os segmentos podes formar um triângulo',end=' ')
    if lineSegment1 == lineSegment2 == lineSegment3:
        print('\033[34;1mEquilátero\033[m')
    elif lineSegment1 != lineSegment2 != lineSegment3 != lineSegment1:
        print('\033[34;1mIsóisceles\033[m')
    else:
        print('\033[34;1mEscaleno\033[m')
else:
    print('\033[31;1mCom esses segmentos não formas um triângulo\033[m')
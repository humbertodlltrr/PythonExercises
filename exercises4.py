import time
import random
import math
from functools import reduce

def multOf3And5():
    upto = 1000
    tot = 0
    i = 3
    while i < upto:
        tot = tot + i
        i = i+3
    i = 5
    while i < upto:
        if i%3 != 0:
            tot = tot + i
        i = i+5
    print(tot)

def evenFibNums():
    top = 4000000
    i = 1
    last = 0
    fib = 0
    while i < top:
        if i%2 == 0:
            fib = fib + i
        tmp = i
        i = i + last
        last = tmp
    print (fib)

def largPrimFact(n):
    while n%2 == 0 and n != 2:
        n = int(n/2)
    if isPrime(n):
        return n
    else:
        for i in range(3,n,2):
            if isPrime(i):
                while n%i == 0:
                    if n == i:
                        return n
                    else:
                        n = int(n/i)

def largPalinProd():
    top = 0
    for i in range(100,1000):
        for j in range(100,1000):
            if isPalindrome(i*j):
                top = max(top,i*j)
    print(top)

def isPalindrome(s):
    pal = [i for i in str(s)]
    for j in range(int(len(pal)/2)):
        if pal[j] != pal[len(pal)-j-1]:
            return False;
    return True

def smallMult():
    arr = range(2,21)
    mult = 1
    for i in arr:
        mult = mult * i

    for i in arr:
        while helperSmallMult(mult/i,arr):
            mult = mult/i
    print (int(mult))


def helperSmallMult(n,arr):
    for i in arr:
        if n%i != 0:
            return False
    return True

def sumSquareDiff():
    n = 100
    sum1 = n*(n+1)*(2*n+1)/6
    for i in range(1,n):
        n = n + i
    sum2 = pow(n,2)
    print(int(sum2-sum1))

def nthPrime(n):
    if n == 1:
        print(2)
    ret = 1
    for i in range(n-1):
        ret += 2
        while not isPrime(ret):
            ret += 2
    print(ret)
        
def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(n/2)+1,2):
        if n%i == 0:
            return False
    return True

def largProdSer():
    ser = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    digits = []
    for dig in ser:
        digits.append(int(dig))

    top = 0
    chainlen = 13
    for i in range(len(digits)-chainlen):
        prod = 1
        for j in range(chainlen):
            prod = prod * digits[i+j]
        top = max(top,prod)
    print(top)

def specPythTripl():
    lim = 1000
    for i in range(1,lim+1):
        for j in range(i,lim+1-i):
            k = lim-i-j
            if k > j and k > i and j > i:
                if (i*i + j*j) == k*k:
                    if i+j+k == lim:
                        return (i*j*k)

def sumOfPrimes():
    lim = 2000000
    test = [True for i in range(lim+1)]
    test[0] = False
    test[1] = False

    for i in range(2,lim+1):
        if test[i] == True:
            for j in range(i*i,lim+1,i):
                test[j] = False

    tot = 0
    for k in range(lim+1):
        if test[k]:
            tot += k
    return tot

def highDivTriangNum():
    lim = 1000000
    tn = 0
    for i in range(1,lim+1):
        tn += i
        divs = 0
        if tn >= 62370000:
            for j in range(1,int(math.sqrt(tn+1))):
                if tn%j == 0:
                    divs += 2
                    if j*j == tn:
                        divs -= 1
                    if divs >= 500:
                        return tn

def largeSum():
    txt = '37107287533902102798797998220837590246510135740250463769376774900097126481248969700780504170182605387432498619952474105947423330951305812372661730962991942213363574161572522430563301811072406154908250230675882075393461711719803104210475137780632466768926167069662363382013637841838368417873436172675728112879812849979408065481931592621691275889832738442742289174325203219235894228767964876702721893184745144573600130643909116721685684458871160315327670386486105843025439939619828917593665686757934951621764571418565606295021572231965867550793241933316490635246274190492910143244581382266334794475817892575867718337217661963751590579239728245598838407582035653253593990084026335689488301894586282278288018119938482628201427819413994056758715117009439035398664372827112653829987240784473053190104293586865155060062958648615320752733719591914205172558297169388870771546649911559348760353292171497005693854370070576826684624621495650076471787294438377604532826541087568284431911906346940378552177792951453612327252500029607107508256381565671088525835072145876576172410976447339110607218265236877223636045174237069058518606604482076212098132878607339694128114266041808683061932846081119106155694051268969251934325451728388641918047049293215058642563049483624672216484350762017279180399446930047329563406911573244438690812579451408905770622942919710792820955037687525678773091862540744969844508330393682126183363848253301546861961243487676812975343759465158038628759287849020152168555482871720121925776695478182833757993103614740356856449095527097864797581167263201004368978425535399209318374414978068609844840309812907779179908821879532736447567559084803087086987551392711854517078544161852424320693150332599594068957565367821070749269665376763262354472106979395067965269474259770973916669376304263398708541052684708299085211399427365734116182760315001271653786073615010808570091499395125570281987460043753582903531743471732693212357815498262974255273730794953759765105305946966067683156574377167401875275889028025717332296191766687138199318110487701902712526768027607800301367868099252546340106163286652636270218540497705585629946580636237993140746255962240744869082311749777923654662572469233228109171419143028819710328859780666976089293863828502533340334413065578016127815921815005561868836468420090470230530811728164304876237919698424872550366387845831148769693215490281042402013833512446218144177347063783299490636259666498587618221225225512486764533677201869716985443124195724099139590089523100588229554825530026352078153229679624948164195386821877476085327132285723110424803456124867697064507995236377742425354112916842768655389262050249103265729672370191327572567528565324825826546309220705859652229798860272258331913126375147341994889534765745501184957014548792889848568277260777137214037988797153829820378303147352772158034814451349137322665138134829543829199918180278916522431027392251122869539409579530664052326325380441000596549391598795936352974615218550237130764225512118369380358038858490341698116222072977186158236678424689157993532961922624679571944012690438771072750481023908955235974572318970677254791506150550495392297953090112996751986188088225875314529584099251203829009407770775672113067397083047244838165338735023408456470580773088295917476714036319800818712901187549131054712658197623331044818386269515456334926366572897563400500428462801835170705278318394258821455212272512503275512160354698120058176216521282765275169129689778932238195734329339946437501907836945765883352399886755061649651847751807381688378610915273579297013376217784275219262340194239963916804498399317331273132924185707147349566916674687634660915035914677504995186714302352196288948901024233251169136196266227326746080059154747183079839286853520694694454072476841822524674417161514036427982273348055556214818971426179103425986472045168939894221798260880768528778364618279934631376775430780936333301898264209010848802521674670883215120185883543223812876952786713296124747824645386369930090493103636197638780396218407357239979422340623539380833965132740801111666627891981488087797941876876144230030984490851411606618262936828367647447792391803351109890697907148578694408955299065364044742557608365997664579509666024396409905389607120198219976047599490197230297649139826800329731560371200413779037855660850892521673093931987275027546890690370753941304265231501194809377245048795150954100921645863754710598436791786391670211874924319957006419179697775990283006991536871371193661495281130587638027841075444973307840789923115535562561142322423255033685442488917353448899115014406480203690680639606723221932041495354150312888033953605329934036800697771065056663195481234880673210146739058568557934581403627822703280826165707739483275922328459417065250945123252306082291880205877731971983945018088807242966198081119777158542502016545090413245809786882778948721859617721078384350691861554356628840622574736922845095162084960398013400172393067166682355524525280460972253503534226472524250874054075591789781264330331690'
    tot = 0
    for i in range(100):
        tot+= int(txt[i*50:i*50+50])
    tot = str(tot)
    return (tot[:10])

def longCollatzSeq():
    upto = 1000001
    d = {}
    d[1] = 1
    maxc = 1
    maxn = 1
    for i in range(2,upto):
        n = i
        c = 1
        while n != 1:
            if n in d:
                c += d[n]-1
                n = 1
            elif n%2 == 0:
                n = int(n/2)
                c += 1
            else:
                n = 3*n + 1
                c += 1
        d[i] = c
        if maxc < c:
            maxc = c
            maxn = i
    return maxn

def powDigSum():
    return reduce(lambda x, y: x+y, [int(i) for i in str(pow(2,1000))])

def factDigSum():
    return reduce(lambda x, y: x+y, [int(i) for i in str(math.factorial(100))])

def getDivs(n):
    arr = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            arr.append(i)
            if i == int(n/i):
                continue
            arr.append(int(n/i))
    arr.sort()
    return arr[:-1]

def getDivs2(n):
    arr = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            arr.append(i)
            if i == int(n/i):
                continue
            arr.append(int(n/i))
    arr.sort()
    return arr[1:]

def amicableNums():
    d = {}
    tot = 0
    for i in range(1,10000):
        if (sum(getDivs(i)) in d) and d[sum(getDivs(i))]==i:
            print(sum(getDivs(i)))
            print(i)
            tot += i + sum(getDivs(i))
        d[i] = sum(getDivs(i))
    return tot

def fib1000digs():
    fib = [1,1,2]
    ind = 3
    while True:
        fib[0] = fib[1]
        fib[1] = fib[2]
        fib[2] = fib[0] + fib[1]
        ind += 1
        if len(str(fib[2])) == 1000:
            return ind

def distinctPows():
    terms = []
    for i in range(2,101):
        for j in range(2,101):
            terms.append(i ** j)
    return len(list(set(terms)))

def digFithPows():
    ret = 0
    for i in range(2,194980):
        if (sum([int(j)**5 for j in str(i)])) == i:
            print(i)
            ret += i
    return ret

def coinSums():
    c = 0
    start = 200
    for i in range(2):
        rem200p = start - i*200
        if rem200p == 0:
            c+= 1
            continue
        for j in range(3):
            rem100p = rem200p - j*100
            if rem100p == 0:
                c+= 1
                continue
            for k in range(5):
                rem50p = rem100p - k*50
                if rem50p == 0:
                    c+= 1
                    continue
                for l in range(11):
                    rem20p = rem50p - l*20
                    if rem20p == 0:
                        c+= 1
                        continue
                    for m in range(21):
                        rem10p = rem20p - m*10       
                        if rem10p == 0:
                            c+= 1
                            continue
                        for n in range(41):
                            rem5p = rem10p - n*5       
                            if rem5p == 0:
                                c+= 1
                                continue
                            for o in range(101):
                                rem2p = rem5p - o*2       
                                if rem2p == 0:
                                    c+= 1
                                    continue
                                if rem2p > 0:
                                    c+= 1
    return c

def digCancFracts():
    digs = ['1','2','3','4','5','6','7','8','9']
    nump = 1
    denp = 1
    for num in range(10,99):
        for den in range(num+1,100):
            for d in digs:
                if (d in str(num) and d in str(den)) and '0' not in str(den):
                    if int(str(num).replace(d,'',1))/int(str(den).replace(d,'',1)) == num/den:
                        nump = nump * num
                        denp = denp * den
    for div in getDivs2(nump):
        while nump%div == 0 and denp%div == 0:
            nump = int(nump/div)
            denp = int(denp/div)
    return denp

def digFacts():
    ret = 0
    for i in range(3,362881):
        fact = 0
        for d in str(i):
            fact += math.factorial(int(d))
        if fact == i:
            print(i,fact)
            ret += i
    return ret

def circHelper(n):
    ret = []
    n = str(n)
    for i in range(len(n)):
        ret.append(int(n))
        n = n[-1:]+n[:-1]
    return list(set(ret))

def circPrimes():
    lim = 1000000
    test = [True for i in range(lim+1)]
    test[0] = False
    test[1] = False

    for i in range(2,int(math.sqrt(lim+1))+1):
        if test[i] == True:
            for j in range(i*i,lim+1,i):
                test[j] = False

    primes = []
    for k in range(lim+1):
        if (test[k]) and (not k in primes):
            carr = circHelper(k)
            if all(test[c] for c in carr):
                primes += carr
    return len(primes)

def truncHelper(n):
    numl = str(n)
    numr = str(n)
    ret = [n]
    for i in range(len(str(n))-1):
        numl = numl[1:]
        numr = numr[:-1]
        ret.append(int(numl))
        ret.append(int(numr))
    return ret

def truncPrimes():
    lim = 800000
    test = [True for i in range(lim+1)]
    test[0] = False
    test[1] = False

    for i in range(2,int(math.sqrt(lim+1))+1):
        if test[i] == True:
            for j in range(i*i,lim+1,i):
                test[j] = False

    primes = []
    for k in range(23,lim+1):
        if all(test[c] for c in truncHelper(k)):
            primes.append(k)
    return (primes)
            
    
start = time.time()
#function
end = time.time()
print(end - start)

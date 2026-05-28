num = int(input('Enter 3 digit number')) ;
ans = (num%10) ;
num //= 10 ;
ans += ( num % 10) ;
num //= 10 ;
ans += num ;
print('Digit sum of given three digit number is ' , ans )

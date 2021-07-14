secure = (('a','@'),('b','%'),('c','~'),('d','^'),('e','&'),('f','('),('g',')'),
          ('h','#'),('i','_'),('j','-'),('k','='),('l',';'),('m',':'),('n','"'),
          ('o',','),('p','<'),('q','.'),('r','>'),('s','/'),('t','?'),('u','{'),
          ('v','}'),('w','['),('x',']'),('y',''),('z','"*'),
          ('Z','+'),('2','-'),('3','*'),('4','A'),('5','B'),('6','C'),('7','E'),
          ('8','M'),('9','K'),('0','**'),)

def securePassword(generate):
    for a,b in secure:
        generate = generate.replace(a,b)
    return generate

if __name__ == '__main__':
    generate = input('Enter the Password : ')
    generate = securePassword(generate)
    print(f"Secured Password is .: {generate}")

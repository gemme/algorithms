/* eslint-disable complexity */




/**
 * karatsuba
 * 
 * @param x first factor
 * @param y second factor
 * @returns factor 
 */
function karatsuba(x, y){
    const n = `${x}`.length;
    if(n === 1){
        return x*y;
    }
    const pow = Math.pow(10, n / 2);
    const a = Math.floor(x / pow);
    const b = x % pow;
    const c = Math.floor(y / pow);
    const d = y % pow;
    let ac = 0, bd = 0, pq = 0, p = 0, q = 0;
    p = a + b;
    q = c + d;
    ac = karatsuba(a, c); // 12 * 56 // 1 * 5  // 3 * 7
    bd = karatsuba(b, d); // 34 * 78 // 2 * 6  // 4 * 8
    // Todo: compute pq recursively
    pq = p * q;//karatsuba(p, q); // 12 + 56
    const adbc = pq - ac -bd;
    return Math.pow(10, n) * ac + Math.pow(10, n/2) * adbc + bd;
}

const result = karatsuba(1234, 5678)
console.log(result);

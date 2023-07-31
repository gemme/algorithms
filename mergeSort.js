/**
 * mergeSort
 * 
 * @param input array unsorted
 * @returns sorted array 
 */
function mergeSort(input){
    const n = input.length
    if(n === 1){
        return input;
    }
    const left = input.slice(0, input.length / 2);
    const right = input.slice((input.length / 2), input.length);
    const C = mergeSort(left);
    const D = mergeSort(right);
    
    /**
     * merge
     * 
     * @returns merge array 
     */
    function merge(){
        let i = 0, j = 0;
        let sorted = [];
        for(let k = 0; k < n  ; k++){
            if(C[i] > D[j]){
                sorted.push(D[j]);
                j++;
            } else {
                sorted.push(C[i]);
                i++;
            }
        }
        return sorted;
    }
    return   merge();
}
const l = 100;
const toSort = Array.from({ length: l }, (v, i) =>  l - i );
const sorted = mergeSort(toSort);
console.log(sorted);
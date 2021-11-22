let haystack = [1, 5, 8, 9, 12, 21, 30, 35, 36, 37, 40, 50, 79, 89, 94, 99];
console.log(haystack);
let needle = 2;
let isin = false;

let left = 0;
let right = haystack.length - 1;
var middle = Math.floor((left + right) / 2);

while (left <= right) {
    console.log(left, right, middle);
    if (needle == haystack[middle]) {
        isin = true;
        break;
    } else if (haystack[middle] < needle) {
        left = middle + 1;
    } else {
        right = middle - 1;
    }


    middle = Math.floor((left + right) / 2);
}
console.log("Needle is" + (isin ? "" : "not") + "in Haystack");
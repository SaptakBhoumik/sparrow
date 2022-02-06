// program to display fibonacci sequence using recursion
function fibonacci(num) {
    if(num < 2) {
        return num;
    }
    else {
        return fibonacci(num-1) + fibonacci(num - 2);
    }
}

const nTerms = 15;
for(let i = 0; i < nTerms; i++) {
    console.log(fibonacci(i));
}
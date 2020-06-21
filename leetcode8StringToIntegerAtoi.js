/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    str=str.replace(/ +/g,'');
    var sign;
    if(str[0]=='-') sign=false;
    else true;
    var i=0;
    if(sign==false){
        i++;
    }
    while(i<str.length && str[i]>='0' && str[i] <='9'){
        i++;
    }
    var absolute;
    if(sign==false) {
        absolute=str.slice(1,i);
    } else {
        absolute=str.slice(0,i);
    }
    console.log(absolute);
    return str;
};

console.log(myAtoi("   -42       asd   "));
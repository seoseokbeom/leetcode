function solution(new_id) {
    # //1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    let lowercase = new_id.toLowerCase()
    # //2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    reg = /[\{\}\[\]\/?, : |\)*~`!^\+ <> @\  # $%&\\\=\(\'\"]/gi
    if (reg.test(lowercase)) {
        lowercase = lowercase.replace(reg, "")
    }
    # //3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    console.log(lowercase)

    for (i= 0
         i < lowercase.length - 1
         i++) {
        if (lowercase[i] == lowercase[i + 1] & & lowercase[i] == ".") {
            // console.log("---")
            lowercase = lowercase.slice(0, i) + lowercase.slice(i + 1)
            i--
        }
    }
    console.log(lowercase)
    # //4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if (lowercase.charAt(0) == ".") {
        lowercase = lowercase.slice(1)
    }

    if (lowercase.charAt(lowercase.length - 1) == ".") {
        lowercase = lowercase.slice(0, lowercase.length - 1)
    }
    # //5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.

    if (lowercase.length == 0) {
        lowercase += "a"
    }
    # //6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # //     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if (lowercase.length >= 16) {
        lowercase = lowercase.slice(0, 15)
    }
    if (lowercase.length == 15 & & lowercase.charAt(14) == ".") {
        lowercase = lowercase.slice(0, 14)
    }
    # //7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    console.log(lowercase)
    if (lowercase.length == 1) {
        lowercase += lowercase.charAt(0)
        lowercase += lowercase.charAt(0)
    } else if (lowercase.length == 2) {
        lowercase += lowercase.charAt(1)
    }
    return lowercase
}
console.log(solution("=.="))

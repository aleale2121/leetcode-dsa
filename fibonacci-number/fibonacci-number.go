var cache map[int]int=make(map[int]int)
var res int
func fib(n int) int {
    if v,ok:=cache[n];ok{
        return v
    }
    if n<2{
        res=n
    }else{
        res=fib(n-1)+fib(n-2)
    }
    cache[n]=res
    return res       
}
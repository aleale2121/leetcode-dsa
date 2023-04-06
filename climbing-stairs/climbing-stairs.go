
func climbStairs(n int) int {
    cache :=make(map[int]int)
    var getValue func(int) int
    getValue=func(i int) int{
        if v,ok:=cache[i];ok{
            return v
        }
        if i<2{
             cache[i]=1
        }else{
             cache[i]=getValue(i-1)+getValue(i-2)
        }
        return  cache[i]
    }
    ans:=getValue(n) 
    return  ans
}

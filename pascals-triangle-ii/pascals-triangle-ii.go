type vertex struct{
    X int
    Y int
}
func getRow(rowIndex int) []int {
    cache:=make(map[vertex]int)
    ans:=make([]int,0)
    var result int
    var getValue func(int,int)int
    getValue= func (i,j int) int{
        if v,ok:=cache[vertex{X:i,Y:j}];ok{
            return v
        }
        if i==0 || j==0 || i==j{
            result = 1
        }else{
            result = getValue(i-1,j-1)+getValue(i-1,j)    
        }
        cache[vertex{X:i,Y:j}]=result
        return result
    } 
    

    for j:=0;j<rowIndex+1;j++{
        ans=append(ans,getValue(rowIndex,j))
    }
    return ans   
}

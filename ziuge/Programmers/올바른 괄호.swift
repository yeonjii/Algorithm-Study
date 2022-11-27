import Foundation

func solution(_ s:String) -> Bool
{
    var ans:Bool = false
    var stack: [String] = []
    
    if s.count % 2 == 1 {
        return false
    }
    
    for i in s {
        if i == ")" && stack.count != 0 {
            _ = stack.popLast()
        } else {
            stack.append(String(i))
        }
    }
    
    if stack.count == 0 {
        ans = true
    }

    return ans
}

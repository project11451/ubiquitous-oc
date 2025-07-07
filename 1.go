package main
import "fmt"

// 全局整型变量声明，默认值为0
var x, y int
// 分组声明，a为整型默认0，b为布尔型默认false
var (
	a int
	b bool
)


// 声明并初始化整型变量c、d
var c, d int = 1, 2
// 声明并初始化e为整型，f为字符串
var e, f = 123, "hello"

func main() {
	// 使用短变量声明，g为整型，h为字符串
	g, h := 123, "hello"
	// 打印所有变量的值
	fmt.Println(x, y, a, b, c, d, e, f, g, h)
}
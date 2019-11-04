namespace java com.server
enum Operation{
    ADD = 1,
    SUBTRACT = 2,
    MULTIPLY = 3,
    DIVIDE = 4
}
exception calException{
    1: string reason

}
struct CalParam{
    1:i32 num1,
    2:i32 num2,
    3:Operation op
}
service Calculator{
    i32 getResult(1: CalParam param) throws (1: calException reason)
}
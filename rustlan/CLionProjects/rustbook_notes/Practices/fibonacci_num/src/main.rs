fn main() {
    for num in 0..25 {
        println!("fibo of {} = {}", num, fibo(num));
    }
}

fn fibo(n: u32) -> u32 {
    if n <= 0{
        return 0;
    } else if n == 1 {
        return 1;
    }
    fibo(n -1) + fibo(n -2)
}

fn main() {
    println!("F to C = {}", f_to_c(92));
}

fn c_to_f(c: i32) -> i32 {
    let f = (c * 9/5)+ 32;
    return f;
}

fn f_to_c(f: i32) -> i32 {
    let c = (f - 32) *  5/9;
    return c;
}

// Equations
//  C to F:
//      (c ×  9/5 ) + 32 = f
// F to C
//      (f − 32) ×  5/9  = c
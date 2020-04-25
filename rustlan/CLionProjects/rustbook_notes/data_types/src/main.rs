fn main() {
    // Data Types
        // we must tell rust what data type a variable has all the time
        // sometime the compiler can tell based on the value of the variable
        // if the compiler doesn't know the type, we get a type annotation error

    // Scalar Types (single value types)
    // Integer Types (can be signed or unsigned, use signed if we are gonna have negative numbers)
    let a: i8 = 100; // we declared a signed integer type of 8 bits, it can store num from -128 to 127
    let b: u8 = 230; // we declared an unsigned integer type of 8 bits, can store num from 0 to 255
    // we can created an integer type to up to 128 bit, 32 is enough most of the time
    // signed variant can store numbers from -(2^n - 1) to 2^n - 1 - 1
    // Unsigned variants can store numbers from 0 to 2^n - 1
    // just use isize or usize when indexing some sort of collection
    println!("The value of a and b are: {}, {}", a,b);


    // Floating-Point Types
    let c: f32 = 3.256; // 32bit
    let d: f64 = 3.984565; // 64bit (use this one, more precise and run as fast)

    println!("the value of c and d are: {}, {}", c,d);


    // Numeric Operations
    let sum =  5 + 10; // addition
    let difference = 95.5 - 4.4; // subtraction
    let product = 4 * 30; // multiplication
    let quotient = 56.7 / 32.2; // division
    let remainder = 43 % 5;


    // Boolean Type
    let t = true;
    let f: bool = false;


    // Character Type
    let mychar = 'z'; // single quote for char
    let heart_eyed_cat = 'v'; // a char in rust is a Unicode Scalar Value (include even emojik)


    // Compound Types
    // Tuple type (once declared, cannot change size)
    let tup = (500, 6.4, 1); // adding type annotations of each value is optional
    let five_hundred = tup.0; // accessing tuple items with index
    let one = tup.2;
    let (var1, var2, var3) = tup; // tup can be unpacked like this
    println!("the value of var2 is: {}", var2);

    // Array Type (fixed length and values have same data type)
    let ar = [1, 2, 3, 4, 5]; // data type was not specified but all have same data type
    let arr:[i32;5] = [1,2,3,4,5]; // data type and length is specified
    // array_name: [item_data_type; number_of_item] = [...]
    let months = ["January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"];
    let ar2 =  [3;5]; // same as let a = [3, 3, 3, 3, 3];
    println!("{}", ar2[3]); // get specific value with index
    // if index is out of range, program will still compile but give a runtime error

}

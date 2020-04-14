use std::any::Any;

fn main() {
    // Variables

    // By default variables are immutable
    let my_variable = 5;
    println!("The value of my_variable is: {}", my_variable);
    // my_variable = 10 // cannot assign twice to immutable variable
    // println!("The value of my_variable is: {}", my_variable) // error

    // mutable variables
    let mut second_variable = 10; // we initialised a mutable variable
    println!("second_variable's value is now {}", second_variable);
    second_variable = second_variable * 11;
    println!("second_variable's value is now {}", second_variable);
    // second_variable = "hello mate!"; // the variable is mutable, but the data type must remain the same
    // println!("second_variable's value is now {}", second_variable);

    // Constants (can be declared globally, always running while the program is running)
    const  SPEED_LIGHT: i32 = 999999999; // constant are immutable and always immutable

    // Shadowing(initializing a new variable with same name another value, old variable is shadowed)
    let x = "four";
    println!("the value of x is: {}", x);
    let x = x.len(); // we can change data type, since we effectively made a new variable
    println!("the value of x is: {}", x);
    // x = 98; // error, x is still immutable


}

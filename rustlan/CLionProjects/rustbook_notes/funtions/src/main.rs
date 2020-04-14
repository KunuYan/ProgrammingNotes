// Function
fn main() {
    println!("Hello, world!");

    another_function(5, "Tony");
    let mut mut_z= 1;
    mut_z = stuff(1);
    println!("mut_z is: {}", mut_z);
}

fn another_function(x: i32, y: &str) {
    println!("The value of x is: {}.", x);
    println!("{} is {} years old.", y,x)
}

// Statements: whatever finishes with ';'
// statement, return no values, can't assign a let statement to an other statement. in rust you an't do x=y=6.
//  fn main() {
    //  let y = 6;
//  }


// expression: no ':' or have a return statement
// return value by default
fn stuff(z: u8) -> u8{
    println!("calling this function makes it a statement"); // the printlm!() is ac function, the calling of it is a statement
    let my_print = println!("Now it's an expression asigned to the variable my_print");
    z + 1 // this is an expression because it returned an value, rust expression are return by the func by default
    // you could put return before z + 1, that why you have option to finish with ;
}

fn express_in_statement() {
    let x = 5;

    let y = {
        let x = 3;
        x + 1 // function in rust return the last expression, but you can use return statement to return a specific value
    }; // an expression can be assigned to a statement

    println!("The value of y is: {}", y);
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
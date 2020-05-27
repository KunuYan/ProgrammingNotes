use std::io;
// the '::' indicate that the right function, type,module, library or package
// is an associate function of the left type,module, library or package
// like python dot method(module.function())
use std::cmp::Ordering;
use rand::Rng;


fn main() {
    get_input();
}


fn get_input() {
    let secret_number = rand::thread_rng().gen_range(1, 101);
    println!("Guess the number!");

    loop {
        println!("Please input your guess.");
        let mut guess = String::new(); // create new instance of empty string
        io::stdin().read_line(&mut guess)
            // we use & to pass a mutable reference to our guess variable.
            // Reference are immutable by default.
            .expect("Failed to read line"); // it's more visible here than if written of same line
        // most associated functions return a result type, which contains a set of values.
        // Including an ok or err. We called expect() method associated to read_line() which read if our
        // result data, if err in crash the program and print the msg passed in.
        // ! this is not "try and except", just a quick way to check errors

        let guess: u32 = match guess.trim().parse() {
            // we often use shadowing when changing data type of variable.
            // we call trim() on guess string variable to remove spaces and '/n'.
            // next we parse the string into a u32
            Ok(num) => num,
            Err(_) => continue, // if we get an error we want to continue
            // '_' is a catchall value
        };

        println!("You guessed: {}", guess);

        // comparing numerical data types like this is better then using if statements.
        // the match method works a bit like the python Doctest
        match guess.cmp(&secret_number) {
            // we use cmp to compare guess to the secret number, returns Ordering.
            // Ordering is an enum like Result, it's variants are Less, Greater, Equal
            Ordering::Less => println!("Too small"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
            // match will check the cases(which variant was returned) and run the code associated to it
        }
    }

}
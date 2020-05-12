fn if_tester(my_number: i32) {
    //operators: <, >, !=, ==
    if my_number < 5 {
        println!("number is smaller than 5");
    } else if my_number > 5 {
        println!("number is bigger than 5");
    } else if my_number == 0 {
        println!("number is 5");
    }
}

fn let_if(condition: bool) {
    // the value that will pontentially be assigned to my_number must be the same data type
    let my_number = if condition {
        1
    } else {
        0
    };

    println!("the value of number from let_if is: {}", my_number);
}

fn control() {
    let mut my_number = 3;
    if_tester(my_number);
    my_number = 7;
    if_tester(my_number);
    let_if(true);
}

// had to specified that looping() return i32
fn looping() -> i32 {
    let mut num = 1;
    let result = loop {
        num += 1;

        if num == 25 {
            // specified that result = num
            break num;
        }
    };
    return result;
}

fn while_loop() {
    // works just like python
    let mut number = 3;
    while number != 0 {
        println!("{}!", number);
        number -= 1;
    } // you can have other loops and if statements breaks statement in them, here
    println!("LIFTOFF!!!");
}

fn for_loop() {
    let arr:[i32;6] = [10, 20, 30, 40, 50, 60];
    // arrays have a predefined iter() function wich you must call to use for loop
    for e in arr.iter() {
        println!("the value is {}", e);
    }

    //let mut index = 0;
    // done in a while loop
    //while index < 6 {
    //    println!("the value is {}", arr[index]);

    //    index += 1;
    //}
}

fn main() {
    control();
    // had to specified that looping() return i32
    let my_result = looping();
    println!("result is {}", my_result + 1);
    while_loop();
    for_loop();

    for my_num in (1..10).rev() {
        println!("{}!", my_num);
    }
    println!("LIFTOFF!!!");
}
